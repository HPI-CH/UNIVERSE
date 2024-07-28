import numpy as np
import pandas as pd
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.pipeline import make_pipeline
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import (TimeSeriesSplit, KFold, ShuffleSplit,
                                     StratifiedKFold, GroupShuffleSplit,
                                     GroupKFold, StratifiedShuffleSplit, RepeatedStratifiedKFold)
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import KFold, GroupKFold
from sklearn.model_selection import LeaveOneGroupOut,  LeaveOneOut
from sklearn.model_selection import ShuffleSplit
import sklearn.metrics as metrics
import joblib

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.mixture import GaussianMixture
import warnings 
import random
random.seed(9700)
warnings.filterwarnings('ignore')




def make_pipeline(model_name):

    if 'lr' in model_name:
        #### logistic regression
        pipeline = Pipeline(
            [
                ('scaler', StandardScaler()), 
                ('var_filter', VarianceThreshold()),
                ('model', LogisticRegression(random_state=42)) # logistic regression pipeline 
            ]
        )

        if "rand" in model_name:
            # a larger search space for random search
            grid = {
                    'model__penalty': ['l2'], 
                    'model__solver': ['liblinear', 'saga', 'newton-cg', 'lbfgs', 'sag'],
                    'model__C':np.logspace(-3,3,7),
                }

        else:
            # parameter grids for GridSearchCV
            grid = [
                {
                    'model__penalty': ['l1'], 
                    'model__solver': ['liblinear', 'saga'], 
                    'model__C':np.logspace(-3,3,7),
                },
                
                {
                    'model__penalty': ['l2'], 
                    'model__solver': ['liblinear', 'saga', 'newton-cg', 'lbfgs'],
                    'model__C':np.logspace(-3,3,7),
                }
            ]

    return pipeline, grid

def nested_cv(X, y, model_name, estimator, param_grid, print_results, save_results, cv_base_path, participant_id): 
    """
    X: DataFrame of features
    y: Series of target labels
    model_name: string that contains model and split information. 'ss': shuffle split; 'logo': leave one group (i.e. subject) out; 'skf': stratified k fold
    implemented model pipelines: 'svm': support vector classifier, 'lr': logistic regression, 'rf': random forest.
    exampel model_name: svm_ss (with data from all subjects); rf_skf_sub_01 (with data from sub_01)
    """

    train_test_info = {
        'model': model_name,
        'best_cv_score': [],
        'best_cv_parameter': [],
        'test_accuracy': [],
        'test_f1': [],
        'test_precision': [],
        'test_recall':[]
    }

    test_predictions = {
        'model': model_name,
        'y_test': [],
        'y_pred': []
    }

    cv_obj_path = os.path.join(
                cv_base_path, 
                model_name + '_all_CVs_'+str(participant_id)
    )

    os.makedirs(cv_obj_path, exist_ok=True)  # create path if not exist
    if 'kfold' in model_name: 
        print('kfold')
        outer_cv = KFold(n_splits= 5, shuffle=True, random_state=42)
        enumerate_splits = outer_cv.split(X,y)

    i = 0  # for documenting number folds
    for train_index, test_index in enumerate_splits:
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        print('Cross validation ' + str(i))
        if print_results:
            print('X_train: ' + str(X_train.shape))
            print('Y_train: ' + str(y_train.shape))
            print('X_test: ' + str(X_test.shape))
            print('y_test: ' + str(y_test.shape))

        # do grid serach on the test set to find optimal hyperparameters   
#         inner_cv = 5 # outer_cv

        if 'rand' in model_name:
            print('RandomizedSearchCV')
            CV = RandomizedSearchCV(estimator=estimator, param_distributions=param_grid, n_iter=50, cv=inner_cv, scoring='accuracy', verbose=2, random_state=42, n_jobs=16)
        else:
            print('GridSearchCV')
            
        if ('_ss' in model_name) or ('_skf' in model_name) or ('_loo' in model_name) or ('_kfold' in model_name): 
            CV.fit(X_train, y_train) 
        elif '_logo' in model_name: 
            groups_train, groups_test = groups.loc[train_index], groups.loc[test_index]
            CV.fit(X_train, y_train, groups=groups_train) 

        # use best hyperparameters on the test set
        y_pred = CV.predict(X_test)

        # save the values
        train_test_info['best_cv_score'].append(CV.best_score_)
        train_test_info['best_cv_parameter'].append(CV.best_params_)
        train_test_info['test_accuracy'].append(metrics.accuracy_score(y_test, y_pred))
        train_test_info['test_f1'].append(metrics.f1_score(y_test, y_pred, zero_division=0))
        train_test_info['test_precision'].append(metrics.precision_score(y_test, y_pred))
        train_test_info['test_recall'].append(metrics.recall_score(y_test, y_pred))

        test_predictions['y_test'].append(y_test.to_list())
        test_predictions['y_pred'].append(y_pred.tolist())

        if print_results:
            print('Best score and parameter combination = ')
            print(CV.best_score_)    
            print(CV.best_params_)
            print('Model accuracy score with CV optimized hyperparameters: {0:0.4f}'. format(metrics.accuracy_score(y_test, y_pred)))
            print('Model F1 score with CV optimized hyperparameters: {0:0.4f}'.format(metrics.f1_score(y_test, y_pred)))
            print("Precision: {0:0.4f}". format(metrics.precision_score(y_test, y_pred)))
            print("Recall: {0:0.4f}". format(metrics.recall_score(y_test, y_pred)))
            print('\n')

        if save_results:
            # save the CV object to disk
            model_filepath = os.path.join(
                cv_obj_path,
                model_name + '_grid_search_CV' + str(i) + '.pkl'
            )
            joblib.dump(
                CV, 
                model_filepath
            )
        i += 1

    if save_results:
        
        model_filepath = os.path.join(
            cv_base_path,
            model_name + "_train_test_info_"+str(participant_id)+".pkl"
        )
        joblib.dump(
            train_test_info, 
            model_filepath
        )
        
        model_filepath = os.path.join(
            cv_base_path,
            model_name + "_test_predictions_"+str(participant_id)+".pkl"
        )
        joblib.dump(
            test_predictions, 
            model_filepath
        )

    return y_test, y_pred, train_test_info

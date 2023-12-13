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
            # l1 lasso l2 ridge
            #  Lasso shrinks the less important feature’s coefficient to zero thus, removing some feature altogether. 
            # So, this works well for feature selection in case we have a huge number of features.

    elif 'svm' in model_name:
        #### SVM
        pipeline = Pipeline(
            [
                ('scaler', StandardScaler()),
                ('var_filter', VarianceThreshold()),
                ('model', SVC())
            ]
        )

        # parameter grids for GridSearchCV
        if "rand" in model_name:
            # a larger search space for random search
            grid = {'model__C': np.logspace(-6,0,7), 'model__gamma': np.logspace(-6,0,7), 'model__kernel': ['rbf']}
        
        else:
#             grid = [
#                 {'base_estimator__C': [0.01, 0.05, 0.1, 0.5, 1, 10, 100, 1000], 'model__kernel': ['linear']},
#                 {'base_estimator__C': np.logspace(-6,0,7), 'model__gamma': np.logspace(-6,0,7), 'model__kernel': ['rbf']},
#                  'max_samples' : [0.05, 0.1, 0.2, 0.5]
#             ]

            grid = [
                {'model__C': [0.01, 0.05, 0.1, 0.5, 1, 10, 100, 1000], 'model__kernel': ['linear']},
                {'model__C': np.logspace(-6,0,7), 'model__gamma': np.logspace(-6,0,7), 'model__kernel': ['rbf']},
            ]

    elif 'rf' in model_name:
    #### random forest
        pipeline = Pipeline(
            [
                ('scaler', StandardScaler()),
                ('var_filter', VarianceThreshold()),
                ('model', RandomForestClassifier(random_state=42, n_jobs=-1))
            ]
        )
        
        if "rand" in model_name:
            # a larger search space for random search
            grid = {
                'model__bootstrap': [True, False],
                'model__max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
                'model__max_features': ['auto', 'sqrt'],
                'model__min_samples_leaf': [1, 2, 3, 4, 5, 6],
                'model__min_samples_split': [2, 5, 10],
                'model__n_estimators': [50, 100, 200, 300, 400, 500]
            }
        else:
            grid = {
                'base_estimator__n_estimators': [10, 100, 200],  # num. of trees
                'base_estimator__min_samples_leaf': [1, 3, 5 ],  # "leaf size"
                'base_estimator__min_samples_split': [2, 4, 8],
                'max_samples' : [0.05, 0.1, 0.2, 0.5]
                }

#                         # parameter grids for GridSearchCV without bagging
#             grid = {
#                 'model__n_estimators': [10, 50, 100, 200, 400, 800],  # num. of trees
#                 'model__min_samples_leaf': [1, 2, 3, 4, 5, 6, 8, 10],  # "leaf size"
#                 'model__min_samples_split': [2, 4, 6, 8],
#                 'model__max_depth': [None, 1, 2, 5, 10, 20, 50, 100, 1000 ],
                
#                 }
            
    elif 'dt' in model_name:
    #### random forest
        pipeline = Pipeline(
            [('model', DecisionTreeClassifier(random_state=42))
            ]
        )
        
        if "rand" in model_name:
            # a larger search space for random search
            grid = {
                'model__bootstrap': [True, False],
                'model__max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
                'model__max_features': ['auto', 'sqrt'],
                'model__min_samples_leaf': [1, 2, 3, 4, 5, 6],
                'model__min_samples_split': [2, 5, 10],
                'model__n_estimators': [50, 100, 200, 300, 400, 500]
            }
        else:
            # parameter grids for GridSearchCV
            grid = {
                'base_estimator__min_samples_leaf': [1, 2, 3, 4, 5, 6, 8, 10],  # "leaf size"
                'base_estimator__min_samples_split': [2, 4, 6, 8],
                'base_estimator__max_depth': [None, 1, 2, 5, 10, 20, 50, 100, 1000 ],
                'max_samples' : [0.05, 0.1, 0.2, 0.5]
                
                }


    return pipeline, grid

def nested_cv(X, y, model_name, estimator, param_grid, print_results, save_results, cv_base_path, participant_id): #groups, 
    """
    X: DataFrame of features
    y: Series of target labels
    model_name: string that contains model and split information. 'ss': shuffle split; 'logo': leave one group (i.e. subject) out; 'skf': stratified k fold
    implemented model pipelines: 'svm': support vector classifier, 'lr': logistic regression, 'rf': random forest.
    exampel model_name: svm_ss (with data from all subjects); rf_skf_sub_01 (with data from sub_01)
    """
    
# #     model_name = 'svm_logo'  # 'ss': shuffle split; 'logo': leave one group (i.e. subject) out; implemented model pipelines: svm, lr, rf

#     if 'svm' in model_name:
#         print('Support Vector Classifier')
#         estimator = pipe_svm
#         param_grid = grid_svm
#     elif 'lr' in model_name:
#         print('Logistic Regression')
#         estimator = pipe_lr
#         param_grid = grid_lr
#     elif 'rf' in model_name:
#         print('Random Forest')
#         estimator = pipe_rf
#         param_grid = grid_rf
#         random_param_grid = random_grid_rf

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

    # # save column names of filtered X
    # with open(os.path.join(
    #         cv_obj_path,
    #         model_name + '_feature_names' + '.txt'
    #     ), 'w') as filehandle:
    #     json.dump(X.columns[estimator['var_filter'].get_support()].to_list(), filehandle)

    if 'kfold' in model_name: 
        print('kfold')
        outer_cv = KFold(n_splits= 5, shuffle=True, random_state=42)
        enumerate_splits = outer_cv.split(X,y)
    elif 'ss' in model_name: 
        print('ShuffleSplit')
        outer_cv = ShuffleSplit(n_splits= 5, test_size=0.20, random_state=42) # default test_size=0.0625
        enumerate_splits = outer_cv.split(X,y)
    elif 'logo' in model_name: 
        print('LeaveOneGroupOut split')
        outer_cv = LeaveOneGroupOut()
        enumerate_splits = outer_cv.split(X, y, groups=groups)
    elif 'skf' in model_name: 
        print('StratifiedKFold split')
        outer_cv = StratifiedKFold(n_splits=5)#, shuffle= True, random_state=9700) #RepeatedStratifiedKFold(n_splits=10, n_repeats=10,random_state=9700): did not really improve the performance of the model
        enumerate_splits = outer_cv.split(X, y)
    elif 'loo' in model_name: 
        print('LeaveOneOut')
        outer_cv = LeaveOneOut()
        enumerate_splits = outer_cv.split(X, y)

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

        ############################## DEBUG LOG REG CONVERGENCE ##############################

        # from sklearn.linear_model import LogisticRegression, SGDClassifier
        # import sys
        # 
        # # model = LogisticRegression(penalty='l1', solver='liblinear')  # 
        # model = SGDClassifier(loss='log')
        # model = model.fit(X_train, y_train)
        # print("Score of log reg: ", model.score(X_test, y_test))
        # sys.exit(0)


        ############################## DEBUG LOG REG CONVERGENCE ##############################

        # do grid serach on the test set to find optimal hyperparameters   
#         inner_cv = 5 # outer_cv

        if 'rand' in model_name:
            print('RandomizedSearchCV')
            CV = RandomizedSearchCV(estimator=estimator, param_distributions=param_grid, n_iter=50, cv=inner_cv, scoring='accuracy', verbose=2, random_state=42, n_jobs=16)
        else:
            print('GridSearchCV')
            
            if 'rf' in model_name:
                CV = GridSearchCV(BaggingClassifier(RandomForestClassifier(random_state=42, n_jobs=-1), max_features = 0.5), 
                                  param_grid, scoring = 'accuracy')
            elif 'dt' in model_name:             
                CV = GridSearchCV(BaggingClassifier(DecisionTreeClassifier(random_state=42), max_features = 0.5), 
                                  param_grid, scoring = 'accuracy')
#             elif 'svm' in model_name: 
#                 CV = GridSearchCV(BaggingClassifier(SVC((random_state=42), max_features = 0.5), 
#                                   param_grid, scoring = 'accuracy')
            elif ('svm' in model_name) or ('lr' in model_name):            
                CV = GridSearchCV(estimator=estimator, param_grid=param_grid, scoring='accuracy', verbose=0, n_jobs=-1)
        print(model_name)

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

        
#         # save results to json file
#         with open(
#             os.path.join(cv_base_path, model_name + "_train_test_info_"+str(participant_id)+".pkl"),
#             'w', encoding='utf-8') as f:
#             json.dump(train_test_info, f, ensure_ascii=False, indent=4)

#         with open(
#         os.path.join(cv_base_path, model_name + "_test_predictions_"+str(participant_id)+".pkl"),
#         'w', encoding='utf-8') as f:
#             json.dump(test_predictions, f, ensure_ascii=False, indent=4)

        # save column names of filtered X
#         with open(os.path.join(
#                 cv_obj_path,
#                 model_name + '_feature_names' + '.txt'
#             ), 'w') as filehandle:
#             json.dump(X.columns[CV.best_estimator_['var_filter'].get_support()].to_list(), filehandle)

    return y_test, y_pred, train_test_info



def get_classification_scores(model_names, cv_base_path):
    
#     score_names = [x + '_test_score' for x in model_names]
#     scores = []
#     for model in model_names:
#         score_path = os.path.join(
#             cv_base_path, 
#             model + "_train_test_info.json"
#         )
    score_names = [model_names + '_test_score']
    scores = []
    model=model_names
    score_path = os.path.join(
        cv_base_path, 
        model + "_train_test_info.json"
    )
    with open(score_path) as f:
        train_test_info = json.load(f)
    scores.append(train_test_info['test_accuracy'])
        
    # collect test scores for all cross validations for all models
    model_score_df = pd.DataFrame(scores, score_names).T

    # calculate summary statistics
    means = model_score_df.mean().to_frame()
    means.rename({0: 'mean'}, axis=1, inplace=True)
    std = model_score_df.std().to_frame()
    std.rename({0: 'std'}, axis=1, inplace=True)
    model_score_summary = pd.concat([means, std], axis=1)
    model_score_summary = model_score_summary.round(3)
    model_score_summary['mean_std'] = '$' + model_score_summary['mean'].astype(str) + ' \pm ' + model_score_summary['std'].astype(str) + '$'

    return model_score_df, model_score_summary


def plot_classification_results(model_name, cv_base_path): #classify
    
    model_score_df, _ = get_classification_scores(model_name, cv_base_path)

    plt.figure(figsize=(10, 7))
    ax = sns.boxplot(data=model_score_df)
    ax = sns.stripplot(data=model_score_df, color=".4", size=3)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

    plt.title('Model performance in classifying ')# + classify)
    plt.ylabel('Accuracy from cross validation')
    plt.xlabel('Models')
    plt.show()


def load_CV(cv_base_path, cv_name, cv_num, score_metric="accuracy"):
    """load cross validation objects from classification

    Args:
        cv_base_path (str): directory for all CV objects
        cv_name (str): name of the CV
        cv_num (int): fold number from cross validation
        score_metric (str, optional): which score. Defaults to "accuracy".

    Returns:
        [type]: loaded CV object, loaded test scores, list of feature names
    """
    model_name = cv_name

    # load CV object
    cv_obj_path = os.path.join(
                cv_base_path,
                model_name + '_all_CVs'
    )

    loaded_CV = joblib.load(os.path.join(
        cv_obj_path, 
        model_name + '_grid_search_CV' + str(cv_num) + '.pkl'
    ))
    # print(cv_obj_path, model_name + '_grid_search_CV' + str(cv_num) + '.pkl')
    # pd.DataFrame(loaded_CV.cv_results_)  # visualize loaded cv folds

    # load test score
    score_path = os.path.join(
            cv_base_path, 
            model_name + "_train_test_info.json"
        )
    with open(score_path) as f:
        train_test_info = json.load(f)
    if score_metric == 'accuracy':
        loaded_CV_test_score = train_test_info['test_accuracy'][cv_num]
    elif score_metric == 'f1':
        loaded_CV_test_score = train_test_info['test_f1'][cv_num]

    feature_names_path = os.path.join(
        cv_base_path, 
        model_name + '_all_CVs',
        model_name + '_feature_names' + '.txt'
        )
    with open(feature_names_path, 'r') as filehandle:
        feature_names = json.load(filehandle)

    return loaded_CV, loaded_CV_test_score, feature_names


def get_feature_importance(cv_base_path, model_name, classify, model):
    feature_coef_list = []
    test_score_list = []
    cv_score_list = []
    for cv_n in np.arange(11):
        loaded_CV, loaded_CV_test_score, feature_names  = load_CV(cv_base_path, model_name, cv_n, "accuracy") 
        if 'lr' in model_name:
            feature_coef_list.extend(abs(loaded_CV.best_estimator_['model'].coef_))
            classifier = "lr"
        elif 'rf' in model_name:
            feature_coef_list.append(loaded_CV.best_estimator_['model'].feature_importances_)   
            classifier = "rf" 
        test_score_list.append(loaded_CV_test_score)
        cv_score_list.append(loaded_CV.best_score_)

    coef_df = pd.DataFrame(
        data=feature_coef_list,
        columns=feature_names
    ).T

    coef_df['avg_coef'] = coef_df.mean(axis=1).to_numpy()

    # save values for the heatmap
    coef_avg = coef_df['avg_coef']
    collecting_dict = coef_avg.to_dict()
    
    collecting_dict["Model"] = model
    if "sub" in model:
        mode = "SKF"
    elif "LOO" in model:
        mode = "LOGO"
        print(mode)
 #   collecting_dict["mode"] = mode
    collecting_dict["classifier"] = classifier
    # avg_coefficients.append(collecting_dict)

    return collecting_dict


def plot_hyperparameters(cv_base_path, model_list):
    cv_num_max = 16
    best_params_list = []
    for model_name in model_list:
        for cv_n in np.arange(cv_num_max):
            loaded_CV, _, _ = load_CV(cv_base_path, model_name, cv_n, score_metric="accuracy")
            best_params_list.append(loaded_CV.best_params_)
        best_params_df = pd.DataFrame.from_dict(best_params_list)
    #     print(best_params_df)
        
        fig = plt.figure(figsize = (25, 5))
        j = 0
        for i in best_params_df.columns:
            plt.subplot(2, 6, j+1)
            j += 1
            if(best_params_df[i].dtype == np.float64 or best_params_df[i].dtype == np.int64):
                sns.boxplot(x=i, data=best_params_df)
            else:
                sns.countplot(x=i, data=best_params_df)
        fig.suptitle('Best estimator parameters for ' + model_name)
        fig.tight_layout()
        fig.subplots_adjust(top=0.95)
        plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from scipy import signal
from scipy.io import loadmat
import math
import seaborn as sns #sns.set(font_scale=1.2)
from scipy.integrate import simps
import nbimporter
import pickle
# Required Libraries are imported
import warnings  
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import VarianceThreshold
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from collections import Counter
import time
#import scikitplot as skplt
import itertools
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LeaveOneOut, LeaveOneGroupOut
from sklearn.preprocessing import StandardScaler
import mlxtend
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as metrics
from numpy import mean
from numpy import std
import os
import random
random.seed(9700)
warnings.filterwarnings('ignore')
from sklearn import svm
from scipy.stats import randint
import numpy as np
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv  # noqa
from sklearn.model_selection import HalvingRandomSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from classification_idyll_ml_personalised import make_pipeline, nested_cv, get_classification_scores, get_feature_importance, plot_classification_results




####### personalized model wild #####

base_path = ''
participant_id =  os.listdir(base_path)
participants_without_wild = ['UN_103', 'UN_120', 'UN_112' ]
participant_id = [id for id in participant_id if id not in participants_without_wild ]

model_name= [ 'lr_kfold', 'lr_skf']#, 'dt_kfold', 'dt_skf', ] #'svm_kfold', 'svm_skf',
for model in range (0, len(model_name)):
#         print(model_name[model])
    pipe_rf, grid_rf = make_pipeline(model_name[model])
    estimator = pipe_rf
    param_grid = grid_rf
    print_results=1
    save_results=1
    cv_base_path= cv_base_path= "/dhc/cold/groups/idyll/ML_results_universe/Wild/Nasa"
    print(cv_base_path)


    for id in range(0, len(participant_id)) : #len(participant_id)
        wild_per_task=[]
        feature_all =[]
        path_ = base_path + participant_id[id]+"/Wild/Features/"
        print(path_)
        tasks = [d for d in os.listdir(path_) if os.path.isdir(os.path.join(path_, d)) and d != '.DS_Store']
        print(tasks)
        if participant_id[id] == "UN_117":
            tasks = [ 'vlw_stress_hig_mw_12', 'vlw_stress_hig_mw_10', 'hig_stress_hig_mw_1', 'vlw_stress_nor_mw_11']
        if participant_id[id] == "UN_112":
            tasks = [ 'low_stress_low_mw_2', 'low_stress_low_mw_4']
        if participant_id[id] == "UN_105":
            tasks = ['vlw_stress_vlw_mw_1', 'vlw_stress_nor_mw_2', 
                     'vlw_stress_low_mw_5', 'low_stress_nor_mw_8', 'low_stress_hig_mw_9']
            
        Label = pd.read_csv(base_path + participant_id[id]+"/Wild/Task_Labels.csv")
        nasa_score = Label['Weighted Nasa Score']
        mean_nasa_score = Label['Weighted Nasa Score'].mean()
        mapping = dict(zip(Label["Labeled folder names"], Label["Weighted Nasa Score"]))
#         print(mapping)
        for task in tasks:
            print(task)
            path = path_ + task  
            print(path)
            files_to_load = {
                'eeg':  "EEG_features.pickle",
                'bvp': 'HRV_features.pickle',
                'eda': 'EDA_features.pickle',
                'temp': 'TEMP_features.pickle',    

                }

            df_all = {}  # Dictionary to store the loaded DataFrames

            for key, file_name in files_to_load.items():
                file_path = os.path.join(path, file_name)
                if os.path.exists(file_path):
                    df_all[key] = pd.read_pickle(file_path)
                else:
                    df_all[key] = None  # or your preferred default value
                    print(f"{file_name} not found in {path}")
            if all(df is not None for df in df_all.values()):
                features = pd.concat(df_all.values(), axis=1, join='inner')
                print("Concatenated DataFrame of all folders shape:", features.shape)
#                 feature_low.append(features)
            else:
                print("Not all required DataFrames are available for the task %s." %task)   

#             if task in mapping:
            nasa_score = mapping[task]
            print(f"Task: {task}, Corresponding nasa score: {nasa_score}")
            print(features.shape)
            print("mean", mean_nasa_score)
            print(nasa_score)
            if nasa_score > mean_nasa_score:
                features ["y"]= 1
                print("feature_high", features.shape)
            else:
                features ["y"]= 0
                print("features_low", features.shape)
#             print(feature_all)
            feature_all.append(features.copy())
#             print(feature_all)
#         print(len(feature_all))
        feature_wild = pd.concat(feature_all, axis=0, ignore_index= True)
#         print(feature_wild['y'].value_counts())
        print("total feature", feature_wild.shape)
        feature_wild = feature_wild.fillna(0)
        feat_high=  feature_wild.loc[feature_wild['y']==1]
        print("feature high", feat_high.shape)

        feat_low= feature_wild.loc[feature_wild['y']==0]
        print("feature low", feat_low.shape)

        y = feature_wild['y']
        X= feature_wild.drop(['y'],axis=1)
        print(X.shape)
        y_test, y_pred, train_test_info= nested_cv(X, y, model_name[model], estimator, param_grid, print_results, save_results, cv_base_path, participant_id[id])


# In[2]:


def combine_lab_data(path_main):
    tasks_easy= ['arithmetix_easy','n_back_easy','stroop_easy', 'sudoku_easy']
    tasks_hard= ['arithmetix_hard','n_back_hard', 'stroop_hard', 'sudoku_hard']
    feature_low= []
    feature_high=[]
    for i in range (0,len(tasks_easy)): 
        path = path_main +"/"+tasks_easy[i]
        print(path)
#         print("***********", tasks_easy[i])
        files_to_load = {
                'eeg':  "EEG_features.pickle",
                'bvp': 'HRV_features.pickle',
                'eda': 'EDA_features.pickle',
                'temp': 'TEMP_features.pickle',    

                }

        df_all = {}  # Dictionary to store the loaded DataFrames

        for key, file_name in files_to_load.items():
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                df_all[key] = pd.read_pickle(file_path)
            else:
                df_all[key] = None  # or your preferred default value
                print(f"{file_name} not found in {path}")
        if all(df is not None for df in df_all.values()):
            features = pd.concat(df_all.values(), axis=1, join='inner')
#             print("Concatenated DataFrame shape:", features.shape)
            feature_low.append(features)
        else:
            print("Not all required DataFrames are available for the task %s." %tasks_easy[i])           

    feature_low_all = pd.concat(feature_low, axis=0, ignore_index= True)
    feature_low_all ["y"]= 0
    print("feature_low_all", feature_low_all.shape)

    for i in range (0,len(tasks_hard)): #len(tasks)=10
        path= path_main +"/"+tasks_hard[i]
#         print("***********", tasks_hard[i])
#         print(path)
        files_to_load = {
                'eeg':  "EEG_features.pickle",
                'bvp': 'HRV_features.pickle',
                'eda': 'EDA_features.pickle',
                'temp': 'TEMP_features.pickle',    

                }

        df_all = {}  # Dictionary to store the loaded DataFrames

        for key, file_name in files_to_load.items():
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                df_all[key] = pd.read_pickle(file_path)
            else:
                df_all[key] = None  # or your preferred default value
                print(f"{file_name} not found in {path}")
        if all(df is not None for df in df_all.values()):
            features = pd.concat(df_all.values(), axis=1, join='inner')
#             print("Concatenated DataFrame shape:", features.shape)
            feature_high.append(features)
        else:
            print("Not all required DataFrames are available for the task %s." %tasks_hard[i]) 

    feature_high_all = pd.concat(feature_high, axis=0, ignore_index= True)
    feature_high_all ["y"]= 1
    print("feature_high_all", feature_high_all.shape)
    features_total=pd.concat([feature_low_all ,feature_high_all], axis=0, join="inner", ignore_index= True)
    print("features_lab",features_total.shape)

    return features_total


# In[4]:


####### personalized model lab #####

base_path = ''
participant_id =  os.listdir(base_path)
participants_with_one_lab = ["UN_120", "UN_112"]
participant_id = [id for id in participant_id if id not in participants_with_one_lab]

lab_session= ['Lab1', 'Lab2']

model_name=[   'lr_kfold']#, 'lr_skf', 'dt_kfold', 'dt_skf', ] #'svm_kfold', 'svm_skf',
for model in range (0,len(model_name)):
    print(model_name[model])
    pipe_rf, grid_rf = make_pipeline(model_name[model])
    estimator = pipe_rf
    param_grid = grid_rf
    print_results=1
    save_results=1
    cv_base_path= ""
    print(cv_base_path)
    lab_all=[]
    count_subject= 0    
    for id in range(0, len(participant_id)) : #len(participant_id)
        both_lab_features = []
        if participant_id[id] in participants_with_one_lab:
            lab_range = [0]
        else:
            lab_range = range(0, 2)    
        print(lab_range)
        
        for lab in lab_range :   
            print("*******************************participant id***************************", participant_id[id])
            print(lab)
            print(id)
            path = base_path + participant_id[id]+"/"+lab_session[lab]+"/Features/"
            print(path)
            features= combine_lab_data(path)              
            both_lab_features.append(features)
        lab_feat = pd.concat(both_lab_features, axis=0, ignore_index=True)

        print("lab_feat", lab_feat.shape)
        y = lab_feat['y']

        X= lab_feat.drop(['y'],axis=1)
        y_test, y_pred, train_test_info= nested_cv(X, y, model_name[model], estimator, param_grid, print_results, save_results, cv_base_path, participant_id[id])


# In[ ]:





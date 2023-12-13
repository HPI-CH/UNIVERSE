import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, iirnotch, filtfilt
import scipy
import math
from mne.io.fiff import raw
import pandas as pd
import mne
import datetime
from sklearn.decomposition import FastICA, PCA
from pypg.plots import simple_plot
import os
from datetime import timedelta, datetime

figure_path= "/dhc/cold/groups/idyll/TEMPORARY_DATA_MANIPULATION/(xtracted_figure)"

def interpolate_rows(dataframe, show= False):
    df = dataframe.copy(deep=True)
    interpolation_method = 'linear'  # nearest, linear, zero 

    for i in dataframe.columns:
        df.loc[df[i] == 0, i] = np.NaN
        df[i] = pd.to_numeric(df[i])
        df[i] = df[i].interpolate(method=interpolation_method)
        df[i] = df[i].fillna(method='backfill') #fill na fields at the start (that were not interpolated with the previous method)

    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("Original df:")
        df.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()

    return df


# def drop_na_eeg(dataframe, columns_of_interest):
#     df = dataframe.copy(deep=True)
#     for i in columns_of_interest:
#         df.loc[df[i] == 0, i] = np.NaN

#     df = df.dropna(axis=0, how='any')#, subset=columns_of_interest)

#     return df

def acc_all_tasks_lab (base_path, participant_id, session, tasks):
    df_acc_tasks =[]
    for i in range (0,len(tasks)): 
        path = base_path + participant_id+"/"+session+"/Labeled/"+tasks[i]
#         print(path)
        columns = ['ACC_X_MUSE', 'ACC_Y_MUSE', 'ACC_Z_MUSE'] # lab data
        files_to_load = {
                'acc_x': 'muse_ACC_X.pickle',
                'acc_y': 'muse_ACC_Y.pickle',
                'acc_z': 'muse_ACC_Z.pickle', 
                        }

        dataframes = {}  # Dictionary to store the loaded DataFrames

        for key, file_name in files_to_load.items():
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                dataframes[key] = pd.read_pickle(file_path)
#                 print(f"{file_name} found in {path}")
            else:
                dataframes[key] = None  # or your preferred default value
                print(f"{file_name} not found in {path}")
        
#         print(dataframes['acc_x'])
#         print(dataframes['acc_y'])
#         print(dataframes['acc_z'])
        if dataframes['acc_x'] is not None:
#             print("NOT NAN")
            df_acc = pd.DataFrame(columns=columns)

            df_acc = pd.concat([dataframes['acc_x'], dataframes['acc_y'], dataframes['acc_z']], axis=1)
            df = df_acc.reset_index()
            df= interpolate_rows(df)
            

            for col in ['index', 'TimeStamp']:
                if col in df.columns:
                    del df[col] 
#             print(df)
            normalizeFactor = 256 / 2 #sf should have been 50 Hz but actually 256 Hz saved 
            sos1, sos3 = butter(N=6, Wn=(20 / normalizeFactor), btype="lowpass", analog=False) # N: order, HP: 20 Hz, LP:0.5 Hz
            sos2, sos4 = butter(N=6, Wn=(0.5 / normalizeFactor), btype="high", analog=False)
            
            for column in columns:
#                 print(df[column].shape)
                df[column] = filtfilt(sos1, sos3, df[column])
                df[column] = filtfilt(sos2, sos4, df[column]) * 9.80665 #meter per second square unit
        #     print(tasks[i])
            df_acc_tasks.append(df)
        #     print(df_acc_tasks)
        acc_all = pd.concat(df_acc_tasks, axis=0)
        acc_mag= np.sqrt(acc_all["ACC_X_MUSE"] ** 2 + acc_all["ACC_Y_MUSE"] ** 2 + acc_all["ACC_Z_MUSE"] ** 2)
    
    return acc_mag

def acc_all_tasks_wild (base_path, participant_id):
    
#     tasks_wild = os.listdir(base_path + participant_id+"/Wild/Labeled/")

    path = os.path.join(base_path, participant_id, "Wild", "Labeled")
    tasks_wild = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d != '.DS_Store']
    print(tasks_wild)
    
    df_acc_tasks =[]
    for i in range (0,len(tasks_wild)): 
        path = base_path + participant_id+"/Wild/Labeled/"+tasks_wild[i]
#         print(path)
        columns = ['Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z']  # lab data
        
        files_to_load = {
                'acc_x': 'muse_ACC_X.pickle',
                'acc_y': 'muse_ACC_Y.pickle',
                'acc_z': 'muse_ACC_Z.pickle', 
                        }

        dataframes = {}  # Dictionary to store the loaded DataFrames

        for key, file_name in files_to_load.items():
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                dataframes[key] = pd.read_pickle(file_path)
            else:
                dataframes[key] = None  # or your preferred default value
                print(f"{file_name} not found in {path}")
#         print(dataframes['acc_x'])
        if dataframes['acc_x'] is not None:
#             print("NOT NAN")
            df_acc = pd.DataFrame(columns=columns)

            df_acc = pd.concat([dataframes['acc_x'], dataframes['acc_y'], dataframes['acc_z']], axis=1)
            df = df_acc.reset_index()
            df= interpolate_rows(df)

            for col in ['index', 'TimeStamp']:
                if col in df.columns:
                    del df[col] 
#             print("df shape before concatenation", df.shape)
            normalizeFactor = 256 / 2 #sf should have been 50 Hz but actually 256 Hz saved 
            sos1, sos3 = butter(N=6, Wn=(20 / normalizeFactor), btype="lowpass", analog=False) # N: order, HP: 20 Hz, LP:0.5 Hz
            sos2, sos4 = butter(N=6, Wn=(0.5 / normalizeFactor), btype="high", analog=False)

            for column in columns:
                df[column] = filtfilt(sos1, sos3, df[column])
                df[column] = filtfilt(sos2, sos4, df[column]) * 9.80665 #meter per second square unit
            df_acc_tasks.append(df)
        if df_acc_tasks:
            acc_all = pd.concat(df_acc_tasks, axis=0)
#             print("df shape after concatenation", acc_all.shape)
            acc_mag= np.sqrt(acc_all["Accelerometer_X"] ** 2 + acc_all["Accelerometer_Y"] ** 2 + acc_all["Accelerometer_Z"] ** 2)

    return acc_mag, tasks_wild

def remove_high_acc(df_eeg, column_names,path, threshold, show= True):
    """Takes a pandas Dataframe and a threshold and removes every row from the dataset with a higher total
    acceleration than the treshold."""
    column_names = ["RAW_TP9","RAW_TP10","RAW_AF7","RAW_AF8"]
    print("checking if the threshold is consistent", threshold)
    # get acc array 
     
    print("accelerometer data for the lab or wild")
    path_split = path.split('/') 
    if "Wild" in path_split:
        columns = ['Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z']
    else:
        columns = ['ACC_X_MUSE', 'ACC_Y_MUSE', 'ACC_Z_MUSE'] ##lab
    acc_x = pd.read_pickle(f"{path}"+"/muse_ACC_X.pickle") ### file names are different in wild and lab
    acc_y = pd.read_pickle(f"{path}"+"/muse_ACC_Y.pickle")
    acc_z = pd.read_pickle(f"{path}"+"/muse_ACC_Z.pickle")


    df_acc = pd.DataFrame(columns = columns)
    df_acc = pd.concat([acc_x,acc_y, acc_z],axis=1)

    df_acc = df_acc.reset_index()
    if "Wild" in path_split:
        del df_acc['TimeStamp'] ## wild
    else:
        del df_acc['index'] ## lab

    df = pd.concat([df_eeg,df_acc],axis=1)
    print("before accelerometer filter", df_eeg.shape)
    
    normalizeFactor = 256 / 2 #sf 50 Hz
    sos1, sos3 = butter(N=6, Wn=(20 / normalizeFactor), btype="lowpass", analog=False) # N: order, HP: 20 Hz, LP:0.5 Hz
    sos2, sos4 = butter(N=6, Wn=(0.5 / normalizeFactor), btype="high", analog=False)
    
    for column in columns:
        df[column] = filtfilt(sos1, sos3, df[column])
        df[column] = filtfilt(sos2, sos4, df[column]) * 9.80665 #meter per second square unit

        
        x = df.loc[np.sqrt(df[columns] ** 2).sum(axis=1) > threshold].index
        acc= np.sqrt(df[columns] ** 2).sum(axis=1)
    for idx in x:
        if idx in df_eeg.index:   
            df_eeg.loc[idx, column_names] = np.nan
    df_eeg.fillna(method='ffill', inplace=True)  # Forward fill
    df_eeg.fillna(method='bfill', inplace=True)  # Backward fill
    mask = df_eeg.index.isin(x)
# Apply interpolation only to the selected rows
    df_eeg.loc[mask] = df_eeg.loc[mask].interpolate(method='linear')
#     df_eeg = df_eeg.interpolate(method='linear')
#     print("after accelerometer filter", df_eeg).
    has_nan = df_eeg.isna().any().any()
    print("Are there any NaN values in the DataFrame????????? ", has_nan)
    total_nan = df_eeg.isna().sum().sum()
    print("**********************Total number of NaN values in the DataFrame: ", total_nan)

    if show== True:
        simple_plot(df["RAW_TP9"], title='Original EEG Signal', label='raw_TP9', figure_path=figure_path)
        simple_plot(df_eeg["RAW_TP9"], title='Filtered EEG Signal', label='movement filter', figure_path=figure_path)
        simple_plot(acc, title='Acceleration Magnitude (m/s2)', label='acceleration mag', figure_path=figure_path)
        plt.show()

    return df_eeg

def find_threshold(acc_mag):

    threshold_found = False
    upper_bound = max(acc_mag)
    lower_bound = 0

    threshold_value = (upper_bound - lower_bound) / 2

    higher_percentage_threshold = 5.25
    lower_percentage_threshold = 3

    percentage_dropped = -99

    ctr = 0

    def percentage_in_range(percentage, lower, upper):
        return (percentage < upper) and (percentage > lower)

    while not threshold_found and ctr <= 20:

        if percentage_in_range(percentage_dropped, lower_percentage_threshold, higher_percentage_threshold):
            threshold_found = True
            print('Found a threshold value! Use %f to achieve %f of interpolation!' % (threshold_value, percentage_dropped))
            # Don't do anything more, we've found an acceptable threshold value
        else:
            x=np.where(np.logical_and(acc_mag>=0, acc_mag<=threshold_value))[0]
            percentage_dropped = (len(acc_mag)- x.shape[0])/len(acc_mag) * 100            
            print('Dropped %.2f for %f' % (percentage_dropped, threshold_value))

            if percentage_dropped > higher_percentage_threshold:
                threshold_value += (upper_bound - lower_bound) / 2
                upper_bound = threshold_value
            elif percentage_dropped < lower_percentage_threshold:
                threshold_value -= (upper_bound - lower_bound) / 2
                lower_bound = threshold_value

        ctr+=1
        if threshold_found:
            break
    return threshold_value

def prefilter(Df,sf_eeg, show= False):
    raw_data = Df[["RAW_TP9", "RAW_TP10", "RAW_AF7", "RAW_AF8"]]
    raw_data = raw_data.to_numpy()
    before_data = raw_data
    raw_data = raw_data.T
    low_freq, highFreq = 0.5, 50
    filtered_data = mne.filter.filter_data(raw_data, sf_eeg, low_freq, highFreq, verbose= False)
    print("Done EEG Filtering!")
    Df[["RAW_TP9", "RAW_TP10", "RAW_AF7", "RAW_AF8"]] = filtered_data.T
    
    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("BP filter 0.5-50:")
        Df.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()
    return Df

def notch(df, sf_eeg, f0, Q):
    b, a = iirnotch(f0, Q, fs=sf_eeg)
    df_notch = df.apply(lambda col: filtfilt(b,a, col), axis=0)
    return df_notch
    
# def ICA_PCA(df):  ## not used so far
#     # Compute PCA
#     pca = PCA(n_components=4)
#     H = pca.fit_transform(df)
#     # Compute ICA
#     ica = FastICA(n_components=4)
#     S_ = ica.fit_transform(df)  # Reconstruct signals
#     A_ = ica.mixing_  # Get estimated mixing matrix,
#     df_ica=pd.DataFrame(S_)
#     df_pca=pd.DataFrame(H)
#     return(df_ica, df_pca)

def average_reference(df_eeg, show= False): #
    columns = [ "RAW_TP9", "RAW_TP10", "RAW_AF7", "RAW_AF8"] 
    df_avg= df_eeg[columns]
    df_avg = df_avg.sub(df_avg.mean(axis=1), axis=0)
    
    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("Average referencing:")
        df_avg.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()
    return df_avg

def normalize_wild(df, show= False):
    
    columns = ["RAW_TP9", "RAW_TP10", "RAW_AF7", "RAW_AF8"]
    
    for column in columns:
#         df[column] = df[column] - np.nanmean(df_closed_eyes[column].to_list())
        min_value = df[column].min()
        max_value = df[column].max()
        df[column] = (df[column] - min_value) / (max_value - min_value)
        
    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("min max normalization:")
        df.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()
    return df

def normalize(df, df_closed_eyes, show= False):
    
    columns = ["RAW_TP9", "RAW_TP10", "RAW_AF7", "RAW_AF8"]
    
    for column in columns:
        df[column] = df[column] - np.nanmean(df_closed_eyes[column].to_list())
        min_value = df[column].min()
        max_value = df[column].max()
        df[column] = (df[column] - min_value) / (max_value - min_value)
        
    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("eyeclosing and min max normalization:")
        df.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()
    return df

def add_miliseconds_muse(muse_data):
    # muse_data = muse_data[990:999]
    if type(muse_data) == str:
        df = pd.read_csv(muse_data)
        # df = pd.read_csv(muse_data, parse_dates=['TimeStamp'], index_col='TimeStamp') #intentar esto
    elif type(muse_data):
        df = muse_data.copy(deep=True)
    else:
        return None

    df = df.sort_index(
        ascending=True)  # to sort rows by index (since some time index are between other values maybe because muse had package loss or delay in streaming)
    list_timestamp_indexes = df.index.tolist()  # get list of df indexes
    # print(F"DEBUG: {list_timestamp_indexes}")
    duplicate_index_list = []  # add only the duplicate (not the original)
    max_duplicates_at_once = 0
    for i in range(len(list_timestamp_indexes)):
        if i == len(list_timestamp_indexes) - 1:
            break
        if list_timestamp_indexes[i] == list_timestamp_indexes[i + 1]:
            duplicate_index_list = []
            keep_looking = True
            temp_i = i
            while keep_looking:
                if temp_i == len(list_timestamp_indexes) - 1:
                    break
                if list_timestamp_indexes[temp_i] == list_timestamp_indexes[temp_i + 1]:
                    duplicate_index_list.append(temp_i + 1)
                    temp_i = temp_i + 1
                else:
                    keep_looking = False
            for j in range(len(duplicate_index_list)):  # go through duplicate_index_list and change them
                # print(F"DEBUG NOW: {list_timestamp_indexes[duplicate_index_list[j]]}, {duplicate_index_list[j]}")
                list_timestamp_indexes[duplicate_index_list[j]] = list_timestamp_indexes[
                                                                      duplicate_index_list[j]] + timedelta(
                    microseconds=j + 7)  # add one microsecond to each timestamp, so they are all different
                # print(F"DEBUG NOW: {list_timestamp_indexes[duplicate_index_list[j]]}, {duplicate_index_list[j]}")
        max_duplicates_at_once = len(duplicate_index_list) if len(
            duplicate_index_list) > max_duplicates_at_once else max_duplicates_at_once
    df.index = list_timestamp_indexes  # assign list as df indexes
    if len(df[df.index.duplicated(
            keep="first")]) > 0:  # if there are still duplicates, remove them (although there should not be any since indexes are ordered at the start)
        df = df[~df.index.duplicated(
            keep="first")]  # ~ is bitwise negation, which we use to invert the boolean arrays of results from df.index.duplicated(keep="first")
    df.index.name = 'TimeStamp'
    # print("Duplicates:")
    # print(df[df.index.duplicated(keep=False)])
    # print(F"DEBUG: {list_timestamp_indexes}")
    # print(F"DEBUG [max_duplicates_at_once]: {max_duplicates_at_once}")
#     df.to_csv(save_path)
    return df

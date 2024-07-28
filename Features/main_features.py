
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import neurokit2 as nk
from scipy.signal import butter, lfilter, savgol_filter, find_peaks
from numpy.lib.stride_tricks import as_strided
import pickle
import os
import random
random.seed(9700)
import warnings 
warnings.filterwarnings('ignore')
from scipy.signal import resample
import matplotlib.pyplot as plt




from features import windowed_view, power_features, add_more_power_features, add_new_features

                               ########### wild data ##############


if __name__ == '__main__':
    print()
    
########### wild data ##############
    base_path = ''
    participant_id =  os.listdir(base_path)

    eeg_columns=['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']
    # hr_filters = ['Raw','butterfy', 'chebyfy',  'waveletfy', 'savgol', 'rls_wav_sav', 'nk', 'biosspy']
    sf_eeg = 256
    sf_ppg = 64 #sampling_frequency
    sf_eda = 4
    window = 60 # in seconds 
    overlap_percent = 80
    bands=[(0.5, 4, 'Delta'), (4, 7, 'Theta'), (8, 12, 'Alpha'), (12, 30, 'Beta'), (30, 50, 'Gamma')]

    df = pd.DataFrame(columns = eeg_columns)

    for id in range(0, len(participant_id) ) : #len(participant_id)                        
        if (participant_id[id] == 'UN_103') or (participant_id[id] == 'UN_120')or (participant_id[id] == 'UN_112'):
            print( "Duration wild:", "no wild data")
        else:
            print("participant id %s " %participant_id[id])
        #             print(tasks)
            copy_folder_names = (base_path + participant_id[id]+"/Wild/Preprocessed/")
            tasks = [d for d in os.listdir(copy_folder_names) if os.path.isdir(os.path.join(copy_folder_names, d)) and not d.startswith("eye-closing")]
            print(tasks)
        ### Lab data loading ###        
            for i in range (0,len(tasks)): 
                path = base_path +participant_id[id]+"/Wild/Preprocessed"+"/"+tasks[i]
                print(path)
                path_save= base_path +participant_id[id]+"/Wild/Features"+"/"+tasks[i]
                files_to_load = {
                                'eeg':  "EEG_filtered.pickle",
                                'bvp': 'BVP_filtered.pickle',
                                'eda': 'EDA_filtered.pickle',
                                'temp': 'TEMP_filtered.pickle',    

                                }

                df_all = {}  # Dictionary to store the loaded DataFrames

                for key, file_name in files_to_load.items():
                    file_path = os.path.join(path, file_name)
                    if os.path.exists(file_path):
                        df_all[key] = pd.read_pickle(file_path)
                    else:
                        df_all[key] = None  # or your preferred default value
                        print(f"{file_name} not found in {path}")



                print(path)


            ################## EEG features 
                if df_all["eeg"] is not None:
                    eeg= df_all["eeg"]
                    eeg= eeg [eeg_columns]
#                     print(eeg)
                    length = len(eeg)-sf_eeg*10*60        
#                     if length > 0:
#                         eeg.drop(eeg.tail((len(eeg)-sf_eeg*10*60)).index,inplace=True)


                    df=eeg.to_numpy()
                    window_size = window * sf_eeg
                    overlap = int((window_size * overlap_percent)/100)

                    df_TP9 = windowed_view(df[:, 0], window_size, overlap) 
                    df_AF7 = windowed_view(df[:, 1], window_size, overlap)
                    df_AF8 = windowed_view(df[:, 2], window_size, overlap) 
                    df_TP10 = windowed_view(df[:, 3], window_size, overlap)
                    df_arr = np.stack([df_TP9, df_AF7, df_AF8, df_TP10], axis=1) 

                    current_df=power_features(df_arr, sf_eeg, window_size, overlap, bands) 
                    df_feature= add_more_power_features(current_df)
                    df_feature= add_new_features(df_feature)
                    columns=['mean_δ', 'mean_θ', 'mean_α', 'mean_β', 'mean_γ', 'α/θ', 'θ/α', 
                             'frontal_α_asy', 'δ_asy', 'θ_asy', 'α_asy', 'β_asy', 'γ_asy']
                    df=df_feature[columns]
                    print("EEG Features", df)
                    df.to_pickle(f"{path_save}"+"/EEG_features.pickle")
                    print("saved EEG features for task", tasks[i])
                else:
                    print("no df found and EEG featured not saved for task", tasks[i])
#    
#                             #### BVP features ##### 

                
                if df_all["bvp"] is not None:
#                     print(df_all["bvp"])   
                    ppg_clean= df_all["bvp"]
                    print(len(ppg_clean))
#                     length = len(ppg_clean)-sf_ppg*10*60

#                     if length > 0:
#                         ppg_clean= ppg_clean[:-length]
                    print(len(ppg_clean))
                    ppg_clean= ppg_clean["savgol_filter_ppg"].to_numpy(copy=True)
                    window_size = window * sf_ppg
                    overlap = int((window_size * overlap_percent)/100)
#                     print(window_size)
                    ppg_win = windowed_view(ppg_clean, window_size, overlap) 
                    print_count = 0
                    hrv_param=[]
                    for windows in range (0, ppg_win.shape[0]): #(0, ppg_win.shape[0]):  
#                         print(windows)
#                         print(ppg_win[windows])
                        info = nk.ppg_findpeaks(ppg_win[windows], sampling_rate=64, show=False)### from neurokit2
#                         print(info["PPG_Peaks"])
                        if 0 <= len(info['PPG_Peaks']) <= 3:
#                             hrv_param = [0, 0, 0, 0, 0, 0]
                            nan_hrv_features = pd.DataFrame(np.nan, index=[0], columns=['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_LFn', 'HRV_HFn', 'HRV_ratio_LFn_HFn'])
                            hrv_param.append(nan_hrv_features)
                            print("less than 3 peaks found")
                            print_count += 1
                        else:
                            hrv_time = nk.hrv_time(info, sampling_rate=sf_ppg, show=False) #time domain
                            hrv_time = hrv_time[['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD']]
                            hrv_freq = nk.hrv_frequency(info, sampling_rate=sf_ppg, show= False, normalize=True) #freq domain
                            hrv_freq = hrv_freq[['HRV_LFn', 'HRV_HFn']]
                            hrv_freq ["HRV_ratio_LFn_HFn"] = hrv_freq ["HRV_LFn"].div(hrv_freq ["HRV_HFn"].values)
                            hrv_features=pd.concat([hrv_time , hrv_freq], axis=1, join="inner")
                            hrv_param.append(hrv_features)               
                    hrv_all = pd.concat(hrv_param, axis=0, ignore_index= True)
                    hrv_all.interpolate(method= "backfill", inplace=True)
                    hrv_all.interpolate(method= "ffill", inplace=True)
                    print("hrv_param", hrv_all)
                    print("***************The print command was executed", print_count, "times.")
                    
                    if window==30:
                        hrv_all = hrv_all [['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_HFn']] 
                    else:
                        hrv_all = hrv_all [['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_LFn', 'HRV_HFn','HRV_ratio_LFn_HFn']]
#                     print("hrv_all", hrv_all)
                    filepath= f"{path_save}"+"/HRV_features.pickle"
                    pickle.dump(hrv_all, open(filepath, 'wb'))
#                     print("HRV features for task", tasks[i])

                                #### EDA features ##### 
                eda_param=[]
#                 print(lab_session[lab])    

                if df_all["eda"] is not None :
#                     print("something")
                    df_eda = df_all["eda"]
                    eda_resampled = resample(df_eda, len(df_eda)*2)
                    resampled_sf = sf_eda*2
                    window_size = window * resampled_sf
                    overlap = int((window_size * overlap_percent)/100)
                    eda_win = windowed_view(eda_resampled, window_size, overlap) 
                    print("window_shape_eda", eda_win.shape[0])
                    
                    for windows in range (0, eda_win.shape[0]):
#                         print(windows)
                        processed_gsr = nk.eda_process(eda_win[windows], resampled_sf)[0]

                        scr_features = nk.eda_analyze(processed_gsr, sampling_rate=resampled_sf, method='interval-related')
                        eda_param.append(scr_features)
                    eda_all = pd.concat(eda_param, axis=0, ignore_index= True)
                    print("EDA Features", eda_all.head(10))

                    filepath= f"{path_save}"+"/EDA_features.pickle"
                    pickle.dump(eda_all, open(filepath, 'wb'))

                           #### TEMP features #####        
                features_all=[]
                if df_all["temp"] is not None:
                    df_temp = df_all["temp"]
                    
                    window_size = window * sf_eda
                    overlap = int((window_size * overlap_percent)/100)
                    temp_win = windowed_view(df_temp, window_size, overlap) 
                    
                    for windows in range (0, temp_win.shape[0]):
                        mean_absolute_values = temp_win[windows].mean()
                        std = temp_win[windows].std()                       
                        features = np.array([mean_absolute_values, std])
                        features_all.append(features)            
                    temp_all = np.stack((features_all), axis=1)
                    temp_all=pd.DataFrame(temp_all.T, columns=["mean_temp","std_temp"])
                    filepath= f"{path_save}"+"/TEMP_features.pickle"
                    pickle.dump(temp_all, open(filepath, 'wb'))

                    print("temp shape", temp_all.shape)
                    
                features= pd.concat([df, hrv_all, eda_all, temp_all], axis=1, join="inner")
                print("all features",features.head(10))


########### lab data ##############


if __name__ == '__main__':
    print()
    
    base_path = ''
    participant_id =  os.listdir(base_path)
    participants_with_one_lab = ["UN_120", "UN_112"]
    lab_session= ['Lab1', 'Lab2']
    
    tasks= ['relaxation_video','arithmetix_easy','n_back_easy','stroop_easy', 'sudoku_easy',
                                                'arithmetix_hard','n_back_hard', 'stroop_hard', 'sudoku_hard']

    eeg_columns=['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']
    # hr_filters = ['Raw','butterfy', 'chebyfy',  'waveletfy', 'savgol', 'rls_wav_sav', 'nk', 'biosspy']
    sf_eeg = 256
    sf_ppg = 64 #sampling_frequency
    sf_eda = 4
    window = 60 # in seconds 
    overlap_percent = 80
    bands=[(0.5, 4, 'Delta'), (4, 7, 'Theta'), (8, 12, 'Alpha'), (12, 30, 'Beta'), (30, 50, 'Gamma')]
    df = pd.DataFrame(columns = eeg_columns)
    
    for id in range(0, len(participant_id)) : #len(participant_id)
        if id in participants_with_one_lab:
            lab_range = [0]
        else:
            lab_range = range(0, 2)
        for lab in lab_range:   
            print("*******************************participant id***************************", participant_id[id])
            print(lab_session[lab])
            print(id)

        ### Lab data loading ###        
            for i in range (0, len(tasks)): 
                path = base_path +participant_id[id]+"/"+lab_session[lab]+"/Preprocessed"+"/"+tasks[i]
                path_save= base_path +participant_id[id]+"/"+lab_session[lab]+"/Features"+"/"+tasks[i]
                files_to_load = {
                                'eeg':  "EEG_filtered.pickle",
                                'bvp': 'BVP_filtered.pickle',
                                'eda': 'EDA_filtered.pickle',
                                'temp': 'TEMP_filtered.pickle',    

                                }

                df_all = {}  # Dictionary to store the loaded DataFrames

                for key, file_name in files_to_load.items():
                    file_path = os.path.join(path, file_name)
                    if os.path.exists(file_path):
                        df_all[key] = pd.read_pickle(file_path)
                    else:
                        df_all[key] = None  # or your preferred default value
                        print(f"{file_name} not found in {path}")


                print(path)


            ################## EEG features 
                if df_all["eeg"] is not None:
                    eeg= df_all["eeg"]
                    eeg= eeg [eeg_columns]
#                     print(eeg)
                    length = len(eeg)-sf_eeg*10*60        
                    if length > 0:
                        eeg.drop(eeg.tail((len(eeg)-sf_eeg*10*60)).index,inplace=True)


                    df=eeg.to_numpy()
                    window_size = window * sf_eeg
                    overlap = int((window_size * overlap_percent)/100)

                    df_TP9 = windowed_view(df[:, 0], window_size, overlap) 
                    df_AF7 = windowed_view(df[:, 1], window_size, overlap)
                    df_AF8 = windowed_view(df[:, 2], window_size, overlap) 
                    df_TP10 = windowed_view(df[:, 3], window_size, overlap)
                    df_arr = np.stack([df_TP9, df_AF7, df_AF8, df_TP10], axis=1) 

                    current_df=power_features(df_arr, sf_eeg, window_size, overlap, bands) 
                    df_feature= add_more_power_features(current_df)
                    df_feature= add_new_features(df_feature)
                    columns=['mean_δ', 'mean_θ', 'mean_α', 'mean_β', 'mean_γ', 'α/θ', 'θ/α', 
                             'frontal_α_asy', 'δ_asy', 'θ_asy', 'α_asy', 'β_asy', 'γ_asy']
                    df=df_feature[columns]
                    print("EEG Features", df.shape)
                    df.to_pickle(f"{path_save}"+"/EEG_features.pickle")
                    print("saved EEG features for task", tasks[i])
                else:
                    print("no df found and EEG featured not saved for task", tasks[i])
#                 df.to_pickle(f"{path_save}"+"/EEG_features_win_"+ str(window) +".pickle")

#                             #### BVP features ##### 

                
                if df_all["bvp"] is not None:
#                     print(df_all["bvp"])   
                    ppg_clean= df_all["bvp"]
                    print(len(ppg_clean))
                    length = len(ppg_clean)-sf_ppg*10*60

                    if length > 0:
                        ppg_clean= ppg_clean[:-length]
                    print(len(ppg_clean))
                    ppg_clean= ppg_clean["savgol_filter_ppg"].to_numpy(copy=True)
                    window_size = window * sf_ppg
                    overlap = int((window_size * overlap_percent)/100)
#                     print(window_size)
                    ppg_win = windowed_view(ppg_clean, window_size, overlap) 
                    
                    hrv_param=[]
                    for windows in range (0, ppg_win.shape[0]): #(0, ppg_win.shape[0]):  
#                         print(windows)
#                         print(ppg_win[windows])
                        info = nk.ppg_findpeaks(ppg_win[windows], sampling_rate=64, show=False)### from neurokit2
#                         print(info["PPG_Peaks"])
                        if 0 <= len(info['PPG_Peaks']) <= 3:
#                             hrv_param = [0, 0, 0, 0, 0, 0]
                            nan_hrv_features = pd.DataFrame(np.nan, index=[0], columns=['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_LFn', 'HRV_HFn', 'HRV_ratio_LFn_HFn'])
                            hrv_param.append(nan_hrv_features)
                            print("less than 3 peaks found")
                        else:
                            hrv_time = nk.hrv_time(info, sampling_rate=sf_ppg, show=False) #time domain
                            hrv_time = hrv_time[['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD']]
                            hrv_freq = nk.hrv_frequency(info, sampling_rate=sf_ppg, show= False, normalize=True) #freq domain
                            hrv_freq = hrv_freq[['HRV_LFn', 'HRV_HFn']]
                            hrv_freq ["HRV_ratio_LFn_HFn"] = hrv_freq ["HRV_LFn"].div(hrv_freq ["HRV_HFn"].values)
                            hrv_features=pd.concat([hrv_time , hrv_freq], axis=1, join="inner")
                            hrv_param.append(hrv_features)               
                    hrv_all = pd.concat(hrv_param, axis=0, ignore_index= True)
                    hrv_all.interpolate(inplace=True)
                    print("hrv_param", hrv_all.shape)
                    
                    if window==30:
                        hrv_all = hrv_all [['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_HFn']] 
                    else:
                        hrv_all = hrv_all [['HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_LFn', 'HRV_HFn','HRV_ratio_LFn_HFn']]
#                     print("hrv_all", hrv_all)
                    filepath= f"{path_save}"+"/HRV_features.pickle"
                    pickle.dump(hrv_all, open(filepath, 'wb'))
#                     print("HRV features for task", tasks[i])

                                #### EDA features ##### 
                eda_param=[]
#                 print(lab_session[lab])    

                if df_all["eda"] is not None :
#                     print("something")
                    df_eda = df_all["eda"]
                    eda_resampled = resample(df_eda, len(df_eda)*2)
                    resampled_sf = sf_eda*2
                    window_size = window * resampled_sf
                    overlap = int((window_size * overlap_percent)/100)
                    eda_win = windowed_view(eda_resampled, window_size, overlap) 
                    print("window_shape_eda", eda_win.shape[0])
                    
                    for windows in range (0, eda_win.shape[0]):
#                         print(windows)
                        processed_gsr = nk.eda_process(eda_win[windows], resampled_sf)[0]

                        scr_features = nk.eda_analyze(processed_gsr, sampling_rate=resampled_sf, method='interval-related')
                        eda_param.append(scr_features)
                    eda_all = pd.concat(eda_param, axis=0, ignore_index= True)
                    print("EDA Features", eda_all.head(10))

                    filepath= f"{path_save}"+"/EDA_features.pickle"
                    pickle.dump(eda_all, open(filepath, 'wb'))

                           #### TEMP features #####        
                features_all=[]
                if df_all["temp"] is not None:
                    df_temp = df_all["temp"]
                    
                    window_size = window * sf_eda
                    overlap = int((window_size * overlap_percent)/100)
                    temp_win = windowed_view(df_temp, window_size, overlap) 
                    
                    for windows in range (0, temp_win.shape[0]):
                        mean_absolute_values = temp_win[windows].mean()
                        std = temp_win[windows].std()                       
                        features = np.array([mean_absolute_values, std])
                        features_all.append(features)            
                    temp_all = np.stack((features_all), axis=1)
                    temp_all=pd.DataFrame(temp_all.T, columns=["mean_temp","std_temp"])
                    filepath= f"{path_save}"+"/TEMP_features.pickle"
                    pickle.dump(temp_all, open(filepath, 'wb'))

                    print("temp shape", temp_all.shape)
                    
                features= pd.concat([df, hrv_all, eda_all, temp_all], axis=1, join="inner")
                print("all features",features.head(10))
#                 filepath= f"{path_save}"+"/Features_All.pickle"
#                 pickle.dump(features, open(filepath, 'wb'))


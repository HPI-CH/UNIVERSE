
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
import statistics

from eeg_filters import add_miliseconds_muse, acc_all_tasks_wild, acc_all_tasks_lab, interpolate_rows, find_threshold, remove_high_acc, prefilter, average_reference, normalize, prefilter, notch, normalize_wild

from ppg_filters import  plot_filters, normalize_ppg, normalize_ppg_wild, calculating_hr, simple_plot, ppg_savgol_filter,interpolate_missing_values_nan 



########### lab data preprocessing ###################



if __name__ == '__main__':
    print()
    
    base_path = ''
    participant_id =  os.listdir(base_path) 
    lab_session= ['Lab1', 'Lab2']
    
    tasks= ['eye_closing', 'relaxation_video','arithmetix_easy','n_back_easy','stroop_easy', 'sudoku_easy',
                                                'arithmetix_hard','n_back_hard', 'stroop_hard', 'sudoku_hard']
    eeg_columns=['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']
    
    #sampling_frequency
    sf_eeg = 256
    sf_eda=4
    cutoff_frequencies = [0.5, 10]
    sf_ppg = 64

    df = pd.DataFrame(columns = eeg_columns)
    
    for id in range(0, len(participant_id)) : #len(participant_id)
        for lab in range (0,2):   
            print(participant_id[id])
            print(lab_session[lab])
            acc_mag = acc_all_tasks_lab(base_path, participant_id[id], lab_session[lab], tasks)
            threshold= find_threshold(acc_mag)
            print("threshold", threshold)

        ### Lab data loading ###        
            for i in range (0,len(tasks)): 
                path = base_path +participant_id[id]+"/"+lab_session[lab]+"/Labeled"+"/"+tasks[i]
                path_save= base_path +participant_id[id]+"/"+lab_session[lab]+"/Preprocessed"+"/"+tasks[i]
                files_to_load = {
                                'df_bvp': 'e4_BVP.pickle',
                                'df_eda': 'e4_EDA.pickle',
                                'df_temp': 'e4_TEMP.pickle', 
                                'df_AF7':  "muse_AF7_RAW.pickle",   
                                'df_AF8':  "muse_AF8_RAW.pickle",
                                'df_TP9':  "muse_TP9_RAW.pickle",
                                'df_TP10': "muse_TP10_RAW.pickle",
                                }

                dataframes = {}  # Dictionary to store the loaded DataFrames

                for key, file_name in files_to_load.items():
                    file_path = os.path.join(path, file_name)
                    if os.path.exists(file_path):
                        dataframes[key] = pd.read_pickle(file_path)
                    else:
                        dataframes[key] = None  # or your preferred default value
                        print(f"{file_name} not found in {path}")


                print(path)
               
                if dataframes['df_AF7'] is not None:
                    df_eeg = pd.concat([dataframes['df_AF7'], dataframes['df_AF8'], dataframes['df_TP9'], dataframes['df_TP10']],axis=1)
                    df_eeg = df_eeg.reset_index(drop= True)


                    if i==0:
                        df_closed_eyes=df_eeg.iloc[(256*30):(256*60)] #[:(256*30)]# removing first/last 30 seconds as baseline from eeg data


                    df_interpolate=interpolate_rows(df_eeg, show= False)
                    print("df_interpolate", df_interpolate.shape)
                    df_high_acc= remove_high_acc(df_interpolate, eeg_columns, path, threshold, show= False)
                    print("df_high_acc", df_high_acc.shape)
                    df_clip=df_high_acc[['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']].clip(500,1000)
                    df_avg= average_reference(df_clip, show= False) 
                    df_norm= normalize(df_avg, df_closed_eyes, show= False)
                    df_bp= prefilter(df_norm, sf_eeg, show= False)
                    df_filtered_eeg= notch(df_bp, sf_eeg, f0=50, Q=50)
                    print("original_eeg", df_eeg.shape)
                    print("filtered eeg", df_filtered_eeg.shape)
#                     df_filtered_eeg.to_pickle(f"{path_save}"+"/EEG_filtered.pickle")
                    print("############# saved EEG files for task", tasks[i])
                else:
                    print("############## no df found and filtered EEG not saved for task", tasks[i])


#                 #### preprocessing BVP#####   
                if dataframes['df_bvp'] is not None:
                    df_bvp = dataframes['df_bvp'].reset_index(drop=True)
                    if i==0:
                        df_bvp_resting_state = df_bvp.iloc[(64*30):(64*60)] # last 30 seconds of the  data
                    print("bvp_interpolated_fig", len(df_bvp))

                    bvp_interpolated = interpolate_missing_values_nan(df_bvp, show= False) # takes care of both nan and missing values
                    print(len(bvp_interpolated))                
                    skewness, filtered_signals= ppg_savgol_filter(bvp_interpolated, sf_ppg, path, window_length= 41, order= 4, show= False)
                    ppg_filtered_nomalized = normalize_ppg(filtered_signals, df_bvp_resting_state, show= False)
                    print(len(ppg_filtered_nomalized))


                    filepath= f"{path_save}"+"/BVP_filtered.pickle"
                    print(ppg_filtered_nomalized.shape)
#                     pickle.dump(ppg_filtered_nomalized, open(filepath, 'wb'))
                    print("saved BVP file for task", tasks[i])
                else:
                    print("no df found and filtered BVP not saved for task", tasks[i])
                if dataframes['df_eda'] is not None:   
                    df_eda= dataframes['df_eda'].reset_index(drop= True)
                    df_eda= interpolate_missing_values_nan(df_eda, show= False)
                    filepath= f"{path_save}"+"/EDA_filtered.pickle"
#                     pickle.dump(df_eda, open(filepath, 'wb'))
                    print("saved EDA file for task", tasks[i])
                else:
                    print("no df found and filtered EDA not saved for task", tasks[i])
                if dataframes['df_temp'] is not None:      
                    df_temp= dataframes['df_temp'].reset_index(drop= True)
                    df_temp= interpolate_missing_values_nan(df_temp, show= False)
                    filepath= f"{path_save}"+"/TEMP_filtered.pickle"
#                     pickle.dump(df_temp, open(filepath, 'wb'))
                    print("saved TEMP file for task", tasks[i])
                else:
                    print("no df found and filtered TEMP not saved for task", tasks[i])

            print("****** ALL filtering done for participant id %s lab %s *****" %(participant_id[id],lab_session[lab]))
        
########### wild data preprocessing ###################



if __name__ == '__main__':
    print()
    
    base_path = ''
    participant_id =  os.listdir(base_path)
    eeg_columns=['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']
    
    #sampling_frequency
    sf_eeg = 256
    sf_eda=4
    cutoff_frequencies = [0.5, 10]
    sf_ppg = 64

    df = pd.DataFrame(columns = eeg_columns)
    
    for id in range(0, len(participant_id)) : #len(participant_id)                        
        if (participant_id[id] == 'UN_103') or (participant_id[id] == 'UN_120'):
            print( "Duration wild:", "no wild data")
        else:
            print("participant id %s " %participant_id[id])
            acc_mag, tasks = acc_all_tasks_wild (base_path, participant_id[id])
            threshold= find_threshold(acc_mag)
            print("threshold", threshold)
#             print(tasks)

        ### Lab data loading ###        
            for i in range (0,len(tasks)): 
                path = base_path +participant_id[id]+"/Wild/Labeled"+"/"+tasks[i]
                print(path)
                path_save= base_path +participant_id[id]+"/Wild/Preprocessed"+"/"+tasks[i]
                files_to_load = {
                                'df_bvp': 'e4_BVP.pickle',
                                'df_eda': 'e4_EDA.pickle',
                                'df_temp': 'e4_TEMP.pickle', 
                                'df_AF7':  "muse_AF7_RAW.pickle",   
                                'df_AF8':  "muse_AF8_RAW.pickle",
                                'df_TP9':  "muse_TP9_RAW.pickle",
                                'df_TP10': "muse_TP10_RAW.pickle",
                                }
                dataframes = {}  # Dictionary to store the loaded DataFrames

                for key, file_name in files_to_load.items():
                    file_path = os.path.join(path, file_name)
                    if os.path.exists(file_path):
                        dataframes[key] = pd.read_pickle(file_path)
                    else:
                        dataframes[key] = None  # or your preferred default value
                        print(f"{file_name} not found in {path}")

                if (participant_id[id] == 'UN_111') or (participant_id[id] == 'UN_105')or (participant_id[id] == 'UN_107'):
                    dataframes['df_AF7'] = dataframes['df_AF7'].reset_index(drop= True)
                    dataframes['df_AF8'] = dataframes['df_AF8'].reset_index(drop= True)
                    dataframes['df_TP9'] = dataframes['df_TP9'].reset_index(drop= True)
                    dataframes['df_TP10'] = dataframes['df_TP10'].reset_index(drop= True)
                    print(dataframes['df_AF7'].shape)
                    print(dataframes['df_AF8'].shape)
                    print(dataframes['df_TP9'].shape)
                    print(dataframes['df_TP10'].shape)
                if dataframes['df_AF7'] is not None:
                    df_eeg = pd.concat([dataframes['df_AF7'], dataframes['df_AF8'], dataframes['df_TP9'], dataframes['df_TP10']],axis=1)
                    print(df_eeg.shape)
                    df_eeg = df_eeg.reset_index(drop= True)


                    df_interpolate=interpolate_rows(df_eeg, show= False)
                    print("df_interpolate", df_interpolate.shape)
                    df_high_acc= remove_high_acc(df_interpolate, eeg_columns, path, threshold, show= False)
                    print("df_high_acc", df_high_acc.shape)
                    df_clip=df_high_acc[['RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10']].clip(500,1000)
                    df_avg= average_reference(df_clip, show= False) 
                    df_norm= normalize_wild(df_avg, show= False)
                    df_bp= prefilter(df_norm, sf_eeg, show= False)
                    df_filtered_eeg= notch(df_bp, sf_eeg, f0=50, Q=50)
                    print("original_eeg", df_eeg.shape)
                    print("filtered eeg", df_filtered_eeg)
                    df_filtered_eeg.to_pickle(f"{path_save}"+"/EEG_filtered.pickle")
                    print("saved EEG files for task", tasks[i])
                else:
                    print("no df found and filtered EEG not saved for task", tasks[i])


    #                 #### preprocessing BVP#####   
                if dataframes['df_bvp'] is not None:
                    df_bvp = dataframes['df_bvp'].reset_index(drop=True)

                    bvp_interpolated = interpolate_missing_values_nan(df_bvp, show= False) # takes care of both nan and missing values
                    print(len(bvp_interpolated))                
                    skewness, filtered_signals= ppg_savgol_filter(bvp_interpolated, sf_ppg, path, window_length= 41, order= 4, show= False)
                    ppg_filtered_nomalized = normalize_ppg_wild(filtered_signals, show= False)
                    print(len(ppg_filtered_nomalized))


                    filepath= f"{path_save}"+"/BVP_filtered.pickle"
                    print(ppg_filtered_nomalized.shape)
                    pickle.dump(ppg_filtered_nomalized, open(filepath, 'wb'))
                    print("saved BVP file for task", tasks[i])
                else:
                    print("no df found and filtered BVP not saved for task", tasks[i])
                if dataframes['df_eda'] is not None:   
                    df_eda= dataframes['df_eda'].reset_index(drop= True)
                    df_eda= interpolate_missing_values_nan(df_eda, show= False)
                    filepath= f"{path_save}"+"/EDA_filtered.pickle"
                    pickle.dump(df_eda, open(filepath, 'wb'))
                    print("saved EDA file for task", tasks[i])
                else:
                    print("no df found and filtered EDA not saved for task", tasks[i])
                if dataframes['df_temp'] is not None:      
                    df_temp= dataframes['df_temp'].reset_index(drop= True)
                    df_temp= interpolate_missing_values_nan(df_temp, show= False)
                    filepath= f"{path_save}"+"/TEMP_filtered.pickle"
                    pickle.dump(df_temp, open(filepath, 'wb'))
                    print("saved TEMP file for task", tasks[i])
                else:
                    print("no df found and filtered TEMP not saved for task", tasks[i])

            print("*********************** ALL filtering done for participant id %s **********" %participant_id[id])







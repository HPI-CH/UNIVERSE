import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy
import math
import pandas as pd
from scipy.signal import butter, lfilter, savgol_filter, find_peaks
import pywt
from pypg.plots import simple_plot
import padasip as pa
import pypg.filters
import pypg.quality
from pypg.plots import simple_plot
from pypg.quality import skewness
import neurokit2 as nk
import biosppy.signals
from neurokit2.signal.signal_formatpeaks import _signal_from_indices
from neurokit2.signal import signal_rate

figure_path= "/dhc/cold/groups/idyll/TEMPORARY_DATA_MANIPULATION/(xtracted_figure)"

def interpolate_missing_values_nan(bvp_series, show= False):

    interpolation_method = 'linear'  # nearest, linear, zero 
    bvp_series[bvp_series == 0] = np.NaN
    bvp_series = pd.to_numeric(bvp_series)
    bvp_series = bvp_series.interpolate(method=interpolation_method)
    bvp_series = bvp_series.fillna(method='backfill')


    if show== True:
        plt.rcParams["figure.figsize"]=20,10
        print("Original df:")
        bvp_series.plot(subplots=True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=8,
                 legend=False,
                 linewidth=0.8);
        plt.show()

    return bvp_series


def normalize_ppg(df, df_resting_state, show= False):
    df = df - np.nanmean(df_resting_state)
    min_value = df.min()
    max_value = df.max()
    df = (df - min_value) / (max_value - min_value)
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

def normalize_ppg_wild(df, show= False):
#     df = df - np.nanmean(df_resting_state)
    min_value = df.min()
    max_value = df.max()
    df = (df - min_value) / (max_value - min_value)
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

# def normalize_ppg(ppg): #bvp_array from empatica normalize bvp data to [-1 1] # we can think of min_max normalization 
#     a = -1
#     b = 1
#     ppg= a + ((ppg - np.min(ppg)) * (b - a) / (np.max(ppg) - np.min(ppg)))
    
#     return ppg

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


def ppg_savgol_filter (ppg, sf_ppg, path, window_length, order, show):
    ppg_savgol= savgol_filter(ppg, window_length, order)
    skewness_savgol= pypg.quality.skewness(ppg_savgol, sf_ppg, window=1, mode='avg')
    filtered_signal = pd.DataFrame({'savgol_filter_ppg': ppg_savgol})    
    if show == True:
        plt.rcParams["figure.figsize"]=30,30
        filtered_signal.plot(subplots= True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=12,
                 legend=True,
                 linewidth=0.9);
        plt.show()
        
        simple_plot(ppg=ppg, title='original BVP signal', figure_path=figure_path)# , label='original'
        simple_plot(ppg=ppg_savgol, title='filtered BVP ', figure_path=figure_path) #, label='bvp_filtered
        
    return skewness_savgol, filtered_signal 


def calculating_hr(ppg_clean, sf_ppg, show): #### calculating HR or PPG_rate 


        ### from neurokit2
        info = nk.ppg_findpeaks(ppg_clean, sampling_rate=64, show=False)
        

        # # Mark peaks
        # peaks_signal = _signal_from_indices(info["PPG_Peaks"], desired_length=len(ppg_clean))

        # Rate computation
        heart_rate = signal_rate(info["PPG_Peaks"], sampling_rate=sf_ppg, desired_length=len(ppg_clean))



        # outlier rejection
        peaks, _ = find_peaks(heart_rate)
        data = heart_rate[peaks]
        data_cor = []  # corrected array
        data_cor.append(data[0:1])  # corrected array

        for i in range(len(data) - 2):  # two first points are already appended
            i += 2
            delta_i = data[i] / data[i - 1]
            if 0.9 < delta_i < 1.1:
                data_cor.append(data[i])
            else:
                data_cor.append(float('nan'))
                
        if len(data_cor)!=1:  
            heart_rate_corrected = [x for x in data_cor if math.isnan(x) == False]    
        else:            
            print(len(data_cor))
            heart_rate_corrected = heart_rate
        
        if len(heart_rate_corrected)==1 or len(data_cor)==1: ### happening only for eye closing session of rls_wav_sav filter ## TODO ??? 
            heart_rate_resampled= heart_rate
        else:
            del heart_rate_corrected[0]
            heart_rate_resampled = signal.resample(heart_rate_corrected, len(ppg_clean))
        x = pd.Series(heart_rate_resampled)  # 200 values
        outliers = x.loc[~x.between(x.quantile(.05), x.quantile(.95))].index  # without outliers
        x.loc[outliers] = np.nan
        heart_rate_no_outliers = x.interpolate(method='linear')  # without outliers
        heart_rate_no_outliers = pd.DataFrame(heart_rate_no_outliers, columns=[ "HR"])
        
        if show== True:
            print("number of PPG_peaks",len(info['PPG_Peaks']))
            print("heart_rate",len(heart_rate))
            print("heart_rate_corrected",len(heart_rate_corrected))
            print("heart_rate_resampled",len(x))
            print("heart_rate_no_outliers",len(heart_rate_no_outliers))
            plt.plot(heart_rate, color='r', label='heart_rate')
            plt.plot(heart_rate_no_outliers, color='g', label='heart_rate_no_outliers')

            plt.xlabel("Samples")
            plt.ylabel("Heart Rate")

            plt.legend()
            plt.show()
        
        return info, heart_rate, heart_rate_no_outliers

def butter_bandpass(lowcut, highcut, fs, order_bp):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order_bp, [low, high], btype='band')
    return b, a

def _butter_bandpass_filter(data, lowcut, highcut, fs, order_bpf):
    b, a = butter_bandpass(lowcut, highcut, fs, order_bpf)
    y = lfilter(b, a, data)
    return y



def denoise_ppg_wavelet_decom(ppg): 
    
    # Wavelet decomposition
    # Create wavelet object and define parameters
    w = pywt.Wavelet('sym4')
    maxlev = pywt.dwt_max_level(len(ppg), w.dec_len)
    # maxlev = 2 # Override if desired
    threshold = 0.04  # Threshold for filtering
    coeffs = pywt.wavedec(ppg, 'sym4', level=maxlev)
    bvp_after_wavelet = pywt.waverec(coeffs, 'sym4')
    
    return bvp_after_wavelet

def rls_wav_sav_filter(bvp_array, window_length, order, path): # window_length odd number larger than order 
   
    # bandpass parameters
    fs = 64.0
    lowcut = 0.5
    highcut = 3.5
    order = 4

    # get acc array 
    acc_x=pd.read_pickle(f"{path}"+"/e4_ACC_X.pickle") ## not unified for wild and lab
    acc_x = acc_x[~np.isnan(acc_x)]

    acc_y=pd.read_pickle(f"{path}"+"/e4_ACC_Y.pickle")
    acc_y = acc_y[~np.isnan(acc_y)]

    acc_z=pd.read_pickle(f"{path}"+"/e4_ACC_Z.pickle")
    acc_z = acc_z[~np.isnan(acc_z)]

    # normalize bvp data to [-1 1]
    a = -1
    b = 1
    bvp_array = a + ((bvp_array - np.min(bvp_array)) * (b - a) / (np.max(bvp_array) - np.min(bvp_array)))

    # normalize acc data to [-1 1]
    acc_x = a + ((acc_x - np.min(acc_x)) * (b - a) / (np.max(acc_x) - np.min(acc_x)))
    acc_y = a + ((acc_y - np.min(acc_y)) * (b - a) / (np.max(acc_y) - np.min(acc_y)))
    acc_z = a + ((acc_z - np.min(acc_z)) * (b - a) / (np.max(acc_z) - np.min(acc_z)))

    # upsample do the sampling rate matched BVP
    acc_x_resampled = signal.resample(acc_x, bvp_array.size)
    acc_y_resampled = signal.resample(acc_y, bvp_array.size)
    acc_z_resampled = signal.resample(acc_z, bvp_array.size)

    # bandpass
    bvp_array_filtered = _butter_bandpass_filter(bvp_array, lowcut, highcut, fs, order)
    acc_x_filtered = _butter_bandpass_filter(acc_x_resampled, lowcut, highcut, fs, order)
    acc_y_filtered = _butter_bandpass_filter(acc_y_resampled, lowcut, highcut, fs, order)
    acc_z_filtered = _butter_bandpass_filter(acc_z_resampled, lowcut, highcut, fs, order)

    # noise reduction
    bvp_array_denoised = savgol_filter(bvp_array_filtered, window_length, order) #window length= odd number, lower than the length of the array
    acc_x_denoised = savgol_filter(acc_x_filtered, window_length, order)
    acc_y_denoised = savgol_filter(acc_y_filtered, window_length, order)
    acc_z_denoised = savgol_filter(acc_z_filtered, window_length, order)

    # adaptive noise cancellation
    acc_matrix = np.column_stack((acc_x_denoised, acc_y_denoised, acc_z_denoised))
    # identification
    filter_RLS = pa.filters.FilterRLS(n=3, mu=0.999, eps=0.1, w='zeros')
    bvp_after_rls, _, _ = filter_RLS.run(bvp_array_denoised, acc_matrix)

    # Wavelet decomposition
    # Create wavelet object and define parameters
    w = pywt.Wavelet('sym4')
    maxlev = pywt.dwt_max_level(len(bvp_after_rls), w.dec_len)
    # maxlev = 2 # Override if desired
    threshold = 0.04  # Threshold for filtering
    coeffs = pywt.wavedec(bvp_after_rls, 'sym4', level=maxlev)
    bvp_after_wavelet = pywt.waverec(coeffs, 'sym4')
    
    
    return bvp_after_wavelet#heart_rate_no_outliers

def plot_filters(ppg, cutoff_frequencies, sf_ppg, path, window_length, order, show): # needs further investigation: length(movefy) = length(other filters)+1    
    skew_original= pypg.quality.skewness(ppg, 64, window=1, mode='avg')
    
    
    ppg_butterfy= pypg.filters.butterfy(ppg, cutoff_frequencies, sf_ppg, filter_type='bandpass',
             filter_order=4, verbose= False, figure_path= figure_path )
#     print(ppg_butterfy.shape)
    skew_butterfy= pypg.quality.skewness(ppg_butterfy, sf_ppg, window=1, mode='avg')

    
    ppg_chebyfy= pypg.filters.chebyfy(ppg, cutoff_frequencies, sf_ppg, filter_type='bandpass',
             filter_order=4, verbose= False, figure_path= figure_path )
#     print(ppg_chebyfy.shape)
    skew_chebyfy= pypg.quality.skewness(ppg_chebyfy, sf_ppg, window=1, mode='avg')

    ppg_movefy= pypg.filters.movefy(ppg, size=100, verbose= False, figure_path= figure_path )
#     print(ppg_movefy.shape)
    skew_movefy= pypg.quality.skewness(ppg_movefy, 64, window=1, mode='avg')
    

    ppg_waveletfy=denoise_ppg_wavelet_decom(ppg)
    skew_waveletfy= pypg.quality.skewness(ppg_waveletfy, sf_ppg, window=1, mode='avg')

    ppg_savgol= savgol_filter(ppg, window_length, order)
    skew_savgol= pypg.quality.skewness(ppg_savgol, sf_ppg, window=1, mode='avg')

    ppg_rls_wav_sav= rls_wav_sav_filter(ppg, window_length, order,path)
    skew_rls_wav_sav= pypg.quality.skewness(ppg_rls_wav_sav, sf_ppg, window=1, mode='avg')
     

    ppg_nk= nk.ppg_clean(ppg, sampling_rate=sf_ppg) # deafult method='elgendi'
    skew_nk= pypg.quality.skewness(ppg_nk, sf_ppg, window=1, mode='avg')
     
    _, ppg_biosspy, _, _, _ = biosppy.signals.bvp.bvp(signal=ppg, sampling_rate=sf_ppg, show= False)
    skew_biosppy= pypg.quality.skewness(ppg_biosspy, sf_ppg, window=1, mode='avg')
    
    filtered_signals = pd.DataFrame({'Raw' : ppg,
                    'butterfy' : ppg_butterfy,
                    'chebyfy' :  ppg_chebyfy,
#                     'movefy' : ppg_movefy,
                    'waveletfy': ppg_waveletfy,
                    'savgol': ppg_savgol,
                    'rls_wav_sav':ppg_rls_wav_sav, 
                    'nk': ppg_nk, 
                    'biosspy': ppg_biosspy  })

    
    data = {'skewness': ['skew_original','skew_butterfy', 'skew_chebyfy',  'skew_waveletfy', 'skew_savgol','skew_rls_wav_sav', 'skew_nk', 'skew_biosppy'],
        'value': [skew_original, skew_butterfy, skew_chebyfy, skew_waveletfy, skew_savgol, skew_rls_wav_sav, skew_nk, skew_biosppy]}

    skewness_all = pd.DataFrame(data)
    
    if show == True:
        plt.rcParams["figure.figsize"]=30,30
        filtered_signals.plot(subplots= True,
                  layout=(5, 5),
                  sharex=False,
                  sharey=False,
                  colormap='viridis',
                 fontsize=12,
                 legend=True,
                 linewidth=0.9);
        plt.show()
        
#         simple_plot(ppg=ppg, title='original BVP signal', figure_path=figure_path)# , label='original'
#         simple_plot(ppg=ppg_chebyfy, title='filtered BVP ', figure_path=figure_path) #, label='bvp_filtered
        
    return skewness_all, filtered_signals 


    

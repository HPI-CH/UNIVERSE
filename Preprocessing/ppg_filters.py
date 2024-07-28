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

figure_path= ""

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

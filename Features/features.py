from os import name
import pandas as pd
import numpy as np
import yasa
from scipy import signal
from numpy.lib.stride_tricks import as_strided





def windowed_view(arr, window, overlap):
    arr = np.asarray(arr)
    window_step = window - overlap
    new_shape = arr.shape[:-1] + ((arr.shape[-1] - overlap) // window_step,
                                  window)
    new_strides = (arr.strides[:-1] + (window_step * arr.strides[-1],) +
                   arr.strides[-1:])
    return as_strided(arr, shape=new_shape, strides=new_strides)



def power_features(df, sampling_frequency, window_size, overlap, bands): #y

    feature_names=['δ_TP9','θ_TP9','α_TP9', 'β_TP9', 'γ_TP9',
                   'δ_AF7','θ_AF7','α_AF7', 'β_AF7', 'γ_AF7',
                   'δ_AF8','θ_AF8','α_AF8', 'β_AF8', 'γ_AF8',
                   'δ_TP10','θ_TP10','α_TP10', 'β_TP10', 'γ_TP10']
    df_feature = pd.DataFrame(columns=feature_names)

    freqs, psd = signal.welch(x=df, fs=sampling_frequency, window="hann", nperseg=window_size, noverlap=0, axis=-1) 
    bandpower = yasa.bandpower_from_psd_ndarray(psd, freqs, bands) # Calculate the bandpower on 3-D PSD array
    bandpower=np.transpose(bandpower, (1, 2, 0))

      
    array_to_df=bandpower[0].flatten()
    for i in range(1, bandpower.shape[0]):
        array_to_df=np.vstack((array_to_df, bandpower[i].flatten()))
        current_df=pd.DataFrame(array_to_df, columns=feature_names) 
#     current_df['y']=y 
    return current_df



def add_more_power_features(df_feature):
    df_feature['α/β_TP9'] = df_feature['α_TP9']/df_feature['β_TP9']
    df_feature['(θ + α)/β_TP9'] = (df_feature['θ_TP9']+df_feature['α_TP9'])/ df_feature['β_TP9']
    df_feature['(θ + α)/(α + β)_TP9'] = (df_feature['θ_TP9']+df_feature['α_TP9'])/ (df_feature['α_TP9']+df_feature['β_TP9'])
    df_feature['θ/β_TP9'] = df_feature['θ_TP9']/df_feature['β_TP9']
    
    
    
    
    df_feature['α/β_AF7'] = df_feature['α_AF7']/df_feature['β_AF7']
    df_feature['(θ + α)/β_AF7'] = (df_feature['θ_AF7']+df_feature['α_AF7'])/ df_feature['β_AF7']
    df_feature['(θ + α)/(α + β)_AF7'] = (df_feature['θ_AF7']+df_feature['α_AF7'])/ (df_feature['α_AF7']+df_feature['β_AF7'])
    df_feature['θ/β_AF7'] = df_feature['θ_AF7']/df_feature['β_AF7']
    
    
    
    df_feature['α/β_AF8'] = df_feature['α_AF8']/df_feature['β_AF8']
    df_feature['(θ + α)/β_AF8'] = (df_feature['θ_AF8']+df_feature['α_AF8'])/ df_feature['β_AF8']
    df_feature['(θ + α)/(α + β)_AF8'] = (df_feature['θ_AF8']+df_feature['α_AF8'])/ (df_feature['α_AF8']+df_feature['β_AF8'])
    df_feature['θ/β_TP9'] = df_feature['θ_TP9']/df_feature['β_TP9']
    
    
    
    df_feature['α/β_TP10'] = df_feature['α_TP10']/df_feature['β_TP10']
    df_feature['(θ + α)/β_TP10'] = (df_feature['θ_TP10']+df_feature['α_TP10'])/ df_feature['β_TP10']
    df_feature['(θ + α)/(α + β)_TP10'] = (df_feature['θ_TP10']+df_feature['α_TP10'])/ (df_feature['α_TP10']+df_feature['β_TP10'])
    df_feature['θ/β_TP10'] = df_feature['θ_TP10']/df_feature['β_TP10']
    
    df_feature['mean_δ'] = (df_feature['δ_TP9']+df_feature['δ_AF7']+df_feature['δ_AF8']+df_feature['δ_TP10'])/4
    df_feature['mean_θ'] = (df_feature['θ_TP9']+df_feature['θ_AF7']+df_feature['θ_AF8']+df_feature['θ_TP10'])/4
    df_feature['mean_α'] =  (df_feature['α_TP9']+df_feature['α_AF7']+df_feature['α_AF8']+df_feature['α_TP10'])/4
    df_feature['mean_β'] = (df_feature['β_TP9']+df_feature['β_AF7']+df_feature['β_AF8']+df_feature['β_TP10'])/4
    df_feature['mean_γ'] = (df_feature['γ_TP9']+df_feature['γ_AF7']+df_feature['γ_AF8']+df_feature['γ_TP10'])/4
    
    df_feature['δ_asy_AF8_AF7'] = np.log(df_feature['δ_AF8'].astype('float64'))-np.log(df_feature['δ_AF7'].astype('float64'))
    df_feature['δ_asy_TP10_TP9']= np.log(df_feature['δ_TP10'].astype('float64'))-np.log(df_feature['δ_TP9'].astype('float64'))
    
    df_feature['θ_asy_AF8_AF7'] = np.log(df_feature['θ_AF8'].astype('float64'))-np.log(df_feature['θ_AF7'].astype('float64'))
    df_feature['θ_asy_TP10_TP9']= np.log(df_feature['θ_TP10'].astype('float64'))-np.log(df_feature['θ_TP9'].astype('float64'))
    
    df_feature['α_asy_AF8_AF7'] = np.log(df_feature['α_AF8'].astype('float64'))-np.log(df_feature['α_AF7'].astype('float64'))
    df_feature['α_asy_TP10_TP9']= np.log(df_feature['α_TP10'].astype('float64'))-np.log(df_feature['α_TP9'].astype('float64'))
    
    df_feature['β_asy_AF8_AF7'] = np.log(df_feature['β_AF8'].astype('float64'))-np.log(df_feature['β_AF7'].astype('float64'))
    df_feature['β_asy_TP10_TP9']= np.log(df_feature['β_TP10'].astype('float64'))-np.log(df_feature['β_TP9'].astype('float64'))
    
    df_feature['γ_asy_AF8_AF7'] = np.log(df_feature['γ_AF8'].astype('float64'))-np.log(df_feature['γ_AF7'].astype('float64'))
    df_feature['γ_asy_TP10_TP9']= np.log(df_feature['γ_TP10'].astype('float64'))-np.log(df_feature['γ_TP9'].astype('float64'))
    return df_feature

def add_new_features(df_feature):
    
    df_feature['θ/β_AF8'] = df_feature['θ_AF8']/df_feature['β_AF8']
    df_feature['α/β'] = (df_feature['α/β_TP9']+df_feature['α/β_AF7']+df_feature['α/β_AF8']+df_feature['α/β_TP10'])/4
    df_feature['(θ + α)/β'] = (df_feature['(θ + α)/β_TP9']+df_feature['(θ + α)/β_AF7']+df_feature['(θ + α)/β_AF8']+df_feature['(θ + α)/β_TP10'])/4
    df_feature['(θ + α)/(α + β)'] = (df_feature['(θ + α)/(α + β)_TP9']+df_feature['(θ + α)/(α + β)_AF7']+df_feature['(θ + α)/(α + β)_AF8']+df_feature['(θ + α)/(α + β)_TP10'])/4
    df_feature['θ/β'] = (df_feature['θ/β_TP9']+df_feature['θ/β_AF7']+df_feature['θ/β_AF8']+df_feature['θ/β_TP10'])/4
    df_feature['α/θ'] = df_feature['mean_α']/df_feature['mean_θ']
    df_feature['θ/α']=df_feature['mean_θ']/df_feature['mean_α']

    df_feature['frontal_α_asy'] = np.log(df_feature['α_AF8'].astype('float64'))-np.log(df_feature['α_AF7'].astype('float64'))


    df_feature['δ_asy'] = np.log((df_feature['δ_AF8']+df_feature['δ_TP10']).astype('float64'))-np.log((df_feature['δ_AF7']+df_feature['δ_TP9']).astype('float64'))
    df_feature['θ_asy'] = np.log((df_feature['θ_AF8']+df_feature['θ_TP10']).astype('float64'))-np.log((df_feature['θ_AF7']+df_feature['θ_TP9']).astype('float64'))
    df_feature['α_asy'] = np.log((df_feature['α_AF8']+df_feature['α_TP10']).astype('float64'))-np.log((df_feature['α_AF7']+df_feature['α_TP9']).astype('float64'))
    df_feature['β_asy'] = np.log((df_feature['β_AF8']+df_feature['β_TP10']).astype('float64'))-np.log((df_feature['β_AF7']+df_feature['β_TP9']).astype('float64'))
    df_feature['γ_asy'] = np.log((df_feature['γ_AF8']+df_feature['γ_TP10']).astype('float64'))-np.log((df_feature['γ_AF7']+df_feature['γ_TP9']).astype('float64'))
    
    return df_feature
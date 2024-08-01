import sys
from typing import List
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from datetime import datetime, timedelta
import re

#Plot graphs for muse and empatica


def normalize(x: List[float]): #Taken from jointly
    """Normalizes signal to interval [-1, 1] with mean 0."""
    if len(x) <= 1:
        raise ValueError("Cannot normalize list with less than 2 entries")
    x_centered = x - np.mean(x)
    x_maximum = np.max(np.abs(x_centered))
    if x_maximum == 0:
        raise ZeroDivisionError("input vector is all-zero")
    x_normalized = x_centered / x_maximum
    return x_normalized


def normalize_series(column: pd.Series) -> pd.Series:
    a = column.dropna()

    # get a pandas series with rows that are not zero, since jointly added zeros to stretch the data.
    # And for the original ones, we just remove a few zeros which would not affect much
    a = a[a != 0]
    a = a[a != 0.0]

    a = pd.Series(normalize(a), a.index) #Normalize values and get indexes of the series (with removed zero rows)
    return a

def plotter(df, x, y_columns, path, counter, title="", linewidth=2.0, x_tick_rotation=45, show=False, alpha=0.9):
    df.plot(x=x, y=y_columns, title=title, kind="line", linewidth=linewidth, figsize=(15, 15), alpha=alpha)
    plt.xticks(rotation=x_tick_rotation)
    plt.savefig(path + str(counter) + ".pdf")
    counter = counter + 1
    if show is True:
        plt.show()
    plt.clf()
    return counter

def plotter_with_peaks(df, x, y_columns, array_of_peaks, path, counter, title="", linewidth=2.0, x_tick_rotation=45, show=False, alpha=0.9):
    df.plot(x=x, y=y_columns, title=title, kind="line", linewidth=linewidth, figsize=(15, 15), alpha=alpha)
    plt.plot(array_of_peaks, df[y_columns[0]].iloc[array_of_peaks], "mx", alpha=0.75)

    plt.xticks(rotation=x_tick_rotation)
    plt.savefig(path + str(counter) + ".pdf")
    counter = counter + 1
    if show is True:
        plt.show()
    plt.clf()
    return counter




#get timestamp between 2 peaks (since peaks are acceleration of up and down movement)
def calculate_spacebarpress_between_peaks(time_stamp_for_peaks):
    aux_time_stamp_for_peaks = []
    for i in range(0, len(time_stamp_for_peaks), 2):
        #print(time_stamp_for_peaks[i])
        #print(time_stamp_for_peaks[i + 1])
        aux_time_stamp_for_peaks.append(time_stamp_for_peaks[i + 1] - time_stamp_for_peaks[i])

    aux_time_stamp_for_peaks = [timedelta(seconds=((x.total_seconds()) / 2)) for x in aux_time_stamp_for_peaks]
    # print(F"aux_time_stamp_for_peaks: {aux_time_stamp_for_peaks}")
    aux = []
    for i in range(0, len(time_stamp_for_peaks), 2):
        aux.append(time_stamp_for_peaks[i])

    for i in range(len(aux_time_stamp_for_peaks)):
        aux[i] = aux[i] + aux_time_stamp_for_peaks[i]
    # print(F"aux: {aux}")

    return aux




def get_acceleration_peak_time(folder_path, merged_df_path):
    #folder_path = "../Data/3. Spacebar Tap Test 2/"
    #folder_path = "../Data/2. Pilot Study Data/3. Samik/"
    #psychopy_log_file_path = folder_path + "psychopy_test_experiment/data/test1_test_experiment_2022-06-14_15h50.26.995.log"
    #df = pd.read_csv(folder_path + "merged_DF.csv")

    df = pd.read_csv(merged_df_path)

    plots_path = folder_path + "Plots/"
    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    counter = 0
    x_tick_rotation = 45
    linewidth = 2.0
    alpha = 0.67



    #Empatica Acceleration
    ACC_X_EMPATICA = normalize_series(df["ACC_X_EMPATICA"])
    ACC_Y_EMPATICA = normalize_series(df["ACC_Y_EMPATICA"])
    ACC_Z_EMPATICA = normalize_series(df["ACC_Z_EMPATICA"])
    TimeStamp = df["TimeStamp"].copy()
    empatica_df = pd.concat([TimeStamp, ACC_X_EMPATICA, ACC_Y_EMPATICA, ACC_Z_EMPATICA], axis=1).reset_index() #concatentation of series

    counter = plotter(empatica_df, "TimeStamp", ["ACC_X_EMPATICA", "ACC_Y_EMPATICA", "ACC_Z_EMPATICA"], plots_path, counter, title="Normalized Acceleration for Empatica", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)
    counter = plotter(df, "TimeStamp", ["ACC_X_EMPATICA", "ACC_Y_EMPATICA", "ACC_Z_EMPATICA"], plots_path, counter, title="Acceleration for Empatica", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)




    #Muse Acceleration Magnitude
    ACC_MAG_MUSE = normalize_series(df["ACC_MAG_MUSE"])
    TimeStamp = df["TimeStamp"].copy()
    muse_mag_df = pd.concat([TimeStamp, ACC_MAG_MUSE], axis=1).reset_index()  # concatentation of series

    #Normlized and zeros removed
    counter = plotter(muse_mag_df, "TimeStamp", ["ACC_MAG_MUSE"], plots_path, counter, title="Normalized Acceleration Magnitude for Muse (after jointly data stretching with zeross)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)
    counter = plotter(df, "TimeStamp", ["ACC_MAG_MUSE"], plots_path, counter, title="Acceleration Magnitude for Muse (after jointly data stretching with zeross)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)



    #Empatica Acceleration Magnitude
    #print(F"df rows:  {len(df.index)}")
    ACC_MAG_EMPATICA = normalize_series(df["ACC_MAG_EMPATICA"])
    #print(F"ACC_MAG_EMPATICA rows after normalization:  {len(ACC_MAG_EMPATICA.index)}")

    TimeStamp = df["TimeStamp"].copy()
    empatica_mag_df = pd.concat([TimeStamp, ACC_MAG_EMPATICA], axis=1).reset_index()  # concatentation of series
    #print(F"empatica_mag_df rows:  {len(empatica_mag_df.index)}")

    counter = plotter(empatica_mag_df, "TimeStamp", ["ACC_MAG_EMPATICA"], plots_path, counter, title="Normalized Acceleration Magnitude for Empatica (after jointly data stretching with zeros)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)
    counter = plotter(df, "TimeStamp", ["ACC_MAG_EMPATICA"], plots_path, counter, title="Acceleration Magnitude for Empatica (after jointly data stretching with zeros)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)



    merge_empatica_muse_df = pd.merge(empatica_mag_df, muse_mag_df, how='inner', on="TimeStamp").reset_index().dropna()
    counter = plotter(merge_empatica_muse_df, "TimeStamp", ["ACC_MAG_EMPATICA", "ACC_MAG_MUSE"], plots_path, counter, title="Merged Muse-Empatica Data Frame (inner join on Timestamp)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)

    merge_empatica_muse_df = merge_empatica_muse_df.drop(['index', 'index_x', 'index_y'], axis=1)
    merge_empatica_muse_df.set_index('TimeStamp')
    merge_empatica_muse_df.to_csv(plots_path + "joined_muse_empatica_ACC_MAG_on_TimeStamp_with_dropped_NA.csv")

    print()



    minimum_peak_height = 0.20
    maximum_peak_height = 0.70
    acc_mag_empatica_array = merge_empatica_muse_df["ACC_MAG_EMPATICA"].values
    peaks, properties = find_peaks(acc_mag_empatica_array, height=[minimum_peak_height, maximum_peak_height])
    #print(F"peaks: {peaks}")
    counter = plotter_with_peaks(merge_empatica_muse_df, "TimeStamp", ["ACC_MAG_EMPATICA", "ACC_MAG_MUSE"], peaks, plots_path, counter, title="Merged Muse-Empatica Data Frame (inner join on Timestamp) with peaks marked", linewidth=linewidth, x_tick_rotation=x_tick_rotation, show=True, alpha=alpha)

    time_stamp_for_peaks_empatica = [merge_empatica_muse_df["TimeStamp"].iloc[x] for x in peaks]
    norm_acc_mag_for_peaks = [merge_empatica_muse_df["ACC_MAG_EMPATICA"].iloc[x] for x in peaks]
    print(F"time_stamp_for_peaks_empatica: {time_stamp_for_peaks_empatica}")
    print(F"norm_acc_mag_for_peaks: {norm_acc_mag_for_peaks}")

    print()
    print()

    #Manually remove peaks (first set slice of start peaks and then of end peaks)
    start_1 = 8
    end_1 = 16
    time_stamp_for_peaks_empatica_1 = time_stamp_for_peaks_empatica[start_1:end_1]
    norm_acc_mag_for_peaks_1 = norm_acc_mag_for_peaks[start_1:end_1]
    peaks_1 = peaks[start_1:end_1]

    start_2 = -9
    end_2 = -1 #use 'None' to slice till the end (-1 is 1 before the last element)
    time_stamp_for_peaks_empatica_2 = time_stamp_for_peaks_empatica[start_2:end_2]
    norm_acc_mag_for_peaks_2 = norm_acc_mag_for_peaks[start_2:end_2]
    peaks_2 = peaks[start_2:end_2]

    #Combine slices from start and end
    time_stamp_for_peaks_empatica = []
    norm_acc_mag_for_peaks = []
    peaks = []

    time_stamp_for_peaks_empatica.extend(time_stamp_for_peaks_empatica_1)
    time_stamp_for_peaks_empatica.extend(time_stamp_for_peaks_empatica_2)

    norm_acc_mag_for_peaks.extend(norm_acc_mag_for_peaks_1)
    norm_acc_mag_for_peaks.extend(norm_acc_mag_for_peaks_2)

    peaks.extend(peaks_1)
    peaks.extend(peaks_2)



    num_peaks_found = len(norm_acc_mag_for_peaks)
    print(F"num peaks found: {num_peaks_found}")
    print(F"time_stamp_for_peaks_empatica: {time_stamp_for_peaks_empatica}")
    print(F"norm_acc_mag_for_peaks: {norm_acc_mag_for_peaks}")
    counter = plotter_with_peaks(merge_empatica_muse_df, "TimeStamp", ["ACC_MAG_EMPATICA", "ACC_MAG_MUSE"], peaks, plots_path, counter, title="Merged Muse-Empatica Data Frame (inner join on Timestamp) with space bar-tapped peaks marked", linewidth=linewidth, x_tick_rotation=x_tick_rotation, show=True, alpha=alpha)

    if num_peaks_found != 16:
        raise Exception(F"Found {num_peaks_found} acceleration peaks instead of the required 16 for Empatica.")

    time_stamp_for_peaks_empatica = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') for x in time_stamp_for_peaks_empatica]

    time_stamp_for_peaks_empatica = calculate_spacebarpress_between_peaks(time_stamp_for_peaks_empatica) #get timestamp between 2 peaks (since peaks are acceleration of up and down movement), so the spacebar press is in the middle of 2 peaks
    print(F"***Timestamp for space bar presses (so middle time between 2 peaks): {time_stamp_for_peaks_empatica}")


    peak_time_duration_from_first_to_last_empatica = []
    for i in range(len(time_stamp_for_peaks_empatica)):
        peak_time_duration_from_first_to_last_empatica.append(time_stamp_for_peaks_empatica[i] - time_stamp_for_peaks_empatica[0])
    print(F"peak_time_duration_from_first_to_last_empatica: {peak_time_duration_from_first_to_last_empatica}")

    print()

    #Peak summarry
    start_timestamp = time_stamp_for_peaks_empatica[0]
    end_timestamp = time_stamp_for_peaks_empatica[-1]
    print(F"Total Duration between first and last peak:   {end_timestamp - start_timestamp}")

    start_timestamp_grp_1 = time_stamp_for_peaks_empatica[0]
    end_timestamp_grp_1 = time_stamp_for_peaks_empatica[3]
    duration_1 = end_timestamp_grp_1-start_timestamp_grp_1
    print(F"***GROUP_1:    Duration: {duration_1}    |    peak_start_timestamp: {start_timestamp_grp_1}    |    peak_end_timestamp: {end_timestamp_grp_1}")

    start_timestamp_grp_2 = time_stamp_for_peaks_empatica[4]
    end_timestamp_grp_2 = time_stamp_for_peaks_empatica[7]
    duration_2 = end_timestamp_grp_2-start_timestamp_grp_2
    print(F"***GROUP_2:    Duration: {duration_2}    |    peak_start_timestamp: {start_timestamp_grp_2}    |    peak_end_timestamp: {end_timestamp_grp_2}")

    total_duration = time_stamp_for_peaks_empatica[4] - time_stamp_for_peaks_empatica[3]
    print(F"***TOTAL DURATION between start and end of space press (so time between last tap from the start group and first tap from end group for Empatica):    Duration: {total_duration}")


    return time_stamp_for_peaks_empatica, duration_1, duration_2, total_duration


def minmaxscale(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


def get_acceleration_peak_time_from_empatica_df(folder_path, empatica_df):
    plots_path = folder_path + "Plots/"
    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    counter = 0
    x_tick_rotation = 45
    linewidth = 2.0
    alpha = 0.67

    #Empatica Acceleration
    ACC_X_EMPATICA = normalize_series(empatica_df["ACC_X_EMPATICA"])
    ACC_Y_EMPATICA = normalize_series(empatica_df["ACC_Y_EMPATICA"])
    ACC_Z_EMPATICA = normalize_series(empatica_df["ACC_Z_EMPATICA"])
    TimeStamp = empatica_df["TimeStamp"].copy()
    empatica_df_short = pd.concat([TimeStamp, ACC_X_EMPATICA, ACC_Y_EMPATICA, ACC_Z_EMPATICA], axis=1).reset_index() #concatentation of series

    counter = plotter(empatica_df_short, "TimeStamp", ["ACC_X_EMPATICA", "ACC_Y_EMPATICA", "ACC_Z_EMPATICA"], plots_path, counter, title="Normalized Acceleration for Empatica", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)

    #Empatica Acceleration Magnitude
    ACC_MAG_EMPATICA = normalize_series(empatica_df["Accel Mag"])

    TimeStamp = empatica_df["TimeStamp"].copy()
    empatica_mag_df = pd.concat([TimeStamp, ACC_MAG_EMPATICA], axis=1).reset_index()  # concatentation of series
    counter = plotter(empatica_mag_df, "TimeStamp", ["Accel Mag"], plots_path, counter, title="Normalized Acceleration Magnitude for Empatica (after jointly data stretching with zeros)", linewidth=linewidth, x_tick_rotation=x_tick_rotation, alpha=alpha)

    minimum_peak_height_start = 0.6
    maximum_peak_height_start = 1.0
    prominence_start = 0.5
    distance_start = 45
    start_offset = int(256 * 64)
    prominence_end = 0.3
    distance_end = 15
    minimum_peak_height_end = 0.65
    maximum_peak_height_end = 1.0
    end_offset = int(530 * 64)
    one_second_overall_srate = 64
    ten_minutes_beginning_time = one_second_overall_srate * 600
    # TODO: This was the old code, but I feel the removal of zeros is resulting in issues for me... acc_mag_empatica_array = minmaxscale(normalize_series(empatica_df["Accel Mag"]))
    acc_mag_empatica_array_start = minmaxscale(empatica_df["Accel Mag"][start_offset:start_offset+ten_minutes_beginning_time])
    print('TEST HERE')

    #peaks_prominance, _ = find_peaks(acc_mag_empatica_array_start,
    #                                 distance=distance_start,
    #                                 height=[minimum_peak_height_start, maximum_peak_height_start],
    #                                prominence=prominence_start)
    ## Adjust for the start_offset:
    #peaks_prominance += start_offset
    #plt.plot(acc_mag_empatica_array_start)
    #plt.plot(peaks_prominance, acc_mag_empatica_array_start[peaks_prominance], 'vg')
    #ticks = np.arange(start_offset, start_offset + ten_minutes_beginning_time, one_second_overall_srate)
    ##tick_labels = np.arange(start_offset, start_offset + (ten_minutes_beginning_time / 64), one_second_overall_srate / 64)
    #tick_labels = [str(datetime.strptime(d[:26], '%Y-%m-%d %H:%M:%S.%f'))[10:22] for d in [empatica_df["TimeStamp"].iloc[x] for x in ticks]]
    #plt.xticks(ticks, tick_labels, rotation=90)
    #plt.show()

    peaks_start, properties_start = find_peaks(acc_mag_empatica_array_start,
                                               distance=distance_start,
                                               height=[minimum_peak_height_start, maximum_peak_height_start],
                                               prominence=prominence_start)
    peaks_start += start_offset
    time_stamp_for_peaks_empatica_start = [empatica_df["TimeStamp"].iloc[x] for x in peaks_start]
    norm_acc_mag_for_peaks_start = [empatica_df["Accel Mag"].iloc[x] for x in peaks_start]
    print(F"time_stamp_for_peaks_empatica start: {time_stamp_for_peaks_empatica_start}")
    print(F"norm_acc_mag_for_peaks start: {norm_acc_mag_for_peaks_start}")

    #Manually remove peaks (first set slice of start peaks and then of end peaks)
    start_1 = 0
    end_1 = 8
    time_stamp_for_peaks_empatica_1 = time_stamp_for_peaks_empatica_start[start_1:end_1]
    norm_acc_mag_for_peaks_1 = norm_acc_mag_for_peaks_start[start_1:end_1]
    peaks_1 = peaks_start[start_1:end_1]

    # Now, take care of the end synchronization tapping group
    acc_mag_empatica_array_end = minmaxscale(empatica_df["Accel Mag"][-ten_minutes_beginning_time:])

    #peaks_prominance, _ = find_peaks(acc_mag_empatica_array_end[end_offset:],
    #                                 distance=distance_end,
    #                                 height=[minimum_peak_height_end, maximum_peak_height_end],
    #                                 prominence=prominence_end)
    ### Adjust for the start_offset:
    #peaks_prominance += len(empatica_df) - ten_minutes_beginning_time + end_offset
    #plt.plot(acc_mag_empatica_array_end)
    #plt.plot(peaks_prominance, acc_mag_empatica_array_end[peaks_prominance], 'vg')
    #ticks = np.arange(len(empatica_df) - ten_minutes_beginning_time, len(empatica_df), one_second_overall_srate)
    ##tick_labels = np.arange(start_offset, start_offset + (ten_minutes_beginning_time / 64), one_second_overall_srate / 64)
    #tick_labels = [str(datetime.strptime(d[:26], '%Y-%m-%d %H:%M:%S.%f'))[10:22] for d in [empatica_df["TimeStamp"].iloc[x] for x in ticks]]
    #plt.xticks(ticks, tick_labels, rotation=90)
    #plt.show()

    peaks_end, properties_end = find_peaks(acc_mag_empatica_array_end[end_offset:],
                                           distance=distance_end,
                                           height=[minimum_peak_height_end, maximum_peak_height_end],
                                           prominence=prominence_end)
    peaks_end += len(empatica_df) - ten_minutes_beginning_time + end_offset
    time_stamp_for_peaks_empatica_end = [empatica_df["TimeStamp"].iloc[x] for x in peaks_end]
    norm_acc_mag_for_peaks_end = [empatica_df["Accel Mag"].iloc[x] for x in peaks_end]
    print(F"time_stamp_for_peaks_empatica end: {time_stamp_for_peaks_empatica_end}")
    print(F"norm_acc_mag_for_peaks end: {norm_acc_mag_for_peaks_end}")

    #Manually remove peaks (first set slice of start peaks and then of end peaks)
    start_2 = 0
    end_2 = 8 #use 'None' to slice till the end (-1 is 1 before the last element)
    time_stamp_for_peaks_empatica_2 = time_stamp_for_peaks_empatica_end[start_2:end_2]
    norm_acc_mag_for_peaks_2 = norm_acc_mag_for_peaks_end[start_2:end_2]
    peaks_2 = peaks_end[start_2:end_2]

    #Combine slices from start and end
    time_stamp_for_peaks_empatica = []
    norm_acc_mag_for_peaks = []
    peaks = []

    time_stamp_for_peaks_empatica.extend(time_stamp_for_peaks_empatica_1)
    time_stamp_for_peaks_empatica.extend(time_stamp_for_peaks_empatica_2)

    norm_acc_mag_for_peaks.extend(norm_acc_mag_for_peaks_1)
    norm_acc_mag_for_peaks.extend(norm_acc_mag_for_peaks_2)

    peaks.extend(peaks_1)
    peaks.extend(peaks_2)

    num_peaks_found = len(norm_acc_mag_for_peaks)
    print(F"num peaks found: {num_peaks_found}")
    print(F"time_stamp_for_peaks_empatica: {time_stamp_for_peaks_empatica}")
    print(F"norm_acc_mag_for_peaks: {norm_acc_mag_for_peaks}")

    if num_peaks_found != 16:
        raise Exception(F"Found {num_peaks_found} acceleration peaks instead of the required 16 for Empatica.")

    time_stamp_for_peaks_empatica = [datetime.strptime(x[:26], '%Y-%m-%d %H:%M:%S.%f') for x in time_stamp_for_peaks_empatica]


    start_timestamp = time_stamp_for_peaks_empatica[0]
    end_timestamp = time_stamp_for_peaks_empatica[-1]
    print(F"Total Duration between first and last peak:   {end_timestamp - start_timestamp}")

    start_timestamp_grp_1 = time_stamp_for_peaks_empatica[0]
    end_timestamp_grp_1 = time_stamp_for_peaks_empatica[7]
    duration_1 = end_timestamp_grp_1-start_timestamp_grp_1
    print(F"***GROUP_1:    Duration: {duration_1}    |    peak_start_timestamp: {start_timestamp_grp_1}    |    peak_end_timestamp: {end_timestamp_grp_1}")

    start_timestamp_grp_2 = time_stamp_for_peaks_empatica[8]
    end_timestamp_grp_2 = time_stamp_for_peaks_empatica[15]
    duration_2 = end_timestamp_grp_2-start_timestamp_grp_2
    print(F"***GROUP_2:    Duration: {duration_2}    |    peak_start_timestamp: {start_timestamp_grp_2}    |    peak_end_timestamp: {end_timestamp_grp_2}")

    total_duration = time_stamp_for_peaks_empatica[8] - time_stamp_for_peaks_empatica[7]
    print(F"***TOTAL DURATION between start and end of space press (so time between last tap from the start group and first tap from end group for Empatica):    Duration: {total_duration}")

    return time_stamp_for_peaks_empatica, duration_1, duration_2, total_duration
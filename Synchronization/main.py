import sys
from datetime import timedelta, datetime
import devicely  # https://pypi.org/project/devicely/
import numpy as np
import pandas as pd
import jointly
from Jointly_muse import __merge_data_with_jointly, normalize
import sync_acceleration_peak_extractor
import psychopy_csv_log_parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import csv


def empatica_reader(path_to_empatica_files, timeshift=0, write_files=False):
    string = "-> Empatica Summary: \n"
    empatica_reader = devicely.EmpaticaReader(path_to_empatica_files)
    string = string + F"    Start Times: {empatica_reader.start_times} \n"
    string = string + F"    Sample Frequencies: {empatica_reader.sample_freqs} \n"
    string = string + F"Joined dataframe:\n {empatica_reader.data.head()}"
    empatica_reader.timeshift(timeshift)  # Shifts all time-values by amount given

    joined_path = None
    if write_files:
        empatica_reader.write(path_to_empatica_files)  # Write data
        joined_path = path_to_empatica_files + "/joined_DF.csv"
        empatica_reader.data.to_csv(joined_path, index=True, header=True,
                                    line_terminator='\n')
    return empatica_reader.data, string, joined_path


# Apparently empatica is 1 hour or 2 hours behind from current time Zone.

def add_2h_empatica(empatica_data, save_path, hour_addition_overwrite=2):
    if type(empatica_data) == str:
        df = pd.read_csv(empatica_data)
    elif type(empatica_data):
        df = empatica_data.copy(deep=True)
    else:
        return None
    list_timestamp_indexes = df.index.tolist()  
    list_timestamp_indexes = [x + timedelta(hours=hour_addition_overwrite) for x in list_timestamp_indexes]
    df.index = list_timestamp_indexes  
    return df


def drop_irregular_rows_and_interpolate_acceleration_data(path, new_file_path, num_columns=11):
    rows_new_csv = []

    encoding = ''
    try:
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            encoding = 'utf-8'
    except:
        with open(path, encoding='latin-1') as file:
            lines = file.readlines()
            encoding = 'latin-1'

    with open(path, encoding=encoding) as file:
        lines = file.readlines()
        aux = [i for i in lines if len(i.split(",")) <= num_columns]  
        for i in range(len(aux)):
            date_time_string = aux[i].split(",")[0]
            try:
                date_object = datetime.strptime(date_time_string, '%Y-%m-%d %H:%M:%S.%f')
                rows_new_csv.append(aux[i])
            except ValueError:
                continue
        rows_new_csv.insert(0,
                            'TimeStamp,Accelerometer_X,Accelerometer_Y,Accelerometer_Z,RAW_TP9,RAW_AF7,RAW_AF8,RAW_TP10,AUX_Right,Marker\n')
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            for item in rows_new_csv:
                # write each item on a new line
                new_file.write(item)

    return new_file_path


def muse_reader(path_to_muse_file, output_files_path, timeshift=0, write_files=True, csv_from_muse_streaming=False):
    string = "-> Muse S (headband) Summary: \n"
    rest_of_DF_path_for_straming_muse = None

    muse_reader = devicely.MuseReader(path_to_muse_file)

    string = string + F"{muse_reader.data.head()}"
    muse_reader.timeshift(timeshift)  # Shifts all time-values by amount given

    if write_files:
        muse_reader.write(output_files_path)
    return muse_reader.data, string, output_files_path, rest_of_DF_path_for_straming_muse

# to sort rows by index (since some time index are between other values maybe because muse had package loss or delay in streaming)
def add_miliseconds_muse(muse_data, save_path):
    if type(muse_data) == str:
        df = pd.read_csv(muse_data)
    elif type(muse_data):
        df = muse_data.copy(deep=True)
    else:
        return None

    df = df.sort_index(
        ascending=True)  
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
    df.to_csv(save_path)
    return df


def interpolate_rows(dataframe, save_file_path,
                     columns_of_interest=('RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10', 'BVP', 'EDA', 'HR', 'TEMP')):
    df = dataframe.copy(deep=True)
    interpolation_method = 'linear'  # nearest, linear, zero  
    for i in columns_of_interest:
        df.loc[df[i] == 0, i] = np.NaN
        df[i] = pd.to_numeric(df[i])
        df[i] = df[i].interpolate(method=interpolation_method)
        df[i] = df[i].fillna(
            method='backfill')  # fill na fields at the start (that were not interpolated with the previous method)

    df.to_csv(save_file_path)
    return df


def drop_na(dataframe, save_file_path,
            columns_of_interest=('RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10', 'BVP', 'EDA', 'HR', 'TEMP')):
    df = dataframe.copy(deep=True)
    for i in columns_of_interest:
        df.loc[df[i] == 0, i] = np.NaN

    df = df.dropna(axis=0, how='any', subset=columns_of_interest)
    df.to_csv(save_file_path)
    return df

def extract_physiological_signals_for_task(task, task_dates, empatica, muse,
                                           implicit_additional_timedelta=timedelta(seconds=5)):
    task_name = task
    empatica_extracted = empatica.query("'%s' <= TimeStamp <= '%s'" % (task_dates[0], task_dates[1]))
    if not  muse.empty: 
        muse_extracted = muse.query("'%s' <= TimeStamp <= '%s'" % (task_dates[0], task_dates[1]))
    else:
        muse_extracted = pd.DataFrame()
    return task_name, empatica_extracted, muse_extracted


def trim_physiological_signal_to_desired_duration_by_cutting_end_off(duration_in_seconds, column_name_srate_tuples, df):
    import math
    individual_signals_in_respective_sampling_rates = []
    for column_name_srate_tuple in column_name_srate_tuples:
        column_name = column_name_srate_tuple[0]
        srate = column_name_srate_tuple[1]
        jumping_factor = column_name_srate_tuple[2]
        if len(df.index) == 0:
            print("SOME ISSUE HERE WITH %s as the index has length of zero. Set trim_start to 0!" % column_name)
            starting_value_idx = 0
        else:
            starting_value_idx = df.index[0]
            for i in df.index:
                import numbers
                if not ((isinstance(df.loc[i, column_name], numbers.Number)) and math.isnan(df.loc[i, column_name])):
                    starting_value_idx = i
                    break
        try:
            temp_values_series = df.loc[starting_value_idx::jumping_factor, column_name]
        except KeyError as ke:
            print('KeyError appeared. Message: %s. Debug if need be. Should run with duplicate-removal solution.' % ke)
            dt = pd.to_datetime(df.index, format='%Y-%M-%D %H:%M:%S')
            delta = pd.to_timedelta(df.groupby(dt).cumcount(), unit='ms')
            df.index = dt + delta.values
            temp_values_series = df.loc[starting_value_idx::jumping_factor, column_name]
        temp_values_series.dropna(inplace=True)
        if len(temp_values_series) >= (duration_in_seconds * srate):
            temp_values_series = temp_values_series[:duration_in_seconds * srate]
        elif len(temp_values_series) < (duration_in_seconds * srate):
            print('ATTENTION! TASK %s! SOMEHOW THERE IS TOO FEW SAMPLES IN THE COLUMN %s FOR DURATION %d AND SRATE %d'
                  % (task_name, column_name, duration_in_seconds, srate))
            print('THEREFORE, DF IS NOT TRIMMED BUT STORED WITH ACTUAL LENGTH, WHICH IS APPROXIMATELY %d SECONDS...'
                  % int(len(temp_values_series) / srate))
        column_with_values = [column_name, temp_values_series]
        individual_signals_in_respective_sampling_rates.append(column_with_values)
    return individual_signals_in_respective_sampling_rates


def pickle_individual_signals_trimmed(path, data_to_pickle):

    for data_tuple in data_to_pickle:
        data_tuple[1].to_pickle(path + ('_%s.pickle' % data_tuple[0]))


def create_storage_folder_for_task_data(folder_path):
    import os
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


if __name__ == '__main__':
    print()

    manual_peak_alignment_check = False
    automated_joining_and_computation_of_offset = False
    manual_joining_based_on_acceleration_peaks = False
    simplest_wild_data_synchronization = False
    timestamp_based_synchronization_for_special_lab_cases = False

    empatica_column_name_srate_tuples = [
        ['ACC_X_EMPATICA', 32, 2],
        ['ACC_Y_EMPATICA', 32, 2],
        ['ACC_Z_EMPATICA', 32, 2],
        ['BVP', 64, 1],
        ['EDA', 4, 16],
        ['HR', 1, 64],
        ['TEMP', 4, 16],
        ['Accel Mag', 32, 2]
    ]
    muse_column_name_srate_tuples = [
        ['RAW_TP9', 256, 1],
        ['RAW_AF7', 256, 1],
        ['RAW_AF8', 256, 1],
        ['RAW_TP10', 256, 1],
        ['ACC_X_MUSE', 256, 1],  # Original ACC and Gyro from Muse have 52 Hz but Mind monitor saves the data at 256 Hz
        ['ACC_Y_MUSE', 256, 1],  
        ['ACC_Z_MUSE', 256, 1],  
        ['Gyro_X', 256, 1],  
        ['Gyro_Y', 256, 1],  
        ['Gyro_Z', 256, 1],  
        ['Accel Mag', 256, 1] 
    ]

    data_alignment_jobs = [
        # ["participant/Session/", "Muse.csv",
        # "Psychopy.csv", 0 , 0 , -0, -0],
    ]
       # The new data:
        # THE ORDER OF THE INDICES IS THE FOLLOWING: MUSE_START_MAX, EMPATICA_START_MAX, MUSE_END_MIN, EMP_END_MIN!!!
    two_empatica_recordings = False
    for data_alignment_job in data_alignment_jobs:
        base_path = './UNIVERSE/data/'
        participant_and_session = data_alignment_job[0]
        participant_data_path = base_path + data_alignment_job[0]

        output_folder = participant_data_path

        # General paths, derived the same way for both
        empatica_files_path = participant_data_path + "Empatica/"
        if two_empatica_recordings:
            empatica_files_path_1st = empatica_files_path + data_alignment_job[-2]
            empatica_files_path_2nd = empatica_files_path + data_alignment_job[-1]
        muse_file_path = participant_data_path + "Muse/" + data_alignment_job[1]
        muse_output_file_path = muse_file_path + "_NEW.csv"
        psychopy_log_path = participant_data_path + "Psychopy/" + data_alignment_job[2]
        merged_df_path = output_folder


        muse_data_from_streaming = False
        unused_columns = ['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10',
                          'Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10',
                          'Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10',
                          'Beta_TP9', 'Beta_AF7', 'Beta_AF8', 'Beta_TP10',
                          'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10',
                          'Battery', 'Elements'
                          ]

        # Empatica E4
        if not two_empatica_recordings:
            dataframe_empatica, output_string_empatica, path_empatica_joined = empatica_reader(empatica_files_path,
                                                                                               timeshift=0,
                                                                                               write_files=False)
        else:
            dataframe_empatica_1st, output_string_empatica, path_empatica_joined = \
                empatica_reader(empatica_files_path_1st, timeshift=0, write_files=False)
            dataframe_empatica_2nd, _, _ = empatica_reader(empatica_files_path_2nd, timeshift=0, write_files=False)
            first_timestamp_1st_recording = dataframe_empatica_1st.iloc[:, 6].first_valid_index()
            last_timestamp_1st_recording = dataframe_empatica_1st.index[-1]
            first_timestamp_2nd_recording = dataframe_empatica_2nd.iloc[:, 6].first_valid_index()
            last_timestamp_2nd_recording = dataframe_empatica_2nd.iloc[:, 6].last_valid_index()
            print('Duration First Recording: %s' % (last_timestamp_1st_recording - first_timestamp_1st_recording))
            print('Duration Second Recording: %s' % (last_timestamp_2nd_recording - first_timestamp_2nd_recording))
            print('Last Timestamp first recording: %s' % last_timestamp_1st_recording)
            print('First Timestamp second recording: %s' % first_timestamp_2nd_recording)
            print('Time missing between both recordings: %s' %
                  (first_timestamp_2nd_recording - last_timestamp_1st_recording))
            measurements_per_second_in_empaticas = 64
            entries_to_fill_in = int((first_timestamp_2nd_recording - last_timestamp_1st_recording).total_seconds() * \
                                     measurements_per_second_in_empaticas)
            print('AMOUNT OF NaN-VALUES TO INSERT BETWEEN THE RECORDINGS: %d' % int(entries_to_fill_in))
            empatica_to_fill_in_between = pd.DataFrame().reindex_like(dataframe_empatica_1st)
            empatica_to_fill_in_between.drop(
                empatica_to_fill_in_between.index[
                    list(range(entries_to_fill_in, len(dataframe_empatica_1st)))
                ], inplace=True, errors='raise')
            new_timestamps = [last_timestamp_1st_recording + (i * (timedelta(seconds=1) / 64))
                              for i in range(1, entries_to_fill_in)]
            empatica_to_fill_in_between = empatica_to_fill_in_between.reindex(new_timestamps)
            dataframe_empatica_temp = dataframe_empatica_1st.append(empatica_to_fill_in_between)
            dataframe_empatica = dataframe_empatica_temp.append(dataframe_empatica_2nd)

            print('ATTENTION!!! NEEDING TO ADJUST SOME CODE HERE! THE PATH TO STORE THE MERGED DATA!!!')
            raise Exception('ATTENTION!!! NEEDING TO ADJUST SOME CODE HERE! THE PATH TO STORE THE MERGED DATA!!!')
            temp_test_folder_for_storage = ''

            import calendar

            unix_time_str = ' %s' % calendar.timegm(dataframe_empatica[::2].index[0].timetuple())

            srate_ACC = ' %s' % 32
            srate_BVP = ' %s' % 64
            srate_EDA = ' %s' % 4
            srate_HR = ' %s' % 1
            srate_TEMP = ' %s' % 4
            first_row = pd.DataFrame(
                {'ACC_X': unix_time_str, 'ACC_Y': unix_time_str, 'ACC_Z': unix_time_str, 'BVP': unix_time_str,
                 'EDA': unix_time_str, 'HR': unix_time_str, 'TEMP': unix_time_str}, index=[0])
            second_row = pd.DataFrame(
                {'ACC_X': srate_ACC, 'ACC_Y': srate_ACC, 'ACC_Z': srate_ACC, 'BVP': srate_BVP, 'EDA': srate_EDA,
                 'HR': srate_HR, 'TEMP': srate_TEMP}, index=[0])

            test_df_emp = pd.concat([first_row, second_row, dataframe_empatica[::2]]).reset_index(drop=True)
            test_df_emp.to_csv(temp_test_folder_for_storage+'ACC.csv',
                               columns=['ACC_X', 'ACC_Y', 'ACC_Z'], header=False, index=False)

            test_df_emp = pd.concat([first_row, second_row, dataframe_empatica[::1]]).reset_index(drop=True)
            test_df_emp.to_csv(temp_test_folder_for_storage+'BVP.csv',
                               columns=['BVP'], header=False, index=False)

            test_df_emp = pd.concat([first_row, second_row, dataframe_empatica[::16]]).reset_index(drop=True)
            test_df_emp.to_csv(temp_test_folder_for_storage+'EDA.csv',
                               columns=['EDA'], header=False, index=False)

            test_df_emp = pd.concat([first_row, second_row, dataframe_empatica[::16]]).reset_index(drop=True)
            test_df_emp.to_csv(temp_test_folder_for_storage+'TEMP.csv',
                               columns=['TEMP'], header=False, index=False)

            test_df_emp = pd.concat([first_row, second_row, dataframe_empatica[::64]]).reset_index(drop=True)
            test_df_emp.to_csv(temp_test_folder_for_storage+'HR.csv',
                               columns=['HR'], header=False, index=False)

            print('Merged the empatica files with the correct sampling rate and stored them properly')

        print(output_string_empatica)
        print()
        dataframe_empatica = add_2h_empatica(dataframe_empatica, save_path=path_empatica_joined)

        # Muse S (Headband)
        dataframe_muse, output_string_muse, path_muse_file, rest_of_DF_path_for_streaming_muse = muse_reader(
            muse_file_path, muse_output_file_path, timeshift=0, write_files=False,
            csv_from_muse_streaming=muse_data_from_streaming
        )

        print(output_string_muse)
        print()
        if not muse_data_from_streaming:
            dataframe_muse = add_miliseconds_muse(dataframe_muse, save_path=path_muse_file)  # TODO: Check if necessary
            # print(dataframe_muse)

        dataframe_muse = dataframe_muse.drop(columns=unused_columns)
        print(dataframe_muse)
        
        ####### especial stretched files for UN_117 ############
        
        
        session_id = data_alignment_jobs[0][0].split("/")[1]
        if (participant_id == '') and (session_id == ''):
            dataframe_empatica = dataframe_empatica[dataframe_muse.index.min():]
            dataframe_empatica ["Accel Mag"] = jointly.helpers.calculate_magnitude(dataframe_empatica, ["ACC_X", "ACC_Y", "ACC_Z"])
            dataframe_empatica.rename(columns={'ACC_X': 'ACC_X_EMPATICA', 'ACC_Y': 'ACC_Y_EMPATICA', 'ACC_Z': 'ACC_Z_EMPATICA'}, inplace=True)
            dataframe_muse["Accel Mag"] = jointly.helpers.calculate_magnitude(dataframe_muse, ["Accelerometer_X", "Accelerometer_Y", "Accelerometer_Z"])
            dataframe_muse.rename(columns={'Accelerometer_X': 'ACC_X_MUSE', 'Accelerometer_Y': 'ACC_Y_MUSE', 'Accelerometer_Z': 'ACC_Z_MUSE'}, inplace=True)
            dataframe_empatica.to_csv( participant_data_path+"stretched_empatica.csv", index= True)
            dataframe_muse.to_csv( participant_data_path+"stretched_muse.csv", index= True)

        if (participant_id == '') and (session_id == ''):  
            dataframe_muse["Accel Mag"] = jointly.helpers.calculate_magnitude(dataframe_muse, ["Accelerometer_X", "Accelerometer_Y", "Accelerometer_Z"])
            dataframe_muse.rename(columns={'Accelerometer_X': 'ACC_X_MUSE', 'Accelerometer_Y': 'ACC_Y_MUSE', 'Accelerometer_Z': 'ACC_Z_MUSE'}, inplace=True)
            dataframe_muse.to_csv( participant_data_path+"stretched_muse.csv", index= True)

            start= max(dataframe_empatica.index.min(), dataframe_muse.index.min())
            end= max(dataframe_empatica.index.max(), dataframe_muse.index.max())
            frequency_hz = 64
            sampling_interval_seconds = 1 / frequency_hz
            pandas_freq_str = f'{int(sampling_interval_seconds * 1000)}L' 
            new_index = pd.date_range(start=dataframe_empatica.index.max(), end=dataframe_muse.index.max()+pd.Timedelta(minutes=1) , freq=pandas_freq_str)  # 'S' for second frequency, change if needed
            dataframe_empatica_extended = dataframe_empatica.reindex(new_index, fill_value=pd.NA)
            dataframe_empatica_extended = pd.concat([dataframe_empatica, dataframe_empatica_extended])
            first_minute_end = dataframe_empatica_extended.index[0] + pd.Timedelta(minutes=1)
            last_minute_start = dataframe_empatica_extended.index[-1] - pd.Timedelta(minutes=1)


            first_minute_data = dataframe_empatica_extended.loc[dataframe_empatica_extended.index[0]:first_minute_end, ['ACC_X', 'ACC_Y', 'ACC_Z']]
            first_minute_data = first_minute_data.resample(pandas_freq_str).ffill()


            last_minute_data_length = dataframe_empatica_extended.loc[last_minute_start:].shape[0]
            first_minute_data = first_minute_data.iloc[:last_minute_data_length]


            dataframe_empatica_extended.loc[last_minute_start:, ['ACC_X', 'ACC_Y', 'ACC_Z']] = first_minute_data.values

            dataframe_empatica_extended ["Accel Mag"] = jointly.helpers.calculate_magnitude(dataframe_empatica_extended, ["ACC_X", "ACC_Y", "ACC_Z"])
            dataframe_empatica_extended.rename(columns={'ACC_X': 'ACC_X_EMPATICA', 'ACC_Y': 'ACC_Y_EMPATICA', 'ACC_Z': 'ACC_Z_EMPATICA'}, inplace=True)
            dataframe_empatica_extended.index.name = 'TimeStamp'
            dataframe_empatica_extended.to_csv( participant_data_path+"stretched_empatica.csv", index= True)



        if manual_peak_alignment_check:
            print()


            mpl.use('Qt5Agg')

            dataframe_muse["Accel Mag"] = normalize(jointly.helpers.calculate_magnitude(
                dataframe_muse, ["Accelerometer_X", "Accelerometer_Y", "Accelerometer_Z"]).to_numpy())
            dataframe_empatica["Accel Mag"] = normalize(jointly.helpers.calculate_magnitude(
                dataframe_empatica, ["ACC_X", "ACC_Y", "ACC_Z"]).to_numpy())

            # Get the time_delta between when both data streams started, and align for the plot only, reset to 0
            time_delta = dataframe_empatica.index[0] - dataframe_muse.index[0]
            dataframe_muse.index -= dataframe_muse.index[0]
            dataframe_empatica.index -= dataframe_empatica.index[0]

            # If row-indices are needed, use these methods and plot using the row_count as x_value
            dataframe_muse['row_count'] = np.arange(len(dataframe_muse))
            dataframe_empatica['row_count'] = np.arange(len(dataframe_empatica))

            sampling_rate_muse = 256  
            sampling_rate_empatica = 64  
            muse_samples_second = sampling_rate_muse
            empatica_samples_second = sampling_rate_empatica
            ten_minutes_muse = muse_samples_second * 60 * 10
            ten_minutes_empatica = empatica_samples_second * 60 * 10

            # create ticks and labels for every two seconds
            empatica_ticks = np.arange(0, ten_minutes_empatica, empatica_samples_second * 2)
            muse_ticks = np.arange(0, ten_minutes_muse, muse_samples_second * 2)

            # start labels positive, end labels negative, as they describe the distance to respective start/end
            muse_labels_beginning = muse_ticks / sampling_rate_muse
            empatica_labels_beginning = empatica_ticks / sampling_rate_empatica
            muse_labels_end = (np.arange(ten_minutes_muse, 0, -(muse_samples_second * 2)) / sampling_rate_muse) * -1
            empatica_labels_end = (np.arange(ten_minutes_empatica, 0, -(empatica_samples_second * 2)) / sampling_rate_empatica) * -1

            muse_labels_beginning = muse_labels_beginning.astype(int)
            empatica_labels_beginning = empatica_labels_beginning.astype(int)
            muse_labels_end = muse_labels_end.astype(int)
            empatica_labels_end = empatica_labels_end.astype(int)

            # Plot the respective muse and empatica data streams
            plt.close('all')
            fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=False, sharey=False, figsize=(12, 8))
            import matplotlib

            start_time_empatica = 160
            end_time_empatica = 105
            start_time_muse = 1
            end_time_muse = 61
            length_plot_sample = 60
            font = {'family': 'normal',
                    'size': 12}
            matplotlib.rc('font', **font)
            ax1.plot(dataframe_empatica['row_count'][:ten_minutes_empatica],
                     dataframe_empatica["Accel Mag"][:ten_minutes_empatica],
                     label='Empatica Acc. Mag.', color='black')
            ax2.plot(dataframe_muse['row_count'][:ten_minutes_muse],
                     dataframe_muse["Accel Mag"][:ten_minutes_muse],
                     label='Muse Acc. Mag.', color='blue')
            ax3.plot(dataframe_empatica['row_count'][:ten_minutes_empatica],
                     dataframe_empatica["Accel Mag"][-ten_minutes_empatica:],
                     label='Empatica Acc. Mag.', color='black')
            ax4.plot(dataframe_muse['row_count'][:ten_minutes_muse],
                     dataframe_muse["Accel Mag"][-ten_minutes_muse:],
                     label='Muse Acc. Mag.', color='blue')
            ax1.legend(loc='upper right')
            ax2.legend(loc='upper right')
            ax3.legend(loc='upper right')
            ax4.legend(loc='upper right')
            ax1.title.set_text('First Ten Minutes Empatica')
            ax2.title.set_text('First Ten Minutes Muse')
            ax3.title.set_text('Last Ten Minutes Empatica')
            ax4.title.set_text('Last Ten Minutes Muse')
            ax1.title.set_size(15)
            ax2.title.set_size(15)
            ax3.title.set_size(15)
            ax4.title.set_size(15)
            ax1.set_xticks(empatica_ticks)
            ax1.set_xticklabels(empatica_labels_beginning)
            ax1.set_xlabel('Seconds relative to the start of the recordings')
            ax1.set_ylabel('Magnitude')
            ax1.set_xlim([empatica_samples_second * start_time_empatica,
                          empatica_samples_second * (start_time_empatica + length_plot_sample)])
            ax1.set_ylim([-0.5, 1.5])
            ax2.set_xticks(muse_ticks)
            ax2.set_xticklabels(muse_labels_beginning)
            ax2.set_xlabel('Seconds relative to the start of the recordings')
            ax2.set_ylabel('Magnitude')
            ax2.set_xlim([muse_samples_second * start_time_muse,
                          muse_samples_second * (start_time_muse + length_plot_sample)])
            ax2.set_ylim([-0.5, 1.5])
            ax3.set_xticks(empatica_ticks)
            ax3.set_xticklabels(empatica_labels_end)
            ax3.set_xlabel('Seconds relative to the end of the recordings')
            ax3.set_ylabel('Magnitude')
            ax3.set_xlim([(empatica_samples_second * 600) - (empatica_samples_second * end_time_empatica),
                          (empatica_samples_second * 600) -
                          (empatica_samples_second * (end_time_empatica - length_plot_sample))])
            ax3.set_ylim([-0.5, 1.5])
            ax4.set_xticks(muse_ticks)
            ax4.set_xticklabels(muse_labels_end)
            ax4.set_xlabel('Seconds relative to the end of the recordings')
            ax4.set_ylabel('Magnitude')
            ax4.set_xlim([(muse_samples_second * 600) - (muse_samples_second * end_time_muse),
                          (muse_samples_second * 600) - (muse_samples_second * (end_time_muse - length_plot_sample))])
            ax4.set_ylim([-0.5, 1.5])
            matplotlib.rc('font', **font)
            matplotlib.rc('font', **font)
            import matplotlib.pylab as pylab

            params = {'legend.fontsize': 12,
                      'axes.labelsize': 12,
                      'axes.titlesize': 12,
                      'xtick.labelsize': 12,
                      'ytick.labelsize': 12}
            pylab.rcParams.update(params)
            pylab.rcParams.update(params)
            plt.tight_layout()
            # plt.suptitle(participant_and_session)
            Plot_Save_Path = base_path
            plt.savefig((base_path + 'acceleration_synchronization_example_%s.pdf')
                        % (participant_and_session.split('/')[1]), dpi=150)

        elif automated_joining_and_computation_of_offset:

            # Merge muse with empatica with jointly by detecting shakes
            # Initialize all starters and enders indices at +/- 10 minutes. Check in the plot and adjust after step 1.
            muse_start_seconds = data_alignment_job[3]
            empatica_start_seconds = data_alignment_job[4]
            muse_end_seconds = data_alignment_job[5]
            empatica_end_seconds = data_alignment_job[6]

            start_window_length = max(muse_start_seconds, empatica_start_seconds)
            end_window_length = min(muse_end_seconds, empatica_end_seconds)

            # Assume a shake was performed at least once a second, likely more. Check in the plot and adjust after step 1.
            # STANDARD IS: milliseconds_between_shakes = 500
            milliseconds_between_shakes = 500

            # Assume a minimum amount of shakes that were performed per synchronization step and are present per modality
            # STANDARD IS: amounts_of_shakes = 6
            amounts_of_shakes = 6

            # Assume a minimum height of peaks for acceleration magnitude. Check in the plot and adjust after step 1.
            # STANDARD IS: min_height = 0.6
            min_height = 0.6

            # Put all of these values derived in step 1 to the correct extractor instance
            extractor = jointly.ShakeExtractor()
            extractor.start_window_length = pd.Timedelta(seconds=start_window_length)
            extractor.end_window_length = pd.Timedelta(seconds=abs(end_window_length))
            extractor.distance = milliseconds_between_shakes
            extractor.min_length = amounts_of_shakes
            extractor.threshold = min_height

            print("**    Merging Empatica and Muse with Jointly (with shake detection)    **")
            stretched_data_dfs = __merge_data_with_jointly(dataframe_muse, dataframe_empatica, output_folder, extractor)
            print("**    Synchronization by means of accounting for time-shift done       **")
            print(F"Muse Dataframe After Stretching: \n {stretched_data_dfs[0].head()}")
            print(F"Empatica Dataframe After Stretching: \n {stretched_data_dfs[1].head()}")
            stretched_data_dfs[0].to_csv(merged_df_path + "stretched_muse.csv")
            stretched_data_dfs[1].to_csv(merged_df_path + "stretched_empatica.csv")
            print("**    Not merged Empatica and Muse with Jointly (with shake detection) **")
            print("**    Only stored stretched files which are accounted for peaks        **")

        elif manual_joining_based_on_acceleration_peaks:
            muse_stretched_path = participant_data_path + 'stretched_muse.csv'
            muse_stretched_df = pd.read_csv(muse_stretched_path)
            empatica_stretched_path = participant_data_path + 'stretched_empatica.csv'
            empatica_stretched_df = pd.read_csv(empatica_stretched_path)

            # First, get the PsychoPy Log File parsed, such that the distance that is needed for the individual empatica
            # presses and the respective distances can be properly assessed
            print()
            print("**    Parsing Psychopy Log File    **")

            is_csv_log_file = ".csv" in psychopy_log_path.split("Psychopy/")[1]

            log_results_dictionary = None

            # Call method either to extract from .csv or from .log file
            if is_csv_log_file:
                log_results_dictionary = psychopy_csv_log_parser.parse_psychopy_log(psychopy_log_path)
            else:
                log_results_dictionary = psychopy_csv_log_parser.parse_psychopy_log_file(psychopy_log_path)

            space_press_psychopy, duration_1_psychopy, duration_2_psychopy, total_duration_psychopy = \
                psychopy_csv_log_parser.get_sync_timestamps(log_results_dictionary)

            # Second, extract the rough emaptica timestamps for tapping the spacebar by extracting the required parameters
            # and manually tweaking the elements / parameters
            print()
            print("**    Detecting Empatica acceleration peaks (for synchronization with psychopy)    **")
            # Empatica Acceleration peak extractor
            space_press_empatica, duration_1_empatica, duration_2_empatica, total_duration_empatica = \
                sync_acceleration_peak_extractor.get_acceleration_peak_time_from_empatica_df(
                    output_folder, empatica_stretched_df
                )
            print("**       Detected Empatica acceleration peaks based on PsychoPy Log File Info      **")

            threshold = timedelta(seconds=5)  # 1.5
            if total_duration_empatica >= total_duration_psychopy:
                if (total_duration_empatica - total_duration_psychopy) > threshold:
                    raise ValueError(
                        F"Space press time difference between Empatica and Psychopy ({total_duration_empatica - total_duration_psychopy}) is greater than allowed ({threshold})")
                else:
                    print(
                        F"*** Difference of time between last space tap from the start group and first space tap from end group between Psychopy and Empatica is: {total_duration_empatica - total_duration_psychopy}")
                    reference_date_start_empatica = space_press_empatica[7]
                    reference_date_end_empatica = space_press_empatica[8]
                    reference_seconds_start_psychopy = space_press_psychopy[3]
                    reference_seconds_end_psychopy = space_press_psychopy[4]
            else:
                if (total_duration_psychopy - total_duration_empatica) > threshold:
                    raise ValueError(
                        F"Space press time difference between Empatica and Psychopy ({total_duration_psychopy - total_duration_empatica}) is greater than allowed ({threshold})")
                else:
                    print(
                        F"*** Difference of time between last space tap from the start group and first space tap from end group between Psychopy and Empatica is: {total_duration_psychopy - total_duration_empatica}")
                    reference_date_start_empatica = space_press_empatica[7]
                    reference_date_end_empatica = space_press_empatica[8]
                    reference_seconds_start_psychopy = space_press_psychopy[3]
                    reference_seconds_end_psychopy = space_press_psychopy[4]

            print()
            print(F"reference_date_start_empatica: {reference_date_start_empatica}")
            print(F"reference_date_end_empatica: {reference_date_end_empatica}")
            print(F"reference_seconds_start_psychopy: {reference_seconds_start_psychopy}")
            print(F"reference_seconds_end_psychopy: {reference_seconds_end_psychopy}")
            print(
                F"*** In psychopy, time '{reference_seconds_start_psychopy}' is considered the start point. Seconds are then added to the date '{reference_date_start_empatica}'")
            print()

            # Get task dates
            relax_video_name, relax_video_date = psychopy_csv_log_parser.get_relaxation_video_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy)

            eye_closing_name, eye_closing_date = psychopy_csv_log_parser.get_eye_closing_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy)

            arithmetix_easy_name, arithmetix_easy_date = psychopy_csv_log_parser.get_arithmetix_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            arithmetix_hard_name, arithmetix_hard_date = psychopy_csv_log_parser.get_arithmetix_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            n_back_trial_easy_name, n_back_trial_easy_date = psychopy_csv_log_parser.get_n_back_trial_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            n_back_trial_hard_name, n_back_trial_hard_date = psychopy_csv_log_parser.get_n_back_trial_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            n_back_easy_name, n_back_easy_date = psychopy_csv_log_parser.get_n_back_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            n_back_hard_name, n_back_hard_date = psychopy_csv_log_parser.get_n_back_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            stroop_trial_easy_name, stroop_trial_easy_date = psychopy_csv_log_parser.get_stroop_trial_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            stroop_trial_hard_name, stroop_trial_hard_date = psychopy_csv_log_parser.get_stroop_trial_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            stroop_easy_name, stroop_easy_date = psychopy_csv_log_parser.get_stroop_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            stroop_hard_name, stroop_hard_date = psychopy_csv_log_parser.get_stroop_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            sudoku_easy_name, sudoku_easy_date = psychopy_csv_log_parser.get_sudoku_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=True)

            sudoku_hard_name, sudoku_hard_date = psychopy_csv_log_parser.get_sudoku_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy,
                easy=False)

            nasa_name_list, nasa_date_list = psychopy_csv_log_parser.get_NASA_with_shifted_time(log_results_dictionary,
                                                                                                reference_date_start_empatica,
                                                                                                reference_seconds_start_psychopy)

            panas_name_list, panas_date_list = psychopy_csv_log_parser.get_PANAS_with_shifted_time(log_results_dictionary,
                                                                                                   reference_date_start_empatica,
                                                                                                   reference_seconds_start_psychopy)

            affective_slider_name_list, affective_slider_date_list = psychopy_csv_log_parser.get_affective_slider_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy)

            likert_name_list, likert_date_list = psychopy_csv_log_parser.get_likert_scale_with_shifted_time(
                log_results_dictionary,
                reference_date_start_empatica,
                reference_seconds_start_psychopy)

            name_list = []
            task_date_tuple_list = []
            # extend all lists together
            # For Tasks with no repetition, so unique throughout the experiment
            name_list.extend([relax_video_name, eye_closing_name, arithmetix_easy_name, arithmetix_hard_name,
                              n_back_trial_easy_name, n_back_trial_hard_name, n_back_easy_name, n_back_hard_name,
                              stroop_trial_easy_name, stroop_trial_hard_name, stroop_easy_name, stroop_hard_name])

            task_date_tuple_list.extend([relax_video_date, eye_closing_date, arithmetix_easy_date, arithmetix_hard_date,
                                         n_back_trial_easy_date, n_back_trial_hard_date, n_back_easy_date, n_back_hard_date,
                                         stroop_trial_easy_date, stroop_trial_hard_date, stroop_easy_date, stroop_hard_date])

            # Sudoku tasks
            name_list.extend([sudoku_easy_name, sudoku_hard_name])
            task_date_tuple_list.extend([sudoku_easy_date, sudoku_hard_date])

            # For tasks with repetitions throughout the experiment  ---- [IMPORTANT: questionnaires need to go at the end of the array!!]
            name_list_for_tasks_with_repetitions = [nasa_name_list, panas_name_list, affective_slider_name_list,
                                                    likert_name_list]
            date_list_for_tasks_with_repetitions = [nasa_date_list, panas_date_list, affective_slider_date_list,
                                                    likert_date_list]
            for i in range(len(name_list_for_tasks_with_repetitions)):
                name_list.extend(name_list_for_tasks_with_repetitions[i])
                task_date_tuple_list.extend(date_list_for_tasks_with_repetitions[i])

            print(F"[DEBUG]   name_list: {name_list} ")
            print(F"[DEBUG]   task_date_tuple_list: {task_date_tuple_list} ")

            numbered_task_labels_dictionary_for_plotting = {}  # Each name is converted to a number
            for i in range(len(name_list)):
                numbered_task_labels_dictionary_for_plotting[i] = name_list[i]

            for task in numbered_task_labels_dictionary_for_plotting:
                # we added 5 seconds padding, to ensure sufficient windows
                dates = task_date_tuple_list[task]
                task_name, empatica_extracted, muse_extracted = extract_physiological_signals_for_task(
                    numbered_task_labels_dictionary_for_plotting[task], dates, empatica_stretched_df, muse_stretched_df)
                print("NOW WORKING ON PROPERLY STORING DATA FOR TASK: %s" % task_name)


                # trim_physiological_signal_to_time
                # create a method to get the downsampled individual values from the respective data
                
                task_duration_in_seconds = (dates[1] - dates[0]).seconds
                individual_signals_trimmed_empatica = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                    task_duration_in_seconds, empatica_column_name_srate_tuples, empatica_extracted)
                individual_signals_trimmed_muse = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                    task_duration_in_seconds, muse_column_name_srate_tuples, muse_extracted)
                organized_data_path = 'organized_data/'
                storage_path = merged_df_path + organized_data_path + task_name

                # TODO: Store the respective data
                create_storage_folder_for_task_data(storage_path)
                pickle_individual_signals_trimmed(storage_path + '/empatica_', individual_signals_trimmed_empatica)
                pickle_individual_signals_trimmed(storage_path + '/muse_', individual_signals_trimmed_muse)

        print('DONE WITH PARTICIPANT %s' % participant_and_session)

    if simplest_wild_data_synchronization:

        participant_id = 'UN_XX'
        participant_session = 'Wild'
        base_path = 'UNIVERSE/data'
        participant_data_base_path = base_path % (participant_id, participant_id, participant_session)
        storage_path_simplest_extracted_data = base_path % (participant_id, participant_id, 'Labeled')


        UN_124_times_and_durations = [
                            [   ['eye-closing', '2022-09-12 16-10-00', 60],
                                ['nor_stress_hig_mw', '2022-09-12 16-11-00', 14 * 60], 
                                ['hig_stress_hig_mw', '2022-09-12 16-25-00', 22 * 60], 
                                ['hig_stress_hig_mw', '2022-09-12 16-47-00', 19 * 60]  #ends 17:06
                            ], 

                            ]
        UN_124_muse_csvs = [
                        [1, 'mindMonitor_2022-09-12--16-06-31.csv', 0],  
                     ]

         UN_123_times_and_durations = [
            
            [
                ['eye-closing', '2022-09-08 13-05-00', 60],
                ['low_stress_low_mw', '2022-09-08 13-06-00', 23 * 60],
                ['nor_stress_hig_mw', '2022-09-08 13-29-00', 21 * 60],
                ['low_stress_hig_mw', '2022-09-08 13-50-00', 21 * 60],
                ['vlw_stress_low_mw', '2022-09-08 14-11-00', 20 * 60],
                ['low_stress_hig_mw', '2022-09-08 14-31-00', 22 * 60],
                ['low_stress_hig_mw', '2022-09-08 14-53-00', 22 * 60] #13:05 to 15:15
                
            ],
            [
                ['eye-closing', '2022-09-08 17-59-00', 60],
                ['vlw_stress_nor_mw', '2022-09-08 18-00-00', 22 * 60],
                ['low_stress_low_mw', '2022-09-08 18-22-00', 21 * 60],
                ['vlw_stress_low_mw', '2022-09-08 18-43-00', 28 * 60], #17:59 to 19:11
            ],
            [
                ['eye-closing', '2022-09-09 13-14-00', 60],
                ['nor_stress_nor_mw', '2022-09-09 13-15-00', 23 * 60],
                ['low_stress_nor_mw', '2022-09-09 13-38-00', 24 * 60],
                ['low_stress_nor_mw', '2022-09-09 14-02-00', 29 * 60], # 13:14 to 14:31
            ]
        ]
        UN_123_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
        ]
        
        UN_121_times_and_durations = [
                            [   ['eye-closing', '2022-11-09 15-29-00', 60],
                                ['hig_stress_hig_mw', '2022-11-09 15-30-00', 43 * 60], #muse ends 16:13
                             ],  
                            [   
                                ['nor_stress_hig_mw', '2022-11-09 16-35-00', 31 * 60], # only empatica ends 17:06 
                            ],  

            
                            [   
                                ['eye-closing', '2022-11-09 19-59-00', 60],
                                ['low_stress_low_mw', '2022-11-09 20-00-00', 47 * 60], #ends 20:47
                            ], 

                            ]
        UN_121_muse_csvs = [
                        [1, 'Muse.csv', 0],
                        [2, 'no_muse_file.csv', 1],   
                        [3, 'Muse.csv', 2],     
                     ]

        UN_119_times_and_durations = [
            [
                ['eye-closing', '2022-09-14 08-37-00', 60],
                ['nor_stress_hig_mw', '2022-09-14 08-33-00', 40 * 60],
            ],
            [
                ['eye-closing', '2022-09-15 11-53-00', 60],
                ['nor_stress_hig_mw', '2022-09-15 11-52-00', 26 * 60],
                ['nor_stress_hig_mw', '2022-09-15 12-20-00', 20 * 60],
                ['nor_stress_hig_mw', '2022-09-15 12-40-00', 23 * 60],
                ['nor_stress_hig_mw', '2022-09-15 13-03-00', 27 * 60],
                ['nor_stress_hig_mw', '2022-09-15 13-30-00', 20 * 60]
            ],
            [
                ['eye-closing', '2022-09-17 16-37-00', 60],
                ['nor_stress_hig_mw', '2022-09-17 16-38-00', 49 * 60],
                ['nor_stress_hig_mw', '2022-09-17 17-27-00', 29 * 60], # 17:56
                            ],
            [
                ['nor_stress_hig_mw', '2022-09-20 21-55-00', 21 * 60],
                ['nor_stress_hig_mw', '2022-09-20 22-16-00', 30 * 60],
                ['nor_stress_hig_mw', '2022-09-20 22-36-00', 20 * 60]
            ]
        ]
        UN_119_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
        ]

        UN_117_times_and_durations = [
            [
                ['eye-closing', '2022-11-09 15-25-00', 60],
                ['hig_stress_hig_mw', '2022-11-09 15-26-00', 53 * 60]
            ],
            [
                ['eye-closing', '2022-11-09 18-13-00', 60],
                ['hig_stress_hig_mw', '2022-11-09 18-14-00', 56 * 60],
                ['low_stress_hig_mw', '2022-11-09 19-10-00', 49 * 60],                
            ],
            [
                ['eye-closing', '2022-11-10 18-11-00', 60],
                ['vlw_stress_nor_mw', '2022-11-10 18-12-00', 60 * 60],
                ['low_stress_nor_mw', '2022-11-10 19-10-00', 30 * 60],
                ['vlw_stress_nor_mw', '2022-11-10 19-42-00', 27 * 60],
            ],
            [
                ['eye-closing', '2022-11-10 21-15-00', 60],
                ['vlw_stress_hig_mw', '2022-11-10 21-16-00', 26 * 60], 
                ['vlw_stress_nor_mw', '2022-11-10 21-42-00', 28 * 60],
                ['vlw_stress_hig_mw', '2022-11-10 22-10-00', 28 * 60]
            ], # the questionnaire time is not mentioned. Took an average of the duration and distributed the time accordingly.

        ]
        UN_117_muse_csvs = [  
            [1, 'Muse.csv', 0],
            [2, 'no_muse_file', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
        ]
        
        UN_116_times_and_durations = [
            [
                ['eye-closing', '2022-09-23 14-04-00', 60],
                ['low_stress_vlw_mw', '2022-09-23 14-05-00', 62 * 60],
                ['vlw_stress_nor_mw', '2022-09-23 15-07-00', 17 * 60],
                ['vlw_stress_nor_mw', '2022-09-23 15-24-00', 17 * 60],
                ['nor_stress_vlw_mw', '2022-09-23 15-41-00', 22 * 60] #ends at 16:03
            ],
            [
                ['eye-closing', '2022-09-23 17-16-00', 60],
                ['vlw_stress_nor_mw', '2022-09-23 17-17-00', 15 * 60],
                ['vlw_stress_nor_mw', '2022-09-23 17-32-00', 18 * 60],
                ['vlw_stress_low_mw', '2022-09-23 17-50-00', 25 * 60], #ends 18:15
            ],
            [
                ['eye-closing', '2022-09-27 16-56-00', 60], #16:55
                ['low_stress_nor_mw', '2022-09-27 16-57-00', 23 * 60],
                ['low_stress_low_mw', '2022-09-27 17-20-00', 20 * 60],
                ['vlw_stress_low_mw', '2022-09-27 17-40-00', 26 * 60] #ends 18:06
            ]
        ]
        UN_116_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2]
        ]
        
        UN_115_times_and_durations = [
            [
                ['eye-closing', '2022-10-25 11-45-00', 60],
                ['low_stress_nor_mw', '2022-10-25 11-46-00', 31 * 60],
                ['low_stress_nor_mw', '2022-10-25 12-17-00', 29 * 60]
            ],
            [
                ['eye-closing', '2022-10-25 18-17-00', 60],
                ['vlw_stress_vlw_mw', '2022-10-25 18-18-00', 25 * 60],
                ['low_stress_low_mw', '2022-10-25 18-43-00', 35 * 60],                
            ],
            [
                ['eye-closing', '2022-10-26 10-53-00', 60],
                ['nor_stress_low_mw', '2022-10-26 10-54-00', 35 * 60],
                ['low_stress_hig_mw', '2022-10-26 11-29-00', 32 * 60],
                ['nor_stress_hig_mw', '2022-10-26 12-01-00', 35 * 60],
            ],
        
        ]
        UN_115_muse_csvs = [  
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
           
        ]
        
        UN_114_times_and_durations = [
            [
                ['vlw_stress_nor_mw', '2022-09-19 10-41-00', 31 * 60],
                ['eye-closing', '2022-09-19 11-12-00',  60],
                ['low_stress_nor_mw', '2022-09-19 11-13-00', 18 * 60],
                ['nor_stress_hig_mw', '2022-09-19 11-31-00', 19 * 60],
                ['nor_stress_hig_mw', '2022-09-19 11-50-00', 23 * 60]
            ],
            [
                ['low_stress_nor_mw', '2022-09-19 20-42-0', 21 * 60],
                ['eye-closing', '2022-09-19 21-03-0',  60],
                ['nor_stress_nor_mw', '2022-09-19 21-04-0', 27 * 60],     #end at 22:25 
                ['low_stress_low_mw', '2022-09-19 21-31-0', 26 * 60],
                ['hig_stress_hig_mw', '2022-09-19 21-57-0', 28 * 60],
            ],
            [
                ['eye-closing', '2022-09-22 09-23-00', 60],
                ['vlw_stress_low_mw', '2022-09-22 09-24-00', 20 * 60],
                ['low_stress_low_mw', '2022-09-22 09-44-00', 27 * 60],
                ['nor_stress_low_mw', '2022-09-22 10-11-00', 21 * 60],
                ['low_stress_hig_mw', '2022-09-22 10-32-00', 23 * 60], #end 11:21
                ['low_stress_hig_mw', '2022-09-22 10-55-00', 26 * 60],
            ],        
            [
                ['eye-closing', '2022-09-22 15-44-00', 60],
                ['nor_stress_hig_mw', '2022-09-22 15-45-00', 23 * 60],
                ['nor_stress_hig_mw', '2022-09-22 16-08-00', 23 * 60],
                ['low_stress_hig_mw', '2022-09-22 16-31-00', 25 * 60], #end 16:56
            ], 
        ]
        UN_114_muse_csvs = [  
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
           
        ]
        UN_113_times_and_durations = [
            [
                ['eye-closing', '2022-10-11 13-48-00', 60],
                ['nor_stress_low_mw', '2022-10-11 13-49-00', 24 * 60],
                ['hig_stress_nor_mw', '2022-10-11 14-13-00', 16 * 60],
                ['low_stress_nor_mw', '2022-10-11 14-29-00', 19 * 60],
                ['nor_stress_low_mw', '2022-10-11 14-48-00', 18 * 60]
            ],
            [
                ['eye-closing', '2022-10-12 16-50-00', 60],
                ['nor_stress_hig_mw', '2022-10-12 16-51-00', 19 * 60],
                ['nor_stress_hig_mw', '2022-10-12 17-10-00', 17 * 60],
                ['nor_stress_nor_mw', '2022-10-12 17-27-00', 16 * 60],
                ['hig_stress_nor_mw', '2022-10-12 17-27-00', 19 * 60]
            ],
            [  
                ['eye-closing', '2022-10-15 14-06-00', 60],
                ['vlw_stress_hig_mw', '2022-10-15 14-07-00', 20 * 60],
                ['nor_stress_hig_mw', '2022-10-15 14-27-00', 17 * 60],
                ['hig_stress_nor_mw', '2022-10-15 14-44-00', 17 * 60],
                ['nor_stress_hig_mw', '2022-10-15 15-01-00', 17 * 60],
                ['low_stress_hig_mw', '2022-10-15 15-18-00', 19 * 60]
            ]
        ]
        UN_113_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2]
        ]
        
        
        UN_112_times_and_durations = [
            [
                ['eye-closing', '2022-09-19 08-14-00',  60],
                ['low_stress_nor_mw', '2022-09-19 08-15-00', 23 * 60],
                ['low_stress_low_mw', '2022-09-19 08-38-00', 24 * 60],
                ['low_stress_low_mw', '2022-09-19 09-02-00', 20 * 60], #9:43
                ['low_stress_low_mw', '2022-09-19 09-22-00', 21 * 60] #9:43
            ],
        ]
        UN_112_muse_csvs = [  
            [1, 'museMonitor_2022-09-19--08-13-56_3675453714137371752.csv', 0],        
        ]
        
        UN_111_times_and_durations = [
            [
                ['eye-closing', '2022-11-21 12-29-00', 60],
                ['nor_stress_nor_mw', '2022-11-21 12-30-00', 10 * 60]
            ],
            [
                ['eye-closing', '2022-11-21 13-19-00', 60],
                ['nor_stress_low_mw', '2022-11-21 13-20-00', 30 * 60]
            ],
            [
                ['eye-closing', '2022-11-21 14-20-00', 60],
                ['hig_stress_hig_mw', '2022-11-21 14-21-00', 30 * 60]
            ],
            [
                ['eye-closing', '2022-11-22 09-14-00', 60],
                ['low_stress_low_mw', '2022-11-22 09-15-00', 31 * 60]
            ],
            [
                ['eye-closing', '2022-11-22 09-56-00', 60],
                ['low_stress_nor_mw', '2022-11-22 09-57-00', 28 * 60]
            ],
            [
                ['eye-closing', '2022-11-22 10-30-00', 60],
                ['nor_stress_hig_mw', '2022-11-22 10-31-00', 31 * 60]
            ],
            [
                ['eye-closing', '2022-11-22 11-15-00', 60],
                ['low_stress_low_mw', '2022-11-22 11-16-00', 31 * 60]
            ],
            [
                ['eye-closing', '2022-11-22 11-51-00', 60],
                ['nor_stress_low_mw', '2022-11-22 11-52-00', 30 * 60]
            ]
        ]
        UN_111_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
            [5, 'Muse.csv', 4],
            [6, 'Muse.csv', 5],
            [7, 'Muse.csv', 6],
            [8, 'Muse.csv', 7]
        ]
        
        UN_110_times_and_durations = [
            [
                ['eye-closing', '2022-09-26 17-23-00', 60],
                ['low_stress_nor_mw', '2022-09-26 17-24-00', 24*60],
                ['eye-closing', '2022-09-26 17-54-00', 60],
                ['low_stress_hig_mw', '2022-09-26 17-55-00', 19*60]
            ],
            [
                ['eye-closing', '2022-09-28 08-50-00', 60],
                ['low_stress_nor_mw', '2022-09-28 08-51-00', 20*60],
                ['eye-closing', '2022-09-28 09-11-00', 60],
                ['low_stress_nor_mw', '2022-09-28 09-12-00', 16*60],
                ['eye-closing', '2022-09-28 09-57-00', 60],
                ['nor_stress_hig_mw', '2022-09-28 09-58-00', 19*60],
                ['eye-closing', '2022-09-28 10-38-00', 60],
                ['nor_stress_nor_mw', '2022-09-28 10-39-00', 19*60],
                ['eye-closing', '2022-09-28 11-11-00', 60],
                ['low_stress_nor_mw', '2022-09-28 11-12-00', 19*60],
                ['eye-closing', '2022-09-28 11-40-00', 60],
                ['nor_stress_hig_mw', '2022-09-28 11-41-00', 19*60]
            ],
            [
                ['eye-closing', '2022-09-30 11-17-00', 60],
                ['low_stress_hig_mw', '2022-09-30 11-18-00', 22*60],
                ['eye-closing', '2022-09-30 11-45-00', 60],
                ['nor_stress_hig_mw', '2022-09-30 11-46-00', 19*60],
                ['eye-closing', '2022-09-30 12-15-00', 60],
                ['hig_stress_hig_mw', '2022-09-30 12-16-00', 19*60],
                ['eye-closing', '2022-09-30 12-39-00', 60]
            ],
            [
                ['eye-closing', '2022-10-06 10-00-00', 60],
                ['low_stress_nor_mw', '2022-10-06 10-01-00', 45 * 60],
                ['eye-closing', '2022-10-06 10-45-00', 60]
            ]
        ]
        UN_110_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3]
        ]

        
        UN_109_times_and_durations = [
            [
                ['eye-closing', '2022-11-08 15-28-00', 60],
                ['nor_stress_nor_mw', '2022-11-08 15-29-00', 32*60]
            ],
            [   # Unfortunately, here there is no muse data present
                ['eye-closing', '2022-11-13 22-40-00', 60],
                ['hig_stress_nor_mw', '2022-11-13 22-41-00', 19*60],
                ['hig_stress_hig_mw', '2022-11-13 23-01-00', 27*60],
                ['hig_stress_hig_mw', '2022-11-13 23-30-00', 35*60],
                ['nor_stress_nor_mw', '2022-11-14 00-07-00', 26*60],
                ['nor_stress_low_mw', '2022-11-14 00-35-00', 31*60]
            ],
            [
                ['eye-closing', '2022-11-15 15-44-00', 60],
                ['hig_stress_nor_mw', '2022-11-15 15-45-00', 15*60],
                ['hig_stress_nor_mw', '2022-11-15 16-01-00', 19*60],
                ['hig_stress_nor_mw', '2022-11-15 16-21-00', 15*60]
            ],
            [
                ['eye-closing', '2022-11-20 22-00-00', 60],
                ['nor_stress_hig_mw', '2022-11-20 22-01-00', 29*60],
                ['nor_stress_hig_mw', '2022-11-20 22-30-00', 25*60],
                ['low_stress_nor_mw', '2022-11-20 22-55-00', 50*60] #23:45
            ]
        ]
        UN_109_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'no_muse_file', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3]
        ]
    
    
        UN_108_times_and_durations = [
                            [   
                                ['eye-closing', '2022-10-20 09-42-00', 60],
                                ['vlw_stress_vlw_mw', '2022-10-20 09-43-00', 29 * 60]
                            ],
                            [   
                                ['eye-closing', '2022-10-24 15-40-00', 60],
                                ['nor_stress_nor_mw', '2022-10-24 15-41-00', 45 * 60]
                            ],
                            [  
                                ['eye-closing', '2022-10-25 15-19-00', 60],
                                ['nor_stress_nor_mw', '2022-10-25 15-20-00', 20 * 60]
                            ],
                            [  
                                ['eye-closing', '2022-10-25 17-28-00', 60],
                                ['hig_stress_hig_mw', '2022-10-25 17-29-00', 9 * 60]
                            ],
                            [  
                                ['eye-closing', '2022-10-26 10-56-00', 60],
                                ['hig_stress_nor_mw', '2022-10-26 10-57-00', 60 * 60]
                            ],
                            [   
                                ['eye-closing', '2022-10-26 16-14-00', 60],
                                ['nor_stress_nor_mw', '2022-10-26 16-15-00', 23 * 60]
                            ],
                            [   
                                ['eye-closing', '2022-10-27 10-55-00', 60],
                                ['nor_stress_nor_mw', '2022-10-27 10-56-00', 45 * 60]
                            ]
                        ]

        UN_108_muse_csvs = [
            [1, 'Muse.csv', 0],    # TODO: Both files roughly match
            [2,'Muse.csv', 1],    # TODO: Both files roughly match
            [3, 'Muse.csv', 2],    # TODO: Both files roughly match
            [4, 'Muse.csv', 3],    # TODO: Both files roughly match
            [5, 'Muse.csv', 4],    # TODO: Both files roughly match
            [6, 'Muse.csv', 5],    # TODO: Both files roughly match
            [7, 'no_muse_recording.csv', 6],
        ]

        UN_107_times_and_durations = [
            [
                ['eye-closing', '2022-10-17 22-10-00', 60],
                ['low_stress_hig_mw', '2022-10-17 22-11-00', 19*60],
                ['vlw_stress_nor_mw', '2022-10-17 22-36-00', 16*60],
                ['low_stress_nor_mw', '2022-10-17 23-00-00', 10*60],
                ['hig_stress_hig_mw', '2022-10-17 23-15-00', 23*60],
                ['hig_stress_hig_mw', '2022-10-17 23-41-00', 18*60]
            ],
            [
                ['nor_stress_hig_mw', '2022-10-22 01-24-00', 19 * 60],
                ['low_stress_nor_mw', '2022-10-22 01-45-00', 15 * 60],
                ['low_stress_vhg_mw', '2022-10-22 02-08-00', 22 * 60],
                ['hig_stress_hig_mw', '2022-10-22 02-33-00', 19 * 60],
                ['nor_stress_vhg_mw', '2022-10-22 02-56-00', 28 * 60]
            ]
        ]
        UN_107_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 3]
        ]
        
        
        UN_106_times_and_durations = [
            [
                ['eye-closing', '2022-11-13 19-05-00', 60],
                ['low_stress_vlw_mw', '2022-11-13 19-06-00', 16*60]
            ],
            [
                ['eye-closing', '2022-11-13 19-33-00', 60],
                ['hig_stress_low_mw', '2022-11-13 19-34-00', 34*60]
            ],
            [
                ['eye-closing', '2022-11-13 21-36-00', 60],
                ['nor_stress_low_mw', '2022-11-13 21-37-00', 29*60]
            ],
            [
                ['eye-closing', '2022-11-14 14-34-00', 60],
                ['nor_stress_hig_mw', '2022-11-14 14-35-00', 55*60]
            ],
            [
                ['eye-closing', '2022-11-14 23-30-00', 60],
                ['nor_stress_hig_mw', '2022-11-14 23-31-00', 75*60]
            ],
        ]
    
        UN_106_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
            [5, 'Muse.csv', 4]
        ]
        
        
        UN_105_times_and_durations = [
            [
                ['eye-closing', '2022-11-18 07-36-00', 60],
                ['vlw_stress_vlw_mw', '2022-11-18 07-37-00', 23* 60],
                ['vlw_stress_nor_mw', '2022-11-18 08-00-00', 46 * 60],
              
            ],
          [
                ['eye-closing', '2022-11-20 09-56-00', 60],
                ['vlw_stress_low_mw', '2022-11-20 09-57-00', 34* 60],
                ['vlw_stress_low_mw', '2022-11-20 10-31-00', 32 * 60],
                ['low_stress_vlw_mw', '2022-11-20 11-03-00', 33 * 60], #11:36
              
            ],
          [
                ['eye-closing', '2022-11-22 10-56-00', 60],
                ['low_stress_nor_mw', '2022-11-22 10-57-00', 48* 60],
                ['low_stress_hig_mw', '2022-11-22 11-45-00', 48 * 60], #12:33
              
            ],

        ]
        UN_105_muse_csvs = [  
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
           
        ]
        
        
        UN_104_times_and_durations = [
            [
                ['eye-closing', '2022-11-08 11-35-00', 60],
                ['nor_stress_nor_mw', '2022-11-08 11-36-00', 31*60]
            ],
            [
                ['eye-closing', '2022-11-08 13-44-00', 60],
                ['low_stress_nor_mw', '2022-11-08 13-45-00', 36*60]
            ],
            [
                ['eye-closing', '2022-11-09 12-46-00', 60],
                ['nor_stress_nor_mw', '2022-11-09 12-47-00', 29*60]
            ],
            [
                ['eye-closing', '2022-11-09 14-39-00', 60],
                ['hig_stress_nor_mw', '2022-11-09 14-40-00', 27*60]
            ],
            [
                ['eye-closing', '2022-11-10 13-36-00', 60],
                ['hig_stress_nor_mw', '2022-11-10 13-37-00', 39*60]
            ],
            [
                ['eye-closing', '2022-11-11 11-13-00', 60],
                ['nor_stress_hig_mw', '2022-11-11 11-14-00', 34*60]
            ],
            [
                ['eye-closing', '2022-11-11 12-11-00', 60],
                ['hig_stress_hig_mw', '2022-11-11 12-12-00', 40*60]
            ],
            [
                ['eye-closing', '2022-11-14 12-04-00', 60],
                ['hig_stress_hig_mw', '2022-11-14 12-05-00', 32*60]
            ]
        ]
        UN_104_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3, 'Muse.csv', 2],
            [4, 'Muse.csv', 3],
            [5, 'Muse.csv', 4],
            [6, 'Muse.csv', 5],
            [7, 'Muse.csv', 6],
            [8, 'Muse.csv', 7]
            
        ] 
        
        UN_102_times_and_durations = [
            [
                ['eye-closing', '2023-01-08 19-21-40', 60],
                ['hig_stress_hig_mw', '2023-01-08 19-22-40', 27.5 * 60]
            ],
            [
                ['eye-closing', '2023-01-08 20-48-00', 60],
                ['vlw_stress_low_mw', '2023-01-08 20-49-00', 34 * 60]
            ],
            [
                ['eye-closing', '2023-01-09 18-40-00', 60],
                ['vlw_stress_hig_mw', '2023-01-09 18-41-00', 34 * 60]
            ],
            [
                ['eye-closing', '2023-01-10 18-07-00', 60],
                ['nor_stress_hig_mw', '2023-01-10 18-08-00', 35 * 60]
            ],
            [
                ['eye-closing', '2023-01-12 17-14-00', 60],
                ['hig_stress_vhg_mw', '2023-01-12 17-15-00', 34 * 60]
            ],
            [
                ['eye-closing', '2023-01-13 18-44-00', 60],
                ['low_stress_hig_mw', '2023-01-13 18-45-00', 30 * 60]
            ]
        ]
        UN_102_muse_csvs = [
            [1, 'Muse.csv', 0],
            [2, 'Muse.csv', 1],
            [3,'Muse.csv', 2],
            [4, 'Muse.csv', 3],
            [5, 'Muse.csv', 4],
            [6, 'Muse.csv', 5]
        ]


        UN_101_times_and_durations = [
                            [   
                                ['eye-closing', '2023-05-27 16-30-00', 60],
                                ['low_stress_low_mw', '2023-05-27 16-31-00', 17 * 60],
                                ['low_stress_low_mw', '2023-05-27 16-48-00', 18 * 60],
                                ['low_stress_low_mw', '2023-05-27 17-06-00', 18 * 60],
                                ['low_stress_low_mw', '2023-05-27 17-24-00', 17 * 60],
                                ['nor_stress_nor_mw', '2023-05-27 17-41-00', 18 * 60],
                                ['nor_stress_nor_mw', '2023-05-27 17-59-00', 18 * 60],
                                ['nor_stress_nor_mw', '2023-05-27 18-17-00', 22 * 60] #ends 18:39
                            ],  
                            [   
                                ['eye-closing', '2023-05-31 11-25-00', 60],
                                ['vlw_stress_nor_mw', '2023-05-31 11-26-00', 19 * 60],
                                ['low_stress_nor_mw', '2023-05-31 11-45-00', 18 * 60],
                                ['nor_stress_hig_mw', '2023-05-31 12-03-00', 18 * 60],
                                ['nor_stress_nor_mw', '2023-05-31 12-21-00', 16 * 60],
                                ['nor_stress_nor_mw', '2023-05-31 12-37-00', 19 * 60], #ends 12:56
                            ],  
                            [  
                                ['eye-closing', '2023-05-31 17-34-00', 60],
                                ['nor_stress_nor_mw', '2023-05-31 17-35-00', 17 * 60],
                                ['hig_stress_hig_mw', '2023-05-31 17-52-00', 18 * 60],
                                ['hig_stress_hig_mw', '2023-05-31 18-10-00', 17 * 60],
                                ['nor_stress_hig_mw', '2023-05-31 18-27-00', 24 * 60], #ends 18:51
                            ],  
                            [   
                                ['eye-closing', '2023-06-01 08-41-00', 60],
                                ['vlw_stress_nor_mw', '2023-06-01 08-42-00', 16 * 60],
                                ['low_stress_hig_mw', '2023-06-01 08-58-00', 19 * 60],
                                ['low_stress_nor_mw', '2023-06-01 09-17-00', 17 * 60],
                                ['low_stress_nor_mw', '2023-06-01 09-34-00', 18 * 60],
                                ['low_stress_nor_mw', '2023-06-01 09-52-00', 18 * 60],
                                ['nor_stress_nor_mw', '2023-06-01 10-10-00', 22 * 60], #ends 10:32
                             ]   
                            ]
        UN_101_muse_csvs = [
                        [1, 'Muse.csv', 0],
                        [2, 'Muse.csv', 1],    
                        [3, 'Muse.csv', 2],      
                        [4,'Muse.csv', 3],     
                    ]

        unused_columns = ['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10', 'Theta_TP9', 'Theta_AF7', 'Theta_AF8',
                          'Theta_TP10', 'Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10', 'Beta_TP9', 'Beta_AF7',
                          'Beta_AF8', 'Beta_TP10', 'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10', 'Battery',
                          'Elements']

        data_time_counter = 0

        # TODO: This needs to be adjusted per participant change for ... csvs
        # TODO: Adjust this here so that we're using a collection that holds tuples of UN_X_muse_csvs and UN_X_times_a..
        ctr = -1
        for idx, muse_csv_info in enumerate(UN_X_muse_csvs):
            participant_session, muse_csv_name, times_and_durations_idx = muse_csv_info
            participant_data_base_path = base_path % (participant_id, participant_id, participant_session)
            empatica_data_path = participant_data_base_path + 'Empatica/'
            muse_data_path = participant_data_base_path + 'Muse/' + muse_csv_name

            # Empatica E4
            dataframe_empatica, _, _ = empatica_reader(empatica_data_path, timeshift=0, write_files=False)
            if ((participant_id == 'UN_111') or (participant_id == 'UN_109')
                    or (participant_id == 'UN_106') or (participant_id == 'UN_104')  or (participant_id == 'UN_102')):
                dataframe_empatica = add_2h_empatica(dataframe_empatica, save_path=None, hour_addition_overwrite=1)
            else:
                dataframe_empatica = add_2h_empatica(dataframe_empatica, save_path=None)

            # Muse S (Headband)
            dataframe_muse, _, _, _ = muse_reader(muse_data_path, None, timeshift=0, write_files=False)
            dataframe_muse = dataframe_muse.drop(columns=unused_columns)

            print('Now we would like to extract the following information for participant %s %s session:' %
                  (participant_id, participant_session))
            print('[Muse]: Session starting time %s and duration %s' % (dataframe_muse.index[0], dataframe_muse.index[-1] - dataframe_muse.index[0]))
            print('[Empatica]: Session starting time %s and duration %s' % (dataframe_empatica.index[0], dataframe_empatica.index[-1] - dataframe_empatica.index[0]))

            start_time_for_extraction = None
            overall_extraction_duration = 0

            # TODO: This needs to be adjusted per participant change for ... durations
            for session_data_to_be_extracted in UN_X_times_and_durations[times_and_durations_idx]:
                session_type, date, duration_in_seconds = session_data_to_be_extracted
                print('session %s on the %s with duration of %d seconds or %d minutes ...'
                      % (session_type, date, duration_in_seconds, int(duration_in_seconds/60)))

                # Break the execution if we don't have enough data from either one modality
                datetime_object_enddate = datetime.strptime(date, '%Y-%m-%d %H-%M-%S')
                datetime_object_enddate += timedelta(seconds=duration_in_seconds)
                end_timestamp = datetime_object_enddate

                if (end_timestamp >= dataframe_muse.index[-1]) or (end_timestamp >= dataframe_empatica.index[-1]):
                    break

                ctr += 1
                overall_extraction_duration += int(duration_in_seconds/60)
                if ctr == 0:
                    start_time_for_extraction = '%s' % date

                enddate_str = datetime_object_enddate.strftime('%Y-%m-%d %H-%M-%S')

                date = datetime.strptime(date, '%Y-%m-%d %H-%M-%S')
                enddate_str = datetime.strptime(enddate_str, '%Y-%m-%d %H-%M-%S') + timedelta(seconds=5)

                task_name, empatica_extracted, muse_extracted = extract_physiological_signals_for_task(
                    session_type, [date, enddate_str], dataframe_empatica, dataframe_muse
                )


                # That column would need to be re-computed based on ACC_X, ACC_Y, and ACC_Z respectively.
                empatica_column_name_srate_tuples = [
                    ['ACC_X', 32, 2],
                    ['ACC_Y', 32, 2],
                    ['ACC_Z', 32, 2],
                    ['BVP', 64, 1],
                    ['EDA', 4, 16],
                    ['HR', 1, 64],
                    ['TEMP', 4, 16]
                ]

                muse_column_name_srate_tuples = [
                    ['RAW_TP9', 256, 1],
                    ['RAW_AF7', 256, 1],
                    ['RAW_AF8', 256, 1],
                    ['RAW_TP10', 256, 1],
                    ['Accelerometer_X', 256, 1],  # 52
                    ['Accelerometer_Y', 256, 1],  # 52
                    ['Accelerometer_Z', 256, 1],  # 52
                    ['Gyro_X', 256, 1],  # 52
                    ['Gyro_Y', 256, 1],  # 52
                    ['Gyro_Z', 256, 1],  # 52
                    # ['HeadBandOn', 256],
                    # ['HSI_TP9', 256],
                    # ['HSI_AF7', 256],
                    # ['HSI_AF8', 256],
                    # ['HSI_TP10', 256]
                ]

                task_duration_in_seconds = (enddate_str - date).seconds
                individual_signals_trimmed_empatica = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                    task_duration_in_seconds, empatica_column_name_srate_tuples, empatica_extracted)
                individual_signals_trimmed_muse = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                    task_duration_in_seconds, muse_column_name_srate_tuples, muse_extracted)
                organized_data_path = 'organized_wild_data/'
                storage_path = storage_path_simplest_extracted_data + organized_data_path + task_name + '_' + str(data_time_counter)
                data_time_counter += 1

                # TODO: Store the respective data
                create_storage_folder_for_task_data(storage_path)
                pickle_individual_signals_trimmed(storage_path + '/empatica_', individual_signals_trimmed_empatica)
                pickle_individual_signals_trimmed(storage_path + '/muse_', individual_signals_trimmed_muse)

            print('For above session of durations %s and %s, we attempted to extract %d minutes starting at %s.' %
                  (dataframe_muse.index[-1] - dataframe_muse.index[0],
                   dataframe_empatica.index[-1] - dataframe_empatica.index[0],
                   overall_extraction_duration, start_time_for_extraction)
                  )

        print('TODO: Take care of the recordings where there is either no muse or no empatica data')
        print('TODO: For now, throw these data points away and dont consider them. Talk w. Sidratul about this.')
        print('Temporary stuff here')

    if timestamp_based_synchronization_for_special_lab_cases:
        #  modified version of the logs parser

        participant_id = 'UN_102'
        participant_session = '1'
        base_path = 'UNIVERSE/UN_102'
        participant_data_base_path = base_path
        output_folder = base_path
        merged_df_path = base_path
        storage_path_simplest_extracted_data = base_path + 'Labeled/'

        # Based on this file, we extracted the respective parts manually from the log
        participant_psychopy_log_file = 'Psychopy.log'
        psychopy_log_path = participant_data_base_path + "Psychopy/" + participant_psychopy_log_file

        unused_columns = ['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10', 'Theta_TP9', 'Theta_AF7', 'Theta_AF8',
                          'Theta_TP10', 'Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10', 'Beta_TP9', 'Beta_AF7',
                          'Beta_AF8', 'Beta_TP10', 'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10', 'Battery',
                          'Elements']

        data_time_counter = 0
        muse_stretched_path = participant_data_base_path + 'stretched_muse.csv'
        muse_stretched_df = pd.read_csv(muse_stretched_path)
        empatica_stretched_path = participant_data_base_path + 'stretched_empatica.csv'
        empatica_stretched_df = pd.read_csv(empatica_stretched_path)

        # First, get the PsychoPy Log File parsed, such that the distance that is needed for the individual empatica
        # presses and the respective distances can be properly assessed
        print()
        print("**    Parsing Psychopy Log File    **")

        is_csv_log_file = ".csv" in psychopy_log_path.split("Psychopy/")[1]

        log_results_dictionary = None

        # Call method either to extract from .csv or from .log file
        if is_csv_log_file:
            log_results_dictionary = psychopy_csv_log_parser.parse_psychopy_log(psychopy_log_path)
        else:
            log_results_dictionary = psychopy_csv_log_parser.parse_psychopy_log_file(
                psychopy_log_path, check_for_correct_tappings_number=False
            )

        space_press_psychopy, duration_1_psychopy = psychopy_csv_log_parser.get_sync_timestamps(
            log_results_dictionary, expecting_both_synchronization_trials=False
        )

        # Second, extract the rough emaptica timestamps for tapping the spacebar by extracting the required parameters
        # and manually tweaking the elements / parameters
        print()
        print("**    Detecting Empatica acceleration peaks (for synchronization with psychopy)    **")
        # Empatica Acceleration peak extractor
        space_press_empatica, duration_1_empatica, duration_2_empatica, total_duration_empatica = \
            sync_acceleration_peak_extractor.get_acceleration_peak_time_from_empatica_df(
                output_folder, empatica_stretched_df
            )
        print("**       Detected Empatica acceleration peaks based on PsychoPy Log File Info      **")

        reference_date_start_empatica = space_press_empatica[7]
        reference_seconds_start_psychopy = space_press_psychopy[3]

        # Get task dates
        relax_video_name, relax_video_date = psychopy_csv_log_parser.get_relaxation_video_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy)

        eye_closing_name, eye_closing_date = psychopy_csv_log_parser.get_eye_closing_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy)


        arithmetix_hard_name, arithmetix_hard_date = psychopy_csv_log_parser.get_arithmetix_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)

        n_back_trial_hard_name, n_back_trial_hard_date = psychopy_csv_log_parser.get_n_back_trial_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)


        n_back_hard_name, n_back_hard_date = psychopy_csv_log_parser.get_n_back_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)

        stroop_trial_easy_name, stroop_trial_easy_date = psychopy_csv_log_parser.get_stroop_trial_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=True)

        stroop_trial_hard_name, stroop_trial_hard_date = psychopy_csv_log_parser.get_stroop_trial_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)

        stroop_easy_name, stroop_easy_date = psychopy_csv_log_parser.get_stroop_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=True)

        stroop_hard_name, stroop_hard_date = psychopy_csv_log_parser.get_stroop_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)

        sudoku_easy_name, sudoku_easy_date = psychopy_csv_log_parser.get_sudoku_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=True)

        sudoku_hard_name, sudoku_hard_date = psychopy_csv_log_parser.get_sudoku_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy,
            easy=False)

        nasa_name_list, nasa_date_list = psychopy_csv_log_parser.get_NASA_with_shifted_time(log_results_dictionary,
                                                                                            reference_date_start_empatica,
                                                                                            reference_seconds_start_psychopy)

        panas_name_list, panas_date_list = psychopy_csv_log_parser.get_PANAS_with_shifted_time(log_results_dictionary,
                                                                                               reference_date_start_empatica,
                                                                                               reference_seconds_start_psychopy)

        affective_slider_name_list, affective_slider_date_list = psychopy_csv_log_parser.get_affective_slider_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy)

        likert_name_list, likert_date_list = psychopy_csv_log_parser.get_likert_scale_with_shifted_time(
            log_results_dictionary,
            reference_date_start_empatica,
            reference_seconds_start_psychopy)

        name_list = []
        task_date_tuple_list = []
        # extend all lists together
        # For Tasks with no repetition, so unique throughout the experiment
        name_list.extend([relax_video_name, eye_closing_name, arithmetix_hard_name,
                          n_back_trial_hard_name, n_back_hard_name,
                          stroop_trial_easy_name, stroop_trial_hard_name, stroop_easy_name, stroop_hard_name])

        task_date_tuple_list.extend([relax_video_date, eye_closing_date, arithmetix_hard_date,
                                     n_back_trial_hard_date, n_back_hard_date,
                                     stroop_trial_easy_date, stroop_trial_hard_date, stroop_easy_date,
                                     stroop_hard_date])

        # Sudoku tasks
        name_list.extend([sudoku_easy_name, sudoku_hard_name])
        task_date_tuple_list.extend([sudoku_easy_date, sudoku_hard_date])

        # For tasks with repetitions throughout the experiment  ---- [IMPORTANT: questionnaires need to go at the end of the array!!]
        name_list_for_tasks_with_repetitions = [nasa_name_list, panas_name_list, affective_slider_name_list,
                                                likert_name_list]
        date_list_for_tasks_with_repetitions = [nasa_date_list, panas_date_list, affective_slider_date_list,
                                                likert_date_list]
        for i in range(len(name_list_for_tasks_with_repetitions)):
            name_list.extend(name_list_for_tasks_with_repetitions[i])
            task_date_tuple_list.extend(date_list_for_tasks_with_repetitions[i])

        print(F"[DEBUG]   name_list: {name_list} ")
        print(F"[DEBUG]   task_date_tuple_list: {task_date_tuple_list} ")

        numbered_task_labels_dictionary_for_plotting = {}  # Each name is converted to a number
        for i in range(len(name_list)):
            numbered_task_labels_dictionary_for_plotting[i] = name_list[i]

        for task in numbered_task_labels_dictionary_for_plotting:
            dates = task_date_tuple_list[task]
            task_name, empatica_extracted, muse_extracted = extract_physiological_signals_for_task(
                numbered_task_labels_dictionary_for_plotting[task], dates, empatica_stretched_df, muse_stretched_df)
            print("NOW WORKING ON PROPERLY STORING DATA FOR TASK: %s" % task_name)

            task_duration_in_seconds = (dates[1] - dates[0]).seconds
            individual_signals_trimmed_empatica = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                task_duration_in_seconds, empatica_column_name_srate_tuples, empatica_extracted)
            individual_signals_trimmed_muse = trim_physiological_signal_to_desired_duration_by_cutting_end_off(
                task_duration_in_seconds, muse_column_name_srate_tuples, muse_extracted)
            organized_data_path = 'organized_data/'
            storage_path = merged_df_path + organized_data_path + task_name

            # TODO: Store the respective data
            create_storage_folder_for_task_data(storage_path)
            pickle_individual_signals_trimmed(storage_path + '/empatica_', individual_signals_trimmed_empatica)
            pickle_individual_signals_trimmed(storage_path + '/muse_', individual_signals_trimmed_muse)

        print('Took care of the participant for whom PsychoPy did not log all information')

    print('DONE')


import datetime
import traceback
from typing import List
import jointly
import pandas as pd
import logging
from jointly.log import logger
from jointly.types import SourceDict
import matplotlib as plt
import numpy as np


def normalize(x: List[float]):
    """Normalizes signal to interval [-1, 1] with mean 0."""
    if len(x) <= 1:
        raise ValueError("Cannot normalize list with less than 2 entries")
    x_centered = x - np.mean(x)
    x_maximum = np.max(np.abs(x_centered))
    if x_maximum == 0:
        raise ZeroDivisionError("input vector is all-zero")
    x_normalized = x_centered / x_maximum
    return x_normalized


def __plot_reference_columns(sources: SourceDict, title: str = "Normalized Acceleration Magnitude Graph", error=True, save_path=""): #Taken from jointly
    """
    Plots a normalized version of the reference columns, i.e., what jointly is detecting shakes on

    :param sources: a SourceDict
    :param title: additional title if desired
    """

    plt.pyplot.figure(f"Test Debug: {title}")

    for device in sources:
        ref_column = sources[device]["ref_column"]
        data = sources[device]["data"][ref_column].dropna()
        data = data[data != 0]
        data = pd.Series(normalize(data.values), data.index)
        plt.pyplot.plot(data.index, data, label=device)

    plt.pyplot.legend()
    plt.pyplot.title(title)



    if error:
        plt.pyplot.show()

        #Show graphs individually
        for device in sources:
            plt.pyplot.figure(f"Test Debug: {title}")
            ref_column = sources[device]["ref_column"]
            data = sources[device]["data"][ref_column].dropna()
            data = data[data != 0]
            data = pd.Series(normalize(data.values), data.index)
            plt.pyplot.plot(data.index, data, label=device)
            plt.pyplot.legend()
            plt.pyplot.title(title)
            plt.pyplot.show()

    else: #If there is no error, save graph instead of showing
        plt.pyplot.savefig(save_path, format='pdf')




# Merging with jointly: https://jointly.readthedocs.io/
def __merge_data_with_jointly(muse_df, empatica_df, output_folder_path, extractor):
    #Creating logger file
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.FileHandler(output_folder_path + 'jointly.log')
    logger_file_handler.setLevel(logging.DEBUG)
    logger.addHandler(logger_file_handler)



    global synched_data
    print(datetime.datetime.now(), "START MERGING MUSE AND EMPATICA DATA")

    #This stretch factor is used only to increase the data values of muse acceleration (x, y, z)
    muse_strechfactor_positive = 127 / max(muse_df['Accelerometer_X'].max(), muse_df['Accelerometer_Y'].max(), muse_df['Accelerometer_Z'].max())
    muse_strechfactor_negative = abs(128 / min(muse_df['Accelerometer_X'].min(), muse_df['Accelerometer_Y'].min(), muse_df['Accelerometer_Z'].min()))
    muse_stretchfactor = min(muse_strechfactor_positive, muse_strechfactor_negative)

    muse_df = muse_df.apply(lambda x: x * muse_stretchfactor if x.name == 'Accelerometer_X' or x.name == 'Accelerometer_Y' or x.name == 'Accelerometer_Z' else x)

    muse_df["Accel Mag"] = jointly.helpers.calculate_magnitude(muse_df, ["Accelerometer_X", "Accelerometer_Y", "Accelerometer_Z"])

    empatica_df["Accel Mag"] = jointly.helpers.calculate_magnitude(empatica_df, ["ACC_X", "ACC_Y", "ACC_Z"])

    sources = {
        "Muse": {
            "data": muse_df,
            "ref_column": "Accel Mag",
        },
        "Empatica": {
            "data": empatica_df,
            "ref_column": "Accel Mag",
        }
    }

    print(muse_df)
    print(empatica_df)



    synchronizer = jointly.Synchronizer(
        sources, reference_source_name="Muse", extractor=extractor
    )


    try:
        # get_synced_data returns a dictionary of sensor names to synced DataFrames
        print('sources before recalculation')
        print(sources)
        synched_data = synchronizer.get_synced_data(recalculate=True)
        print('sources after recalculation')
        print(sources)
        print('sources after recalculation. However, the original data is still not-stretched.')
        print('Stretched data is in synched_data and orignal sources are in sources["data"].')
        __plot_reference_columns(sources, error=False, save_path=output_folder_path + "acc_mag.pdf")
    except Exception:
        traceback.print_exc()
        __plot_reference_columns(sources, error=True)

    # handle the date after sync, which means essentially the stretched data
    muse_df_after_sync = synched_data['Muse']
    empatica_df_after_sync = synched_data['Empatica']

    muse_df_after_sync.rename(columns={'Accelerometer_X': 'ACC_X_MUSE', 'Accelerometer_Y': 'ACC_Y_MUSE', 'Accelerometer_Z': 'ACC_Z_MUSE'}, inplace=True)
    empatica_df_after_sync.rename(columns={'ACC_X': 'ACC_X_EMPATICA', 'ACC_Y': 'ACC_Y_EMPATICA', 'ACC_Z': 'ACC_Z_EMPATICA'}, inplace=True)
    return [muse_df_after_sync, empatica_df_after_sync]

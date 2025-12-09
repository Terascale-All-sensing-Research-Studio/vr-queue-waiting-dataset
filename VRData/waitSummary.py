import os
import pandas as pd
import statistics
import math

#Python function to convert floating point representations to two decimal places
def truncate_float_to_two_decimals(number):
    return math.trunc(number * 100) / 100

def process_csv_files(root_folder, timestamp_col_name='Timestamp(ns)'):
    """
    Loops through folders, processes CSV files, resamples nanosecond timestamps to seconds.

    Args:
        root_folder (str): The path to the root directory containing subfolders and CSV files.
    """

    samples_per_second_list = []

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            #Change csv filename below for each wait treatment. #The example below is for the 3-minute treatment. 
            #No wait: EyeGazeLog_NO_WAIT
            #3-minute wait: EyeGazeLog_3_MINUTE_WAIT
            #6-minute wait: EyeGazeLog_6_MINUTE_WAIT
            
            #To change eye, head, left hand, and right hand
            #Eye: EyeGazeLog
            #Head: HeadPositionLog
            #Left hand: LeftHandLog
            #Right hand: RightHandLog
            
            if filename.endswith("EyeGazeLog_3_MINUTE_WAIT.csv"):
                file_path = os.path.join(dirpath, filename)
                print(f"Processing file: {file_path}")

                try:
                    df = pd.read_csv(file_path, index_col= False)

                    df[timestamp_col_name] = pd.to_datetime(df[timestamp_col_name], unit = 'ns')

                    df = df.set_index(timestamp_col_name)

                    #Adjust the resampling frequency '1S' to calculate sumber of samples per second of correspnding sensor values
                    df_resampled = df.resample('1S').size()

                    df_resampled_without_index = df_resampled.values
                    participant_sps_mean = truncate_float_to_two_decimals(df_resampled_without_index.mean())
                    samples_per_second_list.append(participant_sps_mean)

                except Exception as e:
                    print(f"  Error processing {filename}: {e}")


    print("")
    print("Total number of average samples per second values for all participants: ", len(samples_per_second_list))

    #Calculate mean of list of average samples per second(sps) values calculated for each of 36 participants
    overall_mean = statistics.mean(samples_per_second_list)
    print("Mean of average samples per second values for all participants: ", truncate_float_to_two_decimals(overall_mean))

    #Calculate standard deviation of list of average samples per second(sps) values calculated for each of 36 participants
    overall_standard_deviation = statistics.stdev(samples_per_second_list)
    print("Standard deviation of samples per second values for all participants: ", truncate_float_to_two_decimals(overall_standard_deviation))

    #Calculate minimum of list of average samples per second(sps) values calculated for each of 36 participants
    min_avg_value = min(samples_per_second_list)
    print("The minimum average samples per second  values for all participants: ", min_avg_value)

    #Calculate maximum of list of average samples per second(sps) values calculated for each of 36 participants
    max_avg_value = max(samples_per_second_list)
    print("The maximum average samples per second  values for all participants: ", max_avg_value)

if __name__ == "__main__":
    #Data path is assumed to be 'VRData'
    root_folder_path = 'VRData'
    process_csv_files(root_folder_path)
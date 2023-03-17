import dask.dataframe as dd
import os
import sqlite3


def import_data(dir_path):
    # store each file data in one dataframe
    dataframes = []

    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(dir_path, filename)

            # create dataframe from text file
            dataframe = dd.read_csv(filepath, sep="\t", header=None,
                                    names=["date", "max_temp", "min_temp", "precipitation"])

            # storing station_id
            dataframe["station_id"] = filename[:11]  # removing newline character
            dataframes.append(dataframe)

    # concat all dataframes into a single dataframe
    collective_dataframe = dd.concat(dataframes)

    # converting into panda dataframe
    panda_dataframe = collective_dataframe.compute()
    dataframe = panda_dataframe.reset_index(drop=True)

    # Not including -9999, which indicating the empty values
    stats = dataframe[(dataframe['max_temp'] != -9999) |
                      (dataframe['min_temp'] != -9999) | (dataframe['precipitation'] != -9999)]

    # creating the stats data
    stats = stats.groupby(['station_id', dataframe['date'].map(str).str[:4]]).agg({
        'max_temp': 'mean',
        'min_temp': 'mean',
        'precipitation': 'sum'
    }).reset_index()

    stats.rename(columns={'date': 'year',
                          'max_temp': 'avg_max_temp',
                          'min_temp': 'avg_min_temp',
                          'precipitation': 'total_acc_precipitation'}, inplace=True)

    conn = sqlite3.connect('./db.sqlite3')

    # write data to database
    dataframe.to_sql("weather_data", conn, if_exists="replace",
                     index=True, index_label='id')
    stats.to_sql("weather_stats", conn, if_exists="replace",
                 index=True, index_label='id')
    # close database connection
    conn.close()
    return


import_data('./wx_data')

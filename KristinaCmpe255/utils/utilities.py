import pandas as pd

def merge_data(pollution, crime):
    return pd.merge(pollution, crime, on=['date'], left_index=True)


def per_capita(crime, census):
    for i in range(len(census)):
        crime.loc[list((crime[crime['date'].str.contains(str(census.loc[i,'year']))]).index.values), 'per_capita'] = crime[crime['date'].str.contains(str(census.loc[i,'year']))]['count']/census.loc[i,'pop']

import pandas

def get_hourly_entries(df):

    df['ENTRIESn_hourly'] = (df['ENTRIESn'] - df['ENTRIESn'].shift(1)).fillna(1)

    return df

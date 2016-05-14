from pandas import *
from ggplot import *
import datetime

def plot_weather_data(turnstile_weather):

    df = read_csv(turnstile_weather)
    df_grouped = df.groupby('Hour',as_index=False).sum()

    plot = ggplot(df_grouped, aes(x='Hour',y='ENTRIESn_hourly')) +geom_line(color = 'blue')

    return plot

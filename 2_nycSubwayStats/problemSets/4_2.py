from pandas import *
from ggplot import *
import datetime
import csv


def plot_weather_data(turnstile_weather):

    df = read_csv(turnstile_weather)
    df['Day'] = df['DATEn'].map(lambda x:datetime.strptime(x, '%m/%d/%y').strftime('%w'))
    df_grouped = df.groupby('Day',as_index=False).mean()
    plot = ggplot(df_grouped, aes(x='Day',y='ENTRIESn_hourly')) +geom_line(color='blue') + geom_point(color='blue') + \
        ggtitle('Entries by day of week') + xlab('Day of week (0=Sunday through 6=Saturday)') + ylab('Average Entries')
    return plot

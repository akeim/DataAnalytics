import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):

    bins = np.linspace(0, 6000, 20)

    x = turnstile_weather['ENTRIESn_hourly'].where(turnstile_weather['rain'] == 1)
    y = turnstile_weather['ENTRIESn_hourly'].where(turnstile_weather['rain'] == 0)

    plt.hist(y, bins, alpha=0.5, label='Days with no rain')
    plt.hist(x, bins, alpha=0.5, label='Days with rain')
    plt.legend(loc='upper right')
    plt.ylabel('Frequency in days')
    plt.xlabel('Entries hourly')
    plt.title('Rainy Days Plot by Alyse')
    plt.show()
    return plt

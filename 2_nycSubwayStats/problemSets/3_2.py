import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):

    yes = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1]
    no = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0]
    with_rain_mean = np.mean(yes)
    without_rain_mean = np.mean(no)
    U, p = scipy.stats.mannwhitneyu(yes, no)

    return with_rain_mean, without_rain_mean, U, p

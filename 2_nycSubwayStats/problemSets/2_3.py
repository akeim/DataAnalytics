import pandasql

def avg_weekend_temperature(filename):

    weather_data = pandas.read_csv(filename)

    q = """
        SELECT avg(cast(meantempi as integer))
        FROM weather_data
        WHERE cast(strftime('%w', date) as integer) in (0,6)
    """

    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends

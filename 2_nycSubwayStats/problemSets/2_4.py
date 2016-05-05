import pandasql

def avg_min_temperature(filename):

    weather_data = pandas.read_csv(filename)

    q = """
        SELECT avg(cast(mintempi as integer))
        FROM weather_data
        WHERE mintempi > 55 and rain = 1
    """

    #Execute your SQL command against the pandas frame
    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp_rainy

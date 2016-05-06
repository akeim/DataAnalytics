import pandasql


def max_temp_aggregate_by_fog(filename):

    weather_data = pandas.read_csv(filename)

    q = """
    SELECT fog, max(maxtempi) from weather_data group by fog
    """

    #Execute your SQL command against the pandas frame
    foggy_days = pandasql.sqldf(q.lower(), locals())
    return foggy_days

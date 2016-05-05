import pandas
import pandasql


def num_rainy_days(filename):

    weather_data = pandas.read_csv(filename)

    q = """
    SELECT Count(*) from weather_data where cast(rain as integer) = 1
    """

    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days

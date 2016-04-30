import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        if passenger['Sex'] == 'male':
            predictions[passenger_id] = 0


    return predictions

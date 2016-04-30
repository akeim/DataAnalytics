import numpy
import pandas
import statsmodels.api as sm

def custom_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        elif passenger['Pclass'] == 1 and passenger['Age'] < 18:
            predictions[passenger_id] = 1
        elif passenger['Pclass'] == 2 and passenger['Age'] < 16:
            predictions[passenger_id] = 1
        elif passenger['SibSp'] > 3:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions

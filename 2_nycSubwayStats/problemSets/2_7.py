import pandas

def filter_by_regular(filename):

    td = pandas.read_csv(filename)
    turnstile_data = td[td['DESCn'] == 'REGULAR']
    return turnstile_data

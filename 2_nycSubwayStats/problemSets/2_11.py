import datetime
import time

def reformat_subway_dates(date):

    strip = time.strptime(date, '%m-%d-%y')
    fields = datetime.datetime(*strip[:3])
    date_formatted = fields.strftime('%Y-%m-%d')
    return date_formatted

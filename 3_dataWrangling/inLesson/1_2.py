#!/usr/bin/env python

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    column = sheet.col_values(1, start_rowx=1, end_rowx=None)

    max_val = max(column)
    max_index = column.index(max_val)
    max_time = sheet.cell_value(max_index+1, 0)
    max_tuple = xlrd.xldate_as_tuple(max_time, 0)

    min_val = min(column)
    min_index = column.index(min_val)
    min_time = sheet.cell_value(min_index+1, 0)
    min_tuple = xlrd.xldate_as_tuple(min_time, 0)

    avg_val = sum(column) / len(column)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    print sheet.nrows
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):",
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):",
    print sheet.cell_value(3, 2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):",
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)


    data = {
            'maxtime': max_tuple,
            'maxvalue': max_val,
            'mintime': min_tuple,
            'minvalue': min_val,
            'avgcoast': avg_val
    }
    print data
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()


import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        for i, line in enumerate(f, 1):
            if(i==1):
               headers = line.split(',')
            elif(i>1 and i<12):
                seperated = line.split(',')
                data_line = {}
                for i,value in enumerate(seperated):
                    data_line.update({headers[i].strip() : value.strip()})
                data.append(data_line)
            else:
                break
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}


    assert d[0] == firstline
    assert d[9] == tenthline


test()

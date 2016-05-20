
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    data_good = []
    data_bad = []
    with open(input_file, "r") as file_in:
        reader = csv.DictReader(file_in)
        header = reader.fieldnames
        for row in reader:
            start = row['productionStartYear']
            start_val = start[:4]
            try:
                start_val = int(start_val)
                row['productionStartYear'] = start_val
                if (start_val >= 1886) and (start_val <= 2014):
                    data_good.append(row)
                else:
                    data_bad.append(row)
            except:
                if start_val == 'NULL':
                    data_bad.append(row)

    with open(output_good, "w") as good:
        writer = csv.DictWriter(good, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in data_good:
            writer.writerow(row)

    with open(output_bad, "w") as bad:
        writer = csv.DictWriter(bad, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in data_bad:
            writer.writerow(row)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()

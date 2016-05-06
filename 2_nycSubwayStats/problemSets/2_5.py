import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        with open(name, 'r') as bad_file:
            with open("updated_{0}".format(name), 'w') as correct_file:
                new = csv.writer(correct_file)
                for row in csv.reader(bad_file):
                    new.writerow(row[:8])
                    low_count = 0
                    high_count = 8
                    while high_count < 43:
                        low_count = high_count
                        high_count = high_count + 5
                        new.writerow(row[:3] + row[low_count:high_count])

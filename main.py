import csv
# opening the names.csv file and reading it.
with open('names.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
# creating a new csv file (new_name.csv) and writing it.
    with open('new_name.csv', 'w') as new_file:
        # a delimiter is what is used to separate the different values in the file. in this case '\t' creates a space in the new csv file to separate the values.
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
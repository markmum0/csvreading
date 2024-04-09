import csv
# read the original csv 'names.csv' using the DictReader this time
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# create a new csv file 'new_names.csv'. the field names are headers for the data
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
# write using the DictWriter. Add field names and delimiter of choice
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
# write the headers of the data. The descriptions
        csv_writer.writeheader()
# check the new_names.csv file for results
        for line in csv_reader:
            csv_writer.writerow(line)
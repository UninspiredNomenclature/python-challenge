# import modules
import os
import csv

#import data
csvpath = os.path.join('Resources', 'budget_data.csv')

#open csv for improved reading
csvreader = csv.reader("budget_data.csv", delimiter=',')

csv_header = next(csvreader)
print(f"csv header: {csv_reader}")


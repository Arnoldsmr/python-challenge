import os
import csv

csvpath = os.path.join("python-challenge","Pypoll","Resources","election_data.csv")

with open(csvpath,encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    csv_header = next(csv_file)
                      
    total_votes = 0
    candidates = {}
                   
    for row in csv_reader:
        total_votes  = total_votes + 1
        candidate = row[2]

        if candidate != candidates:
            candidates[candidate] = 1

    percentages = {}
   

    print("Election Results")
    print(f"Total Votes: {total_votes}")
  
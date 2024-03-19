#read csv
import os
import csv


election_data = []
total_ballet = 0

Resource = os.path.join('Resources', 'election_data.csv')

with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    election_data.append(csv_header)

    vote = 0

    for row in csvreader:
        vote += 1


print("Election Results")
print("-------------------")
print(f"Total Votes: {vote}")
print("-------------------")

#total number voted
#list of canidates
# % of votes won for each canidate 
# number of votes won for each canidate
# winner of popular vote
#print it
#create .txt and output info
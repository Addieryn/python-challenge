#read csv
import os
import csv


election_data = []
total_ballet = 0

Resource = os.path.join('Resources', 'election_data.csv')


def print_percentages(election):

    
    ballet = int(election[0])
    county = str(election[1])
    canidate = str(election[2])

    ballet += 1
    can_name == str(election[2])

    if county != county:
        can_name = county




with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    election_data.append(csv_header)

    vote = 0

    for row in csvreader:
        vote += 1

        ballet = int(row[0])
        county = str(row[1])
        canidate = str(row[2])


        ballet += 1
        can_name = row[2]

    for row in csvreader:
        can_name = str(row[2])
     

        #need to pull at each point
        if can_name != can_name:
            canidate = can_name
            #if i take it out it prints 1, but when i leave it in the loop it doesnt print
            print(canidate)
    #perc_win = (vote) * 100



print("Election Results")
print("-------------------")
print(f"Total Votes: {vote}")
print("-------------------")



#output_path = os.path.join("analysis", "Election_Results.csv")

#with open(output_path, 'w') as csvfile:
      #csvwriter = csv.writer(csvfile)

#list of canidates
# % of votes won for each canidate 
# number of votes won for each canidate
# winner of popular vote
#print it
#create .txt and output info
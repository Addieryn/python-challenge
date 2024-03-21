#read csv
import os
import csv


#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

election_data = []
total_ballet = 0
can_list = []
first_can = ["", []]
second_can = ["", []]
third_can = ["", []]

Resource = os.path.join('Resources', 'election_data.csv')


with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    election_data.append(csv_header)

    total_ballet = 0
    vote = 0

    candidate_dict = {}

    for row in csvreader:
        total_ballet += 1

        if row[2] in candidate_dict:
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1
        else:
            candidate_dict[row[2]] = 1
    
    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {total_ballet}")
    print("-------------------")
    
    most_votes = 0
    most_who = ""

    candidate_info = []
        
    for key, value in candidate_dict.items():
        
        print(f'{key}: {value} ({(int(value)/total_ballet):.3%})')
        candidate_info.append("{}".format(f'{key}: {value} ({(int(value)/total_ballet):.3%})') + os.linesep)
        
        if most_votes == 0:
            most_votes = value
            most_who = key

        if value > most_votes:
            most_votes = value
            most_who = key

print("-------------------")
print(f'Winner: {most_who}')            
print("-------------------")

print(candidate_info)


output_path = os.path.join("analysis", "Election_Results.txt")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Total Votes:", f"{total_ballet}"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(candidate_info)
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Winner:" f'{most_who}'])
    csvwriter.writerow(["-------------------"])

#read csv
import os
import csv

election_data = []  #creating where i'll store info
total_ballet = 0

Resource = os.path.join('Resources', 'election_data.csv') #finding and reading csv

with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    election_data.append(csv_header)

    total_ballet = 0        #setting up values
    vote = 0

    candidate_dict = {}     #dictionary to hold lists of pulled info

    for row in csvreader:
        total_ballet += 1       #adding total of votes

        if row[2] in candidate_dict:        #using in dictionary so we can store and comparre each value
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1  #using the adding to total the number of votes/rows associated with the name
        else:
            candidate_dict[row[2]] = 1
    
    print("Election Results")               #printing before for loop
    print("-------------------")
    print(f"Total Votes: {total_ballet}")
    print("-------------------")
    
    most_votes = 0      #setting p values
    most_who = ""

    candidate_info = []    #creating list to store info from for loop
        
    for key, value in candidate_dict.items():   #used .items() to retain and seperate values to use later
        
        print(f'{key}: {value} ({(int(value)/total_ballet):.3%})')      #:.3% instead of value / total * 100  #Also printing in for loop to get each canidate info
                                                                     
        candidate_info.append("{}".format(f'{key}: {value} ({(int(value)/total_ballet):.3%})') + os.linesep)    #os.linesep to try and give a new row
        
        if most_votes == 0:         #using a comparison to find most votes
            most_votes = value
            most_who = key

        if value > most_votes:      #using previous finding to get name(key) related to value
            most_votes = value
            most_who = key

print("-------------------")    #print next set including value just gained
print(f'Winner: {most_who}')            
print("-------------------")

output_path = os.path.join("analysis", "Election_Results.txt") #writing a new .txt file

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Total Votes:", f"{total_ballet}"]) #used f string at the end so I could seperate info better
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(candidate_info)          #thinking I should have used a def to make a function, but found this way easier to grasp
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Winner:" f'{most_who}'])
    csvwriter.writerow(["-------------------"])

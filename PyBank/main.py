#read csv
import os
import csv


Resource = os.path.join('Resources', 'budget_data.csv')


budget_data = [] #has to be list because its tracking the whole row
total_month = 0 #creating values outside read/loops
total = 0
pl_line = 0
month_change = [] #has to be list because it keeps track of its relative place in the row so it can save all values
list_change = []
increase = ["", 0]         #list because multiple comparable values ["" for the value of the row, 0 for the comparison to the row]
decrease = ["",999999999]

with open(Resource) as csvfile:     #finding and reading csv
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader) #skipping header
    budget_data.append(csv_header)
   
    start_row = next(csvreader) #starts at row after header
   
    total_month = 1             #starting value 
    total = int(start_row[1])   
    pl_line = int(start_row[1])    
    

    for row in csvreader:
        
        total_month += 1        #taking value and adding to the next
        total += int(row[1])

        net_change = int(row[1]) - pl_line # - because we need change(negative numbers)
        
        pl_line = int(row[1])       #pl_line comes after net_change to set new value and not override
        
        list_change += [net_change] #adding the changes together 
        month_change += [row[0]]

        if net_change < decrease[1]: #taking each rows change value and comparing it to our list number 0
            decrease[0] = row[0]     #making our list value equal to row value
            decrease[1] = net_change #making our number we are comparing the next iteration
        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change  
  
#def needs to be out of loop but doesnt matter where       
def average(list_change):       #using list_change because its the list of all numbers in column
    length = len(list_change)   #number of values
    total = sum(list_change)    #total of values
    return total / length       #return sends the value calculated

print("Financial Analysis")
print("-------------------")  
print(f"Total Months: {total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${average(list_change):.2f}")           #using .2f rounds to 2 decimals
print(f"Greatest increase in profit: {increase[0]} (${increase[1]})")   #using [0] and [1] for the month captured in list and value accociated with it
print(f"Greatest decrease in profit: {decrease[0]} (${decrease[1]})")

output_path = os.path.join("analysis", "Financial_Analysis.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
      
    csvwriter.writerow(["Total Months:", total_month])
    csvwriter.writerow(["Total:", f"${total}"])                                 #using f" to take value as is but still seperating using ","
    csvwriter.writerow(["Average Change:", f"${average(list_change):.2f}"])
    csvwriter.writerow(["Greatest increase in profit:", increase[0], f"${increase[1]}"])
    csvwriter.writerow(["Greatest decrease in profit:", decrease[0], f"${decrease[1]}"])

#read csv
import os
import csv


budget_data = []
total_month = 0

Resource = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------")

total = 0
pl_great = 0
#def average(numbers):
#    length = len(numbers)
#    total = 0
#    for i in numbers:
#        total += i
#    return total / length
    

with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    budget_data.append(csv_header)
   # print(f"{csv_header}")
    profit_loss = 0
    
    #incsv = csv.reader(csvfile)
    #column = 1               
    #datatype = int
    #data = (datatype(row[column]) for row in incsv)
    #least_value = min(csv_header)

    for row in csvreader:
        
        increase = 0
        decrease = 0
        total_month += 1
        month = str(row[0]) 
        profit_loss += int(row[1]) 
        pl_great = int(row[1])

    if increase <= pl_great:
            increase = pl_great
            
    if decrease >= pl_great:
            decrease = pl_great
        
    #for row in incsv:
           
       # if least_value == datatype(row[column]):
        #    print(row)
   
print(f"Total Months: {total_month}")
print(f"Total: ${profit_loss}")
#print(average(profit_loss))
print(f"Greatest increase in profit: {month} (${increase})")
print(f"Greatest decrease in profit: {month} (${decrease})")

#total months recorded
#net total
#average change in profit/loss
#greatest increase over time
#greatest decrease over time
#print it
#create .txt and output info
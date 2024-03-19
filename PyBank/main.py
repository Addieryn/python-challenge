#read csv
import os
import csv


budget_data = []
total_month = 0

Resource = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------")

total = 0
pl_line = 0
month_change = []
list_change = []
increase = ["", 0]
decrease = ["",999999999]

with open(Resource, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    budget_data.append(csv_header)
   
    profit_loss = 0
    first_row = next(csvreader)
    total_month += 1
    total += int(first_row[1])
    pl_line += int(first_row[1])    
  

    for row in csvreader:
        
        
        total_month += 1
        month = str(row[0]) 
        profit_loss += int(row[1]) 
       
        total += int(row[1])

        net_change = int(row[1]) - pl_line
        
        pl_line = int(row[1])
        list_change += [net_change]
        month_change += [row[0]]


        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change

        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change
        
  
         
def average(list_change):
    length = len(list_change)
    total = sum(list_change)
    return total / length

  
print(f"Total Months: {total_month}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average(list_change):.2f}")
print(f"Greatest increase in profit: {increase[0]} (${increase[1]})")
print(f"Greatest decrease in profit: {decrease[0]} (${decrease[1]})")

#output_path = os.path.join("analysis", "Financial_Analysis.csv")

#with open(output_path, 'w') as csvfile:
      #csvwriter = csv.writer(csvfile)
      
        #csvwriter.writerow(f"Total Months: {total_month}")
        #csvwriter.writerow(f"Total: ${profit_loss}")
        #csvwriter.writerow(f"Average Change: ${average(list_change):.2f}")
        #csvwriter.writerow(f"Greatest increase in profit: {increase[0]} (${increase[1]})")
        #csvwriter.writerow(f"Greatest decrease in profit: {decrease[0]} (${decrease[1]})")
     

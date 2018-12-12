# Modules
import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    month_count = 0
    total_count = 0
    prev_row = 0
    next_row = 0
    avg_change = 0
    next(csvreader)
    prev_row = 0
    change_list = []
    month_list = []
    for row in csvreader:
        month_count += 1
        total_count += int(row[1])
        if month_count <= 1:
            change = 0
        else: 
            change = int(row[1]) - prev_row
            change_list.append(change)
            month_list.append(row[0])
        prev_row = int(row[1])
    avg_change = sum(change_list)/len(change_list)
    greatest_change = max(change_list)
    least_change = min(change_list)
    greatest_index = change_list.index(greatest_change)
    least_index = change_list.index(least_change)
    greatest_month = month_list[greatest_index]
    least_month = month_list[least_index]
   
    print("Total Months: " + str(month_count))
    print("Total:  $" + str(total_count))
    print("Average Change:  $" + str(avg_change))
    print("Greatest increase in profits: " + str(greatest_month) + " $" + str(greatest_change))
    print("Greatest decrease in profits: " + str(least_month) + " $" + str(least_change))


    
    
    
    
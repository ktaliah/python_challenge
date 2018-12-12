# Modules
import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# Open file as CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Counts set to zero
    month_count = 0
    total_count = 0
    prev_row = 0
    next_row = 0
    avg_change = 0
    prev_row = 0

    # Skip header row
    next(csvreader)

    # Lists to store data
    change_list = []
    month_list = []

    # Loop through CSV file
    for row in csvreader:
        
        # Adds 1 for each row
        month_count += 1

        # Adds amount in index 1 for each row
        total_count += int(row[1])

        # Sets change count to 0 at month 1
        if month_count <= 1:
            change = 0
        
        else: 

            # Subtracts amount in index 1 from previous row
            change = int(row[1]) - prev_row

            # Adds changes in profits/losses
            change_list.append(change)

            # Adds months
            month_list.append(row[0])
        # Sets previous row to index 1 in each row    
        prev_row = int(row[1])
    
    # Calculates average change as the total sum of the change list divided by the length of the change list
    avg_change = sum(change_list)/len(change_list)

    # Sets greatest increase to the max value in the change list
    greatest_increase = max(change_list)

    # Sets greatest decrease to the min value in the change list
    greatest_decrease = min(change_list)

    # Finds the index value of the greatest increase in the change list
    increase_index = change_list.index(greatest_increase)
    
    # Finds the index value of the greatest decrease in the change list
    decrease_index = change_list.index(greatest_decrease)

    #Finds the corresponding month of the greatest increase in profits
    increase_month = month_list[increase_index]

    #Finds the corresponding month of the greatest decrease in profits
    decrease_month = month_list[decrease_index]
   
    print("Total Months: " + str(month_count))
    print("Total:  $" + str(total_count))
    print("Average Change:  $" + str(avg_change))
    print("Greatest increase in profits: " + str(increase_month) + " $" + str(greatest_increase))
    print("Greatest decrease in profits: " + str(decrease_month) + " $" + str(greatest_decrease))
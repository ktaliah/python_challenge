# Modules
import os
import csv

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Open file as CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Counts set to zero
    vote_count = 0

    # Skip header row
    next(csvreader)

    # Lists to store data
    candidate_list = []

    # Loop through CSV file
    for row in csvreader:
        
        # Adds 1 for each row
        vote_count += 1

        candidate_found = False

        # Used to add the vote counts for each candidate
        index = 0

        for candidate in candidate_list:
            if row[2] == candidate['name']:
                candidate_found = True
                break

            index += 1                    
        
        if candidate_found == False:

            # Create dictionary
            candidate_dictionary = {'name': row[2], 'count': 1}

            # Append dictionary to candidate list
            candidate_list.append(candidate_dictionary)
        else:
            candidate_list[index]['count'] += 1 

print("Election Results")
print("------------------------------")
print("Total Votes: " + str(vote_count))
print("------------------------------")
for candidate in candidate_list:
    percent = (candidate['count']/vote_count) * 100
    print(candidate['name'] + ": " + str('%.3f' % percent) + "% " + "(" + str(candidate['count']) + ")")
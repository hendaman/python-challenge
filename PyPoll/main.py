# Imports
import os
import csv

# Read the csv file

csvpath = os.path.join('Resources', 'election_data.csv')

# Define lists to be used
total_votes = 0
list_ballot_id = []
list_county = []
list_candidate = []
candidate_votes = {}

# Open the csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

# Skip the header
    csv_header = next(csvreader)



# Calculate the total rows of data after the header by putting each column in lists
    for row in csvreader:
        total_votes += 1
        candidate = (row[2])
        if candidate not in list_candidate:
            list_candidate.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

        
# Calculate total votes
votes = (int(len(csv_header)))
print(votes)

# Determine all candidates that received votes

list_ballot_id.append(row[0])
list_county.append(row[1])

# Calculate the total number of votes each candidate won



# Calculate what percentage of all votes each candidate won



# Determine the winner of the election based on who has the most votes




# Display results in the terminal as per the correct format and export them to a text file
print("Election Results")
print("---------------------------")
print(f"Total Votes: {votes}")
print("---------------------------")

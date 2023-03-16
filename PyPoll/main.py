# Imports
import os
import csv

# Read the csv file/create path to save to
csvpath = os.path.join('Resources', 'election_data.csv')

save_to = os.path.join('analysis', 'election_results.txt')

# Define variables
total_votes = 0
winning_count = 0
winning_percentage = 0
list_candidate = []
candidate_votes = {}

# Open the csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Skip the header
    csv_header = next(csvreader)

# Calculate the total rows of data to work out vote count and store each candidate for each row
    for row in csvreader:
        total_votes += 1
        candidate = (row[2])
# Use a list to store the unique candidates names if they aren't already in the list and count each vote against the candidate in a dictionary regardless of if they are already there
        if candidate not in list_candidate:
            list_candidate.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Display results in the terminal as per the correct format and export them to a text file
with open(save_to, "w") as txt_file:
    results1 = (f"Election Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n")
    
    print(results1, end="")
    txt_file.write(results1)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage = float(votes) / float(total_votes) * 100
        results2 = (f"{candidate}: {percentage:.1f}% ({votes:,})\n")

        print(results2)
        txt_file.write(results2)

        if (votes > winning_count) and (percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = percentage

    results3 = (f"---------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"---------------------------\n")
    
    print(results3)
    txt_file.write(results3)

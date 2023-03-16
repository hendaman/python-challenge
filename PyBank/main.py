# Imports
import os
import csv

# Read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

save_to = os.path.join('analysis', 'profit_analysis.txt')

# Define lists to be used
total_months = 0
total_net = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999]
first_row = True
net_change = 0

# Open the csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Skip the header
    csv_header = next(csvreader)
    
    for row in csvreader:
        if first_row is True:
            total_months += 1
            total_net += int(row[1])
            month_of_change += [row[0]]
            first_row = False
            prev_net = int(row[1])
    
# Calculate the total rows of data after the header, as well as store the total net profit/loss, the net changes and put them in a list alongside the month the changes were in
        else:
            total_months += 1
            total_net += int(row[1])
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list += [net_change]
            month_of_change += [row[0]]
# Determine which date and amount had the greatest increase in profits from previous month
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
# Determine which data and amount had the greatest decrease in profits from previous month
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Return the mean of those changes over that period of time
mean_changes = sum(net_change_list) / (len(month_of_change) - 1)

# Display the data in correct format in the terminal, and export as a text file with the results to the analysis folder
with open(save_to, "w") as txt_file:
    results = (
        f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${mean_changes}\n"
        f"Greatest Increase in Profits:{greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits:{greatest_decrease[0]} (${greatest_decrease[1]})\n")
    print(results, end ="")
    txt_file.write(results)
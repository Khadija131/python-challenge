# PyBank analysis script
#
#
# Import the os module and the csv module
import os
import csv

# Set path for date
csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Analysis", "budget_analysis.txt")

# Lists and variables to store data
date = []
monthly_pnl = []
months = 0
total = 0
prev_rev = 0
change = 0
total_change = 0
inc = ["", 0]
dec = ["", 0]

# Open path
with open(csvpath, newline="") as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       csv_header = next(csvreader)

        # Read each row of data after header and assign variables
       for row in csvreader
            date.append(row[0])
            monthly_pnl.append(row[1])

        # Create script to calculate:
            
            #The total number of months included in the dataset
            months += 1
            total += int(row[1])

            #Evaluate change
            change = int(row[1]) - prev_rev
            if prev_rev ==0:
                  change = 0
            prev_rev = int(row[1])
            total_change += change

            #Evaluate Increase
            if change > int(inc[1]):
                  inc[1] = change
                  inc[0] = row[0]

            #Evaluate Decrease
            if change < int(dec[1]):
                  dec[1] = change
                  dec[0] = row[0]


     total_change = total_change / (months -1)

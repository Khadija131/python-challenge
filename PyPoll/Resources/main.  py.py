#PyPoll challenge
#
#
#Import the os module for reading CSV Files
import os
import csv

# Set file path
csvpath = os.path join( 'Resources', 'election_datat.csv')
pathout = os.path.join("Analysis, "election_results.txt")
                       
#List and variables to store data
 candidates = []
 votes = []
 county =[]
 otooley =[]
 khan= []
 correy= []
 li= []

 # Etract Data from election_data.csv to three columns: 'Voter ID', 'County', and 'Candidate' with open(csvpath) as csvfile:
 csvreader =csv.reader(csvfile, delimiter=',')
 cvs_header = next(csvreader)

 # Read each row of data after the header and loop through rows
 for row in cvsreader:
        votes. append(row[0])
        county. append(row[1])
        cndidates.append (row[2])

        # The total number of votes cast
              voter_total = len (row [1])

        # A complete list of candidates who received votoes and the total number of votes candidates won.
             for can in candidates:
                if can =="khan":
                    khan. append(candidates)
                elif can =="correy"
                    correy.append(candidates)
                    votes_correy = len(correy0)
                elif can =="11":
                    li. append(candidates)
                    votes_li = len(li)
                else:
                    otooley.append(candidates)
                    votes_otooley =  len(otooley)

# The percentage of votes each candidates won.
per_khan = round(((votes_khan/ voter_total) * 100), 2
per_correy = round(((votes_correy/ voter_total)*100),2)
per_li = round (((votes_li/ votertotal)*100, 2)
per_otooley = round((votes_otoonley/ voter_total)*100), 2)

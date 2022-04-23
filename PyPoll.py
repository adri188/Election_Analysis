# retrieve data file

import os
import csv
from pickle import TRUE
from timeit import repeat
#print(os.getcwd())

# Assign a variable for the file to load and the path.
file_to_load= os.path.join("Module3","Election_Analysis","Resources","election_results.csv") # Indirect Path     
    #file_to_load = '"..",Resources/election_results.csv' Direct Path
 
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Module3","Election_Analysis","analysis", "election_analysis.txt")


#1.  Total Number of votes cast 
# #initialize variables/lists / dicts
total_votes=0    
candidate_options = []
candidate_votes ={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    #to do: read and analyze data 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
        #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        #Add votes
        total_votes += 1
        # get candidate name 
        candidate_name=row[2]
        #append to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begging tracking votes - create key and value  for dictionary
            candidate_votes[candidate_name] = 0
        #add votes 
        candidate_votes[candidate_name] += 1
    
    #Print total votes 
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
    
    # Get vote count for candidate  calculate % and print
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes)/ float(total_votes))*100
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
         
        
    #Print winning candidate summary
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

#2. A complete list of candidates who received votes
#New List of candiate
    
#3. % votes each candidate won 
#4. Total number of votes for each candidate
#5. Winner of election

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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #to do: read and analyze data 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
   # Print the file object.
    # print(election_data)

#1.  Total Number of votes cast
#2. A complete list of candidates who received votes
#3. % votes each candidate won 
#4. Total number of votes for each candidate
#5. Winner of election

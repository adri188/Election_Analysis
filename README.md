# Election_Analysis

## Project Overview
Colorado board of directors initially  presented following  tasks to complete election audit for the congressional election

    1. Total votes cast
    2. Complete list of candidates who received votes    
    3. % votes each candidate won 
    4. Total number of votes for each candidate
    5. Winner of election
  
The election commission has requested some additional data to complete the audit:

    6. The voter turnout for each county
    7. Percentage of votes from each county out of the total count
    8. The county with the highest turnout

A written summary of the resuls and the methods use to complete this audit are presented below.

  
 ## Resources
 
 * Data Sources: election_results.csv
 * Software: Python 3.6.1, VS Code 1.66.2
 
 ## Summary

 ### Election Results
 The analysis of the election shows:
 
- Total Votes: 369,711

- County Votes:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)

- Denver had the largest turnout on the election

-Candidate Results:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892) 
  - Raymon Anthony Doane: 3.1% (11,606)
   
- Winner of the election
  - Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

 
### Election-Audit Summary 

The method used for this analysis can be used as a template to audit upcoming elections by making a few modifications. 
This code consists in: 
- Importing data from a tabulated file
- Creating desired variables
- Extracting requested information:
   > Add to total vote count
   > Create Candidate List and County List 
   > Add votes for each candidate and County
- Calculating results 
   > Based on conditionals evaluate winning candidate and largest county
-Writing a report

#### To use this on your next congressional election Follow this steps: 

1. Upload csv file with ballot count for new election: Make sure information is in the same order. ( Ballot ID, County, Candidate)

<img width="652" alt="Screen Shot 2022-04-24 at 2 32 08 PM" src="https://user-images.githubusercontent.com/102937320/164997536-689f89c3-369a-4196-b092-4188cf318250.png">

2. update name of the csv file  on file to load , or add an input variable to specify which election to analyze. 

<img width="774" alt="Screen Shot 2022-04-24 at 3 24 47 PM" src="https://user-images.githubusercontent.com/102937320/164999258-1dda97a9-4160-4bc3-93e7-8cfa24be13b0.png">

#### To use this on any election

Based on csv file, you can get candidate and county reference (or position on list)  and modify accordingly  on this lines 
<img width="414" alt="Screen Shot 2022-04-24 at 4 24 19 PM" src="https://user-images.githubusercontent.com/102937320/165000980-c901f7b4-2e4d-4d5a-987d-3a379dc2e957.png">

You can add additional variables and  modify lists and dictionaries following same structure as counties to collect any other  desired data, such as parties, race, etc.






# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of otes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The Candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of the votes.
  - Diana DeGette received 73.8% of the vote, and 272,892 number of the votes.
  - Raymon Anthony Doane received 3.1% of the vote, and 11,606 number of the votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote, and 272,892 number of the votes.
  
## Challenge Overview
Using excel open the .csv to examine data and get the total ballots, then using python in Visual Studio Code, import a .csv and iterate through it to gather unique candidate names in a list, creating a dictionary with the candidate names, count the vote of each candidate and calculate the percentage of votes using the total votes cast in the election. After that was all working properly, stored the highest votes and the candidate associated with it in a variable using a if and statement. Lastly, write the variables of the analysis into the election_analysis.txt

## Challenge Summary
- https://docs.python.org/3.7/library/functions.html#round -  used python documentation to round the percentage of votes to 1 decimal place.


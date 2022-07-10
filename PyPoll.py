# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")


# initialize variables


total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0



with open(file_to_load) as election_data:

    # To Do: read and analyze the data here.

    # Read the file object with the reader funciton

    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.

    #for row in file_reader:
    #    print(row)

    # Read and print the header row.

    headers = next(file_reader)

    for row in file_reader:

        # 2. Add the total vote count.

        total_votes += 1

        # print the candidate name from each row

        candidate_name = row[2]
       

        # if candidate does not match any existing candidate...

        if candidate_name not in candidate_options:

            # add it to the list of candidates

            candidate_options.append(candidate_name)

            # begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1


# save the results to our text file

with open(file_to_save, "w") as txt_file:

   
    # Print the final vote count to the terminal.
  
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    
    txt_file.write(election_results)
    
    
        
    print(candidate_options) 
    print(candidate_votes)   
        
    # 3. Print the total votes  
        
    print(total_votes)  
        
    # determine the percentage of votes for each candidate by looping through counts 
        
    # 1. iterate through the candidate list. 
        
    for candidate_name in candidate_votes:    
        
            # 2. retrieve vote count of a candidate  
        
            votes = candidate_votes[candidate_name]   
        
        # 3. calculate the percentage of votes. 
        
            vote_percentage = float(votes) / float(total_votes) * 100   
        
        # 4. print the candidate name and percentage of votes and save it to a text file    
        
            candidate_results = (f"\n{candidate_name}: received {round(vote_percentage, 1)}% of the vote, for a total of {votes:,} votes.\n")  
        
            print(candidate_results)

            txt_file.write(candidate_results)

        
            if (votes > winning_count) and (vote_percentage > winning_percentage):  
                
                winning_count = votes   
                winning_percentage = vote_percentage    
        
                winning_candidate = candidate_name   
        
    winning_candidate_summary = (   
        f"\n-------------------------\n"  
        f"Winner: {winning_candidate}\n"    
        f"Winning Vote Count: {winning_count:,}\n"  
        f"Winning Percentage: {winning_percentage:.1f}%\n"  
        f"-------------------------\n") 
        


    print(winning_candidate_summary)   
        
    txt_file.write(winning_candidate_summary)
        
        
        

















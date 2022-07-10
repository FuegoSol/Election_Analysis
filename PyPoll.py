# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who received votes
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

canidate_options = []

canidate_votes = {}

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

        # print the canidate name from each row

        canidate_name = row[2]
       

        # if canidate does not match any existing canidate...

        if canidate_name not in canidate_options:

            # add it to the list of canidates

            canidate_options.append(canidate_name)

            # begin tracking that canidates vote count
            canidate_votes[canidate_name] = 0
            
        canidate_votes[canidate_name] += 1




print(canidate_options)
print(canidate_votes)

# 3. Print the total votes

print(total_votes)

# determine the percentage of votes for each canidate by looping through counts

# 1. iterate through the canidate list.

for canidate_name in canidate_votes:

        # 2. retrieve vote count of a canidate

        votes = canidate_votes[canidate_name]

    # 3. calculate the percentage of votes.

        vote_percentage = float(votes) / float(total_votes) * 100

    # 4. print the canidate name and percentage of votes

        print(f"{canidate_name}: received {round(vote_percentage, 1)}% of the vote.")


        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = canidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)





















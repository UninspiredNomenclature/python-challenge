# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""
 
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
 
# Initialize variables to track election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winner = ""
winning_votes = 0
 
 
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Print a loading indicator (for large datasets)
        print("Data is loading. ", end="Data loaded.")
        
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates:
            candidates[candidate] = 0

        # Add a vote to the candidate's count
        candidates[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

# Print the total vote count (to terminal)
    print(f"\nProcessed {total_votes:,} votes.\n")

# Write the total vote count to the text file
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    "-------------------------\n"
)

# Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidates:
    # Get the vote count and calculate the percentage
    votes = candidates[candidate]
    vote_percentage = (votes / total_votes) * 100

    # Update the winning candidate if this one has more votes
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

    # Print and save each candidate's vote count and percentage
    output += f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n"

# Generate and print the winning candidate summary
output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print complete results to terminal
print(output)

# Write results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

print(f"Results have been written to: {file_to_output}")
# 1. Total Number votes cast
# 2. Complete list of candidates receiving votes
# 3. Percentage of votes for each candidate
# 4. Total number for each candidate
# 5. Winner based on popular vote

#add dependencies
import csv
import os
#Assign variable for file and path
file_to_load = os.path.join('resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

total_votes = 0

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open the election results and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read the header
    headers = next(file_reader)
    
    #print each row
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print out candidates and votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning candidate and votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
         f"--------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"--------------------------\n")
         
    print(winning_candidate_summary)
    


open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")



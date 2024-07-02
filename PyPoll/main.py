#!/usr/bin/env python
# coding: utf-8

# In[51]:


import csv
import os

raw_data = os.path.join(".", "Resources", "election_data.csv")
save_file = os.path.join(".", "analysis", "election_results.txt")

# total counter
vote_counter = 0

# candidate count and vote count
candidate_votes = {}
candidates = []
winning_count = 0
vote_percentage = 0

with open(raw_data) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        vote_counter += 1

        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates.append(candidate_name) 

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# print(candidate_votes)
# print(candidates)  



with open(save_file, "w") as txt_file:
    outcome = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_counter}\n"
        f"-------------------------\n"
    )
    print(outcome)

    txt_file.write(outcome)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(vote_counter) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        # print(votes)
        # print(vote_percent)
        print(voter_output)

    txt_file.write(voter_output)

    winnerz = (
        f"-------------------------\n"
        f"{winning_candidate} WINS!\n"
        f"-------------------------"
    )
    print(winnerz)
    txt_file.write(winnerz)



# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


# In[ ]:





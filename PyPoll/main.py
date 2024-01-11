import csv
import os

csvpath=os.path.join("..","PyPoll","Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    total_votes=0
    candidate_list=[]
    candidate_vote1=0 
    candidate_vote2=0
    candidate_vote3=0

    for row in csvreader:
        total_votes=total_votes+1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2]==candidate_list[0]:
            candidate_vote1=candidate_vote1+1
        elif row[2]==candidate_list[1]:
            candidate_vote2=candidate_vote2+1
        else:
            candidate_vote3=candidate_vote3+1

    candidate_votes=[candidate_vote1, candidate_vote2, candidate_vote3]
    
    candidate_perc1=round((candidate_vote1/total_votes)*100, 3)
    candidate_perc2=round((candidate_vote2/total_votes)*100, 3)
    candidate_perc3=round((candidate_vote3/total_votes)*100, 3)

    winner=max(candidate_votes)
    if winner==candidate_votes[0]:
        winner_name=candidate_list[0]
    elif winner==candidate_votes[1]:
        winner_name=candidate_list[1]
    else:
        winner_name=candidate_list[3]

print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
print(f"{candidate_list[0]}: {candidate_perc1}% ({candidate_vote1})")
print(f"{candidate_list[1]}: {candidate_perc2}% ({candidate_vote2})")
print(f"{candidate_list[2]}: {candidate_perc3}% ({candidate_vote3})")
print("----------------------------------")
print(f"Winner: {winner_name}")
print("----------------------------------")

file=("Analysis/pypoll.txt")
with open(file, 'w') as text:
    text.write("Election Results\n")
    text.write("----------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("----------------------------------\n")
    text.write(f"{candidate_list[0]}: {candidate_perc1}% ({candidate_vote1})\n")
    text.write(f"{candidate_list[1]}: {candidate_perc2}% ({candidate_vote2})\n")
    text.write(f"{candidate_list[2]}: {candidate_perc3}% ({candidate_vote3})\n")
    text.write("----------------------------------\n")
    text.write(f"Winner: {winner_name}\n")
    text.write("----------------------------------\n")

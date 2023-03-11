import os
import csv

#Read the csv files from Resources folder and store them into a electiondata list.
csvfile = open (os.path.join("Resources","election_data.csv"),'r')
electiondata = csv.reader(csvfile,delimiter=",")

#skip reading the header in the csv file.
next(electiondata, None)

#create list and dictionary
totalVotes = []
candidates = []
candidateVoteCount = {}
voteCount = []

#loop through the election data file to find the total number of votes and store each candidate name in the name variable.
for row in electiondata:

    name = row[2]
    totalVotes.append(row[0])
    
    #Store and remove any duplicate candidate name and initiate their vote counter.
    if name not in candidates:
        candidates.append(row[2])
        candidateVoteCount[name] = 0

    #for each candidate, count the number of vote.
    candidateVoteCount[name] = candidateVoteCount[name] + 1

#Create the text file or rewrite the text file in analysis folder if exist and get the total number of votes in the list.
f =open(os.path.join("analysis","election_results.txt"),"w+")
f.write ("Election Results\n\n")
f.write ("----------------------------\n\n")
f.write (f"Total Votes: {len(totalVotes)}\n\n")
f.write ("----------------------------\n\n")

#Display each candidate's name, the total number of votes for each candidate, calculate their vote percentage 
#and find who has the highest number of vote.
for name in candidateVoteCount:
    candidateVote = candidateVoteCount[name]
    votePercent = "{:.3%}".format(float(candidateVote)/float(len(totalVotes)))

    voteCount.append(candidateVoteCount[name])
    highestVoteIndex = voteCount.index(max(voteCount))

    f.write (f"{name}: {votePercent} ({candidateVote}) \n\n")

#Display the winner's name.
f.write ("----------------------------\n\n")
f.write (f"Winner: {candidates[highestVoteIndex]}\n\n")
f.write ("----------------------------")
f.close()
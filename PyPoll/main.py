import os
import csv

banner = "-"*20
# initialize list for tallying votes
ballot_list = []
candidates = []

charles_votes = 0
diana_votes = 0
raymon_votes = 0

csvpath = os.path.join(os.getcwd(),"Class_Materials", "personal_repos","python-challenge", "PyPoll", "Resources", "election_data.csv")
# print(csvpath)    checking path
if not os.path.exists(csvpath):
    print("File does not exist.")
    exit()

with open(csvpath, "r") as csvreader:
    reader = csv.reader(csvreader, delimiter = ",")
    header = next(reader)
    # turn csv into list, get length of list for total number of votes cast
    list_reader = list(reader)
    len(list_reader)

    for row in list_reader:
        # ballot_list += row[2]
        if row[2]=="Charles Casper Stockham":
            charles_votes +=1
        elif row[2]=="Diana DeGette":
            diana_votes +=1
        elif row[2]=="Raymon Anthony Doane":
            raymon_votes +=1

# function to make percentage and round to 3 places, for votes
def percentage(x):
    percent = x*100
    return str(round(percent,3))+"%"

# get percentages
c_percent = percentage(charles_votes/(charles_votes+diana_votes+raymon_votes))

d_percent = percentage(diana_votes/(charles_votes+diana_votes+raymon_votes))

r_percent = percentage(raymon_votes/(charles_votes+diana_votes+raymon_votes))


# ANSWERS

print("Election Results")
print(banner)
print("Total Votes:",len(list_reader))
print(banner)
print("Charles Casper Stockham:",c_percent, "(",charles_votes,")")
print("Diana DeGette:",d_percent, "(",diana_votes,")")
print("Raymon Anthony Doane:",r_percent, "(",raymon_votes,")")
print(banner)
print("Winner: Diana DeGette")
print(banner)

with open("Class_Materials/personal_repos/python-challenge/PyPoll/analysis/output.txt", "x") as f:
    print("Election Results",file=f)
    print(banner,file=f)
    print("Total Votes:",len(list_reader),file=f)
    print(banner,file=f)
    print("Charles Casper Stockham:",c_percent, "(",charles_votes,")",file=f)
    print("Diana DeGette:",d_percent, "(",diana_votes,")",file=f)
    print("Raymon Anthony Doane:",r_percent, "(",raymon_votes,")",file=f)
    print(banner,file=f)
    print("Winner: Diana DeGette",file=f)
    print(banner,file=f)
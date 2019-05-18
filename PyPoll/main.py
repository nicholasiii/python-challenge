import os
import csv
elections_csv_path = os.path.join("../03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")

votetotal=int(0)
Khanvotes=int(0)
LiVotes=int(0)
CorreyVotes=int(0)
OTooleyVotes=int(0)
khanpercent=float(0)
lipercent=float(0)
correypercent=float(0)
otooleypercent=float(0)
Khan=str("Khan")

with open(elections_csv_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header=next(csvfile)

    for row in csvreader:
        votetotal=votetotal+1
        if row[2]=="Khan":
            Khanvotes=Khanvotes+1
        if row[2]=="Li":
         LiVotes=LiVotes+1
        if row[2]=="Correy":
            CorreyVotes=CorreyVotes+1
        if row[2]=="O'Tooley":
            OTooleyVotes=OTooleyVotes+1
        
khanpercent=Khanvotes/votetotal
lipercent=LiVotes/votetotal
correypercent=CorreyVotes/votetotal
otooleypercent=OTooleyVotes/votetotal

print("Election Results:")
print("-------------------------")
print("Total Votes:         "+str(votetotal))
print("-------------------------")
print("Khan:       "+format(khanpercent, "%")+"       "+str(Khanvotes))
print("Correy:     "+format(correypercent, "%")+"       "+str(CorreyVotes))
print("Li:         "+format(lipercent, "%")+"       "+str(LiVotes))
print("O'Tooley:   "+format(otooleypercent, "%")+"       "+str(OTooleyVotes))
if max(Khanvotes,LiVotes,CorreyVotes,OTooleyVotes)==Khanvotes:
    print("Khan wins!")
if max(Khanvotes,LiVotes,CorreyVotes,OTooleyVotes)==CorreyVotes:
    print("Correy wins!")
if max(Khanvotes,LiVotes,CorreyVotes,OTooleyVotes)==LiVotes:
    print("Li wins!")
if max(Khanvotes,LiVotes,CorreyVotes,OTooleyVotes)==OTooleyVotes:
    print("O'Tooley wins!")

file = open("results.txt","w") 
 
file.write("Election Results:\n")
file.write("-------------------------\n")
file.write("Total Votes:         "+str(votetotal)+"\n")
file.write("-------------------------\n")
file.write("Khan:       "+format(khanpercent, "%")+"       "+str(Khanvotes)+"\n")
file.write("Correy:     "+format(correypercent, "%")+"       "+str(CorreyVotes)+"\n")
file.write("Li:         "+format(lipercent, "%")+"       "+str(LiVotes)+"\n")
file.write("O'Tooley:   "+format(otooleypercent, "%")+"       "+str(OTooleyVotes))

file.close() 
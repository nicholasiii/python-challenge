import os
import csv

months=int(0)
profit_loss=int(0)
average_change=float(0)
profit_change=float(0)
greatestincmonth=str
greatestinc=float(0)
greatestdecmonth=str
greatestdec=float(0)
lastprof=float(0)

budget_csv_path = os.path.join("../03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(budget_csv_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header=next(csvfile)
    print(f"CSV Header: {csv_header}")

#months as int, profit/loss, average change in profit/loss, greatestincrease, greatest decrease
    for row in csvreader:
        months=months+1
        profit_loss=profit_loss+int(row[1])
        if greatestinc<(int(row[1])-lastprof):
            greatestinc=(int(row[1])-lastprof)
            greatestincmonth=row[0]
        if greatestdec>(int(row[1])-lastprof):
            greatestdec=(int(row[1])-lastprof)
            greatestdecmonth=row[0]
        profit_change=int(row[1])-lastprof
        #if statement to keep first profit from counting towards the average
        if lastprof!=0:
            average_change=average_change+profit_change
        lastprof=int(row[1])
average_change=average_change/(months-1)
print("Financial Analysis")
print("-----------------------")
print("Total Months:  "+str(months))
print("Total Profit/Loss:  "+str(profit_loss))
print("Average Monthly Change:    "+str(average_change))
print("Greatest Monthly Increase:  "+greatestincmonth+"   "+str(greatestinc))
print("Greatest Monthly Decrease:   "+greatestdecmonth+"    "+str(greatestdec))


file = open("results.txt","w") 
 
file.write("Financial Analysis\n") 
file.write("-----------------------\n") 
file.write("Total Months:  "+str(months)+"\n") 
file.write("Total Profit/Loss:  "+str(profit_loss)+" \n")
file.write("Average Monthly Change:    "+str(average_change)+"\n")
file.write("Greatest Monthly Increase:  "+greatestincmonth+"   "+str(greatestinc)+"\n")
file.write("Greatest Monthly Decrease:   "+greatestdecmonth+"    "+str(greatestdec)+"\n")

file.close() 

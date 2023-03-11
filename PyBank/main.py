import os
import csv

#Read the csv files from Resources folder and store them into a budgetdata list.
csvfile = open (os.path.join("Resources","budget_data.csv"),'r')
budgetdata = csv.reader(csvfile,delimiter=",")

#skip reading the header in the csv file.
next(budgetdata, None)

#create list
date = []
profitloss = []
changes = []

#Store each date and profit figure into the list.
for row in budgetdata:
    date.append(row[0])
    profitloss.append(int(row[1]))

#Calculate the changes in profit or loss and store them in a list.
for i in range(len(profitloss)-1):
    currentVal = float(profitloss[i])
    nextVal = float(profitloss[i+1])
    changes.append(nextVal-currentVal)

#Calculate the average of the changes in profit and loss.
averageChange = sum(changes)/len(changes)

#Find the index for the greatest increase and decrease in the changes in profit and loss.
greatIncrease = changes.index(max(changes))
greatDecrease = changes.index(min(changes))

#Create the text file or rewrite the text file in analysis folder if exist and write the financial analysis result in it..
f =open(os.path.join("analysis","financial_analysis.txt"),"w+")
f.write ("Financial Analysis\n\n")
f.write ("----------------------------\n\n")
f.write (f"Total Months: {len(date)}\n\n")
f.write (f"Total: ${sum(profitloss)}\n\n")
f.write (f"Average Change: ${round(averageChange,2)}\n\n")
f.write (f"Greatest Increase in Profits: {date[greatIncrease+1]} (${int(changes[greatIncrease])})\n\n")
f.write (f"Greatest Decrease in Profits: {date[greatDecrease+1]} (${int(changes[greatDecrease])})")
f.close()
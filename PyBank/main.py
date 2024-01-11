import csv
import os

csvpath=os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    Total_months=0
    profit=[]
    change=[]
    premonth=0
    for row in csvreader:
        Total_months=Total_months+1
        profit.append(int(row[1]))
        currentmonth=int(row[1])
        if premonth !=0:
            month_change=currentmonth-int(premonth)
            change.append(month_change)
            max_change=max(change)
            min_change=min(change)
            if month_change==max_change:
                max_month=row[0]
            elif month_change==min_change:
                min_month=row[0]
        premonth=row[1]
        
    total_profit=sum(profit)
    avg_change=round((sum(change)/len(change)), 2)

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {Total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

file=("Analysis/pybank.txt")
with open(file, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {Total_months}\n")
    text.write(f"Total: ${total_profit}\n")
    text.write(f"Average Change: ${avg_change}\n")
    text.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    text.write(f"Greatest Decrease in Profits: {min_month} (${min_change})\n")


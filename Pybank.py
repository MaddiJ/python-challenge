# import file
import os
import csv
input_file  = "\Resources\budget_data.csv"
csvpath = os.path.join('..','Resources','budget_data.csv')


#list your variables
# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []
# Open csv in default read mode with context manager
with open(input_file,newline="", encoding="utf-8") as budget:
     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",")
    # Skip the header labels to iterate with the values
    header = next(csvreader)
    # Iterate through the rows in the stored file contents
    for row in csvreader:
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month accordingly using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
#Print Statements
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
#Output files
output_file = os.path.join('..', directory, 'analysis', 'output.txt')
with open(output_file, "w") as file:
    file.write("Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")

# import file
import os, csv 
#import pathlib 
#import path

# declare the location for file using Pathlib

input_file= os.path.join ("Module3Python", "Starter_Code ","Resources","budget_data.csv")
csvpath = "./Resources/budget_data.csv"

#list your variables
total_months=[]
total_profit= []
monthlyprofitchange= [] 


# Open csv in default read mode with context manager
with open(csvpath, "r") as csvfile:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",")
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
        monthlyprofitchange.append(total_profit[i+1]-total_profit[i])
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthlyprofitchange)
max_decrease_value = min(monthlyprofitchange)
# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthlyprofitchange.index(max(monthlyprofitchange)) + 1
max_decrease_month = monthlyprofitchange.index(min(monthlyprofitchange)) + 1
#Print Statements
# Print Statements
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthlyprofitchange)/len(monthlyprofitchange),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
#Output files
# Output files
output_file = "./Analysis/budget_analysis.csv"
with open(output_file,"w") as file:
#Write methods to print to Financial_Analysis_Summary
# Write methods to print to Financial_Analysis_Summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthlyprofitchange)/len(monthlyprofitchange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

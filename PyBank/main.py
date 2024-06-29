# importing libraries needed
import csv
import os
# create variables
month_count = 0  # totalling months
net_calc = 0  # profittracker
greatest_increase = 0  # Greatest increase in profits
greatest_increase_month = ""  # Month of greatest increase
greatest_decrease = 0  # Greatest decrease in profits
greatest_decrease_month = ""  # Month of greatest decrease
value_change = 0
profit_change_list = []


# open the needed csv file
raw_data = os.path.join(".", "Resources", "budget_data.csv")

# create text file for output
data_analysis = os.path.join(".", "analysis", "data_analysis.txt")

# reading csv file
with open (raw_data) as financial_data:
    reader = csv.reader(financial_data)

    # remove header
    header = next(reader)
    month_count += 1
    first_row = next(reader)
    net_calc += int(first_row[1])
    previous_profit = int(first_row[1])
    
    # er = each row
    for er in reader:
        # tracks number of months
        month_count += 1 
        
        # tracks net change
        net_calc = net_calc + int(er[1])
        
        # calc profit change
        profit_change = int(er[1]) - previous_profit
        previous_profit = int(er[1])
        profit_change_list.append(profit_change)
        

        # biggest inc
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_month = er[0]

        # biggest dec
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = er[0]

# print(profit_change_list)
# print(sum(profit_change_list))
# print(len(profit_change_list))
# average = sum(profit_change_list) / len(profit_change_list)

output = (
    f"Data Analysis:\n"
    f"--------------------------------\n"
    f"Total Months:    {month_count}\n"
    f"Total Profit:    {net_calc}\n"
    f"The average is {average}\n"
    f"The month with the greatest increase is {greatest_increase_month} with an increase of ${greatest_increase}\n"
    f"The month with the greatest decrease is {greatest_decrease_month} with an increase of ${greatest_decrease}\n"
)

print(output)     

output_file = os.path.join(".", "analysis", "analysis.txt")

# Write the output to the custom file
with open(output_file, 'w') as file:
    file.write(output)
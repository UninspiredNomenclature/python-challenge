# -*- coding: UTF-8 -*-
"""PyBank Script - Analyzes financial records"""
 
# Import necessary modules
import csv
import os
 
# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
 
# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
dates = []
previous_profit_loss = 0
current_profit_loss = 0
 
# Open and read the CSV file
with open(file_to_load) as financial_data:
    print(financial_data)
    reader = csv.reader(financial_data)
 
    # Skip the header row but store it
    header = next(reader)
    first_data_row = next(reader)
    total_months = 1
    total_net = int(first_data_row[1])
    previous_profit_loss = int(first_data_row[1])
 
    # Loop through remaining rows in the dataset
    for row in reader:
        total_months += 1

        # Convert profit/loss string to integer and add to total
        current_profit_loss = int(row[1])
        total_net += current_profit_loss

        # Calculate change from previous month
        net_change = current_profit_loss - previous_profit_loss

        # Store the date and change in their respective lists
        dates.append(row[0])
        net_change_list.append(net_change)

        # Update previous_profit_loss for next iteration
        previous_profit_loss = current_profit_loss
 
    # Calculate the average net change across the months
    average_change = sum(net_change_list) / len(net_change_list)
 
    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(net_change_list)
    increase_date = dates[net_change_list.index(greatest_increase)]

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(net_change_list)
    decrease_date = dates[net_change_list.index(greatest_decrease)]
    # Add 1 to index because changes list is one shorter than dates list
    
    
 
    # Create the output summary
    output = (
        "\nFinancial Analysis\n"
        "-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net:,}\n"
        f"Average Change: ${average_change:,.2f}\n"
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase:,})\n"
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease:,})\n"
    )
 
    # Print results to terminal
    print(output)
 
    # Write results to text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
    print(f"\nResults have been written to: {file_to_output}")

# Assignment
This Python script analyzes timecard data from an Excel file to extract specific data related to employee work patterns. The analysis focuses on identifying employees who have:
a. Worked for 7 consecutive days.
b. who have less than 10 hours of time between shifts but greater than 1 hour.
c. Who has worked for more than 14 hours in a single shift.

### Prerequisites
Python 3.x
pandas library(command: pip install pandas)

# Timecard Analysis with pandas
This repository contains a Python script that analyzes timecard data to identify various work patterns.

## Prerequisites
Python 3.x
pandas library (pip install pandas)

## Output
The script will print the following information to the console:
Employees who have worked for 7 consecutive days.
Employees who have less than 10 hours of time between shifts but greater than 1 hour.
Employees who have worked for more than 14 hours in a single shift.

## Code Structure
# Function to read the Excel file with specific data types.
read_excel_file_with_header(filename)
# Read the timecard data
df = read_excel_file_with_header('C:/Users/USER/OneDrive/Documents/assignment_eclipse/src/timecard.xlsx')
Section a): Identifies employees who have worked for 7 consecutive days.
Section b): Identifies employees with less than 10 hours between shifts but greater than 1 hour.
Section c): Identifies employees who have worked for more than 14 hours in a single shift.


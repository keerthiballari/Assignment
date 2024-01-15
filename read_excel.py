import pandas as pd

def read_excel_file_with_header(filename):
    df = pd.read_excel(filename, dtype={'File Number': str, 'Timecard Hours (as Time)': str})
    return df

df = read_excel_file_with_header('C:/Users/USER/OneDrive/Documents/assignment_eclipse/src/timecard.xlsx')

# a) Who has worked for 7 consecutive days.

# Convert the Time and Time Out columns to datetime
df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

# Calculate the difference between consecutive dates for each employee
df['Date Diff'] = df.groupby('File Number')['Time'].diff().dt.days

# Identify employees who have worked for 7 consecutive days
result_a = df[df['Date Diff'] == 1].groupby('File Number')['Employee Name'].unique().reset_index()
print("a) Who has worked for 7 consecutive days:")
print(result_a.to_string(index=False))


# Who have less than 10 hours of time between shifts but greater than 1 hour:

# Calculate the time difference between consecutive shifts for each employee
df['Shift Diff'] = (df['Time'] - df.groupby('File Number')['Time Out'].shift()).dt.total_seconds() / 3600

# Identify employees who have less than 10 hours of time between shifts but greater than 1 hour
result_b = df[(df['Shift Diff'] < 10) & (df['Shift Diff'] > 1)].groupby('File Number')['Employee Name'].unique().reset_index()
print("\nb) Who have less than 10 hours of time between shifts but greater than 1 hour:")
print(result_b.to_string(index=False))

# Who has worked for more than 14 hours in a single shift:

# Calculate the duration of each shift for each employee
df['Shift Duration'] = (df['Time Out'] - df['Time']).dt.total_seconds() / 3600

# Identify employees who have worked for more than 14 hours in a single shift
result_c = df[df['Shift Duration'] > 14].groupby('File Number')['Employee Name'].unique().reset_index()
print("\nc) Who has worked for more than 14 hours in a single shift:")
print(result_c.to_string(index=False))
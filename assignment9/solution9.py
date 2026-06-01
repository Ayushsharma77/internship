import pandas as pd
import numpy as np
import re


# PART 1: Regex Patterns


email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[6-9]\d{9}$'
string_pattern = r'^[a-zA-Z\s]+$'

test_email = "test.user@email.com"
test_mobile = "9876543210"
test_string = "Hello World"

print("Email Valid:", bool(re.match(email_pattern, test_email)))
print("Mobile Valid:", bool(re.match(mobile_pattern, test_mobile)))
print("String Valid:", bool(re.match(string_pattern, test_string)))



# PART 2 & 3: Pandas Datetime & CSV Analysis


df = pd.read_csv('sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_of_Week'] = df['Date'].dt.day_name()

print(df.isnull().sum())

df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())
df['Units'] = df['Units'].fillna(0)
df = df.dropna(subset=['Date'])

df['Total_Cost'] = df['Units'] * df['Price']
df['Profit'] = df['Revenue'] - df['Total_Cost']

monthly_revenue = df.groupby('Month')['Revenue'].sum()
print(monthly_revenue)

total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

average_units = np.mean(df['Units'])
print("Average Units Sold:", average_units)

df.to_csv('cleaned_sales_data.csv', index=False)

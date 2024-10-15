from datetime import datetime, timedelta,date

today = datetime.today()

# print(today)
# # Result 10

# # 1.
# print(today.month)
# # Result 10

# # 2.
# print(today.timetuple()[1])
# # Result 10

# # 3.
# print(today.strftime('%m'))
# # Result 10

# # 4
# print(today.isoformat()[5:7])
# # Result 10

# # 5 
# print(datetime.fromisoformat(str(today)).month)
# # Result 10

# # 6
# print(datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S.%f').month)
# # Result 10


# #####################################################################################



# Basic Exercises:
# Get today's date: Write a program to display the current date using datetime.date.today().

today = datetime.today()

# Extract year, month, and day: Given the current date, extract and print the year, month, and day separately.

year, month, day = today.year, today.month, today.day
print(year, month, day )

# Format date as a string: Convert today's date into a string with the format YYYY/MM/DD.

today_string = today.strftime('%Y/%m/%d')
print(f"{today_string}, is a {type(today_string)}")

# Parse a date string: Given a date string '2024-10-10', parse it into a datetime object using strptime.

given_string = '2024-10-10'

parsed_string = datetime.strptime(given_string, '%Y-%m-%d')

print(f"{parsed_string}, is a {type(parsed_string)}")

# Get the current time: Display the current local time.

current_time = datetime.now()

print(current_time)
# Create a specific date: Create a datetime object for the date January 1, 2020, and display it.

specific_date = date(2020, 1, 1 )
print(specific_date)

# Difference between two dates: Calculate the number of days between today and December 25, 2024.

date_december = date(2024, 12, 5)

differnce = today.date() - date_december

print(differnce)
# Add days to the current date: Add 7 days to today’s date and display the result.

today_plus_7days = today + timedelta(days=7)

print(today_plus_7days)
# Subtract time: Given a datetime object representing the current time, subtract 3 hours and display the new time.

today_less_3_hours = today - timedelta(hours=3)
print(today_less_3_hours)

# Weekday of a specific date: Find out which day of the week July 4, 2022, falls on.
date_july_2022 = date(2022, 7,4)

print(date_july_2022.isoweekday())

# Intermediate Exercises:
# Find the last day of the current month: Write a program that determines the last day of the current month.

def last_day_current_month(thisdate: datetime) -> datetime:

    year = thisdate.year
    month = thisdate.month +1
    day = 1

    new_date = date(year, month, day) - timedelta(1)

    return new_date

last_day_mounth_today = last_day_current_month(today)
print(last_day_mounth_today)

# Convert timestamp to date: Given a Unix timestamp (e.g., 1694342400), convert it to a human-readable date.

date_from_timestamp = datetime.fromtimestamp(1694342400)
print(date_from_timestamp)

# Find the difference in timezones: Calculate the difference in hours between two timezones, e.g., New York (UTC-5) and Tokyo (UTC+9).

# Calculate the age: Given a date of birth (e.g., '1990-05-15'), calculate the exact age in years, months, and days.

# Round to the nearest hour: Write a function that rounds the current time to the nearest hour.

# Convert a naive datetime to aware: Convert a naive datetime object to an aware datetime using a specific timezone (e.g., UTC or US/Eastern).

# Time until the next event: Calculate the number of days, hours, and minutes left until New Year's Eve (December 31, 2024, 23:59:59).

# Difference between two datetime objects with timezone: Given two datetime objects in different timezones (e.g., UTC and US/Pacific), calculate the time difference in hours and minutes.

# Check if a date is valid: Write a function that takes a string in the format YYYY-MM-DD and returns whether it is a valid date.

# Get the number of days in a specific month and year: Write a program that accepts a month and a year as input and returns the number of days in that month.


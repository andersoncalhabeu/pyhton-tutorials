# --------------------------------------------
# Tutorial: Working with dates and times in Python
# Author: [Your Name]
# --------------------------------------------

# The datetime module is used for manipulating dates and times.
import datetime

# ============================================================
# 1. The datetime.date object (date only)
# ============================================================

# Creating a specific date (year, month, day)
date1 = datetime.date(2025, 8, 18)
print("Specific date:", date1)

# Today's date
today = datetime.date.today()
print("Today's date:", today)

# Accessing date attributes
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# ============================================================
# 2. The datetime.time object (time only)
# ============================================================

time1 = datetime.time(14, 30, 45)  # hour, minute, second
print("\nSpecific time:", time1)

print("Hour:", time1.hour)
print("Minute:", time1.minute)
print("Second:", time1.second)

# ============================================================
# 3. The datetime.datetime object (date + time)
# ============================================================

# Creating a specific datetime
dt1 = datetime.datetime(2025, 8, 18, 21, 7, 0)
print("\nSpecific datetime:", dt1)

# Current date and time (system)
now = datetime.datetime.now()
print("Current date and time:", now)

# Only the date or only the time
print("Date only:", now.date())
print("Time only:", now.time())

# ============================================================
# 4. Operations with dates and times (timedelta)
# ============================================================

# timedelta allows us to add or subtract periods of time
delta = datetime.timedelta(days=7, hours=3)
print("\nTime delta:", delta)

# Adding and subtracting from a datetime
one_week_later = now + datetime.timedelta(days=7)
one_week_ago = now - datetime.timedelta(days=7)

print("One week later:", one_week_later)
print("One week ago:", one_week_ago)

# Difference between two dates
diff = one_week_later - now
print("Difference between dates:", diff)

# ============================================================
# 5. Date formatting and string parsing
# ============================================================

# Formatting with strftime
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print("\nFormatted date:", formatted)

# Main codes:
# %d = day | %m = month | %Y = year | %H = hour(24h) | %M = minute | %S = second

# Converting string to datetime (strptime)
date_str = "25/12/2025 18:30:00"
dt_converted = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
print("String converted to datetime:", dt_converted)

# ============================================================
# 6. Working with time zones (timezone)
# ============================================================

# For time zones, we use timezone with UTC offset
import pytz  # install with: pip install pytz

utc = datetime.datetime.now(datetime.timezone.utc)
print("\nNow in UTC:", utc)

# Converting UTC to another timezone (Example: São Paulo)
sp_tz = pytz.timezone("America/Sao_Paulo")
now_in_sp = utc.astimezone(sp_tz)
print("Now in São Paulo:", now_in_sp)

# ============================================================
# 7. Practical exercise
# ============================================================
# Goal: calculate how many days are left until New Year's

current_year = today.year
new_year = datetime.date(current_year + 1, 1, 1)
days_left = new_year - today
print(f"\n{days_left.days} days left until New Year!")
# ============================================================
# End of the datetime tutorial
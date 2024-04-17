from datetime import datetime


def calculate_time_difference(event_date):
    current_date = datetime.now().date()
    event_date = datetime.strptime(event_date, "%Y-%m-%d").date()
    time_difference = current_date - event_date
    return time_difference


# Get current date
current_date_str = input("Enter the current date (YYYY-MM-DD): ")

# Get event dates
event_dates = [
    ("Napoleon Bonaparte's birthdate (Aug 15, 1769)", "1769-08-15"),
    ("The bombing of Pearl Harbor (Dec 7, 1941)", "1941-12-07"),
    ("The Wright Brothers 1st flight (Dec 17, 1903)", "1903-12-17")
]

# Calculate and print time differences
for event_name, event_date in event_dates:
    time_difference = calculate_time_difference(event_date)
    print(f"Time difference between {event_name} and the current date ({current_date_str}): {time_difference}")

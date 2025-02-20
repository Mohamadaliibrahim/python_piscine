import time
import datetime

epoch_time = time.time()

# print(epoch_time)

formatted_time = f"{epoch_time:,.4f}"

# print(formatted_time)

scientific_notation = f"{epoch_time:.2e}"

# print(scientific_notation)

# Get the current time in the specified format
formatted_date = datetime.datetime.now().strftime("%b %d %Y")

# datetime.datetime.now() give you the current local date and also includes the time (hours, minutes, seconds, and even microseconds).
# strftime() function converts that date and make it a string in a formated way.
# print (datetime.datetime.now())

print(f"Seconds since January 1, 1970: {formatted_time} or {scientific_notation} in scientific notation$")
print(formatted_date)

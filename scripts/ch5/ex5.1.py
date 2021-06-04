import time

epoch = time.time()

# Days
secsOfaday = 24 * 60 * 60
days = epoch // secsOfaday

# Hours
seconds_remainder = epoch % secsOfaday
hours = seconds_remainder // (60 * 60)

# Minutes
seconds_remainder = seconds_remainder % (60 * 60)
minutes = seconds_remainder // 60

# Seconds
seconds = seconds_remainder % 60

# Print
print("\nDays:", days, "\nHours:", hours, "\nMinutes:", minutes, "\nSeconds:", seconds)

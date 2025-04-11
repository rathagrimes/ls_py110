# 1. Translate into hours and minutes
# 2. If greater than 24, subtract 24 until it's less
# 3. If less than zero, add 24 until it's more
# 4. Format

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

def time_of_day(num_minutes):
    hours = num_minutes // MINUTES_PER_HOUR
    mins = num_minutes % MINUTES_PER_HOUR
    while hours > HOURS_PER_DAY:
        hours -= HOURS_PER_DAY
    while hours < 0:
        hours += HOURS_PER_DAY
    return f"{hours:02d}:{mins:02d}"


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

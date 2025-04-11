HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def parse_hours_and_mins(string):
    hours, minutes = [int(v) for v in string.split(':')]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def after_midnight(string):
    return parse_hours_and_mins(string)

def before_midnight(string):
    mins = parse_hours_and_mins(string)
    return (MINUTES_PER_DAY - mins) % MINUTES_PER_DAY

# print(parse_hours_and_mins("00:00")) #0
# print(parse_hours_and_mins("12:34")) #754
# print(parse_hours_and_mins("24:00")) #1440

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

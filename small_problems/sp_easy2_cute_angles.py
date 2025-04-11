import math

def dms(angle_in_decimal):
    degree = math.floor(angle_in_decimal)
    minutes = seconds = 0
    minutes_in_decimal = (angle_in_decimal - degree) * 60
    minutes = math.floor(minutes_in_decimal)
    seconds_in_decimal = (minutes_in_decimal - minutes) * 60
    seconds = math.floor(seconds_in_decimal)

    # correct for range
    while degree > 360:
        degree -= 360
    while degree < 0:
        degree += 360

    return f"{degree}°{minutes:02}'{seconds:02}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# print(dms(-1) == "-1°00'00\"")
# print(dms(400) == "400°00'00\"")
# print(dms(-40) == "-40°00'00\"")
# print(dms(-420) == "-420°00'00\"")

print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) == "320°00'00\"")
print(dms(-420) == "300°00'00\"")

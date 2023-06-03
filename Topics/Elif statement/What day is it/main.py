reference = 10.5  # on Tuesday
offset = int(input())

if reference + offset < 0:      # previous day
    print("Monday")
elif reference + offset > 24:   # next day
    print("Wednesday")
else:                           # current day
    print("Tuesday")

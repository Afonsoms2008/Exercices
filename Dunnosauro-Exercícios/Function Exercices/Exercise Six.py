def convert_time(hours, minutes):
    if hours >= 12:
        period = "P"
    else:
        period = "A"

    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    return hours, minutes, period


def display_time(hours, minutes, period):
    print(f"{hours}:{minutes:02d} {period}.M.")


while True:
    hour = int(input("Enter hours: "))
    minute = int(input("Enter minutes: "))

    hour, minute, period = convert_time(hour, minute)

    display_time(hour, minute, period)
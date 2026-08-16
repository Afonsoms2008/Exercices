
months = {1 : "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10:"October",
        11: "November",
        12: "December"}


date_input = input("Enter your birthday in the DD/MM/YYYY format: ")
day, month, year = date_input.split("/")
day, month, year = int(day) ,int(month) ,int(year)
print(f"You were born on the {day} of {months[month]} of {year}")
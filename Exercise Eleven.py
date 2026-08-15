def date(day,month,year):
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
    date_output = (f"{day} of {months[month]} of {year}")
    print(date_output)
    return date_output

date_input = input("Enter de date of today in the DD/MM/YYYY format: ")
day, month, year = date_input.split("/")
day, month, year = int(day) ,int(month) ,int(year)
date(day,month,year)
#[2, 6, 8, 9]
date = "6/13/2023"
dateParts = date.split("/")
print(dateParts)
day = dateParts[0]
month = dateParts[1]
year = dateParts[2]
print(f"Day: {day}\n", f"Month: {month}\n", f"Year: {year}", sep="")
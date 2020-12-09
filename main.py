# Python csv library for data processing and data analysis:
import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = list()
    for row in data:
        # Exclude the 1st string item in the list:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

print("")
print("Printing all contents:")
data = pandas.read_csv("weather_data.csv")
print(data)

print("")
print("Printing day column as a list:")
print(data["day"].to_list())

print("")
print("Converting to dict()")
data_dict = data.to_dict()
print(data_dict)
print("")

print('''
Challenge: Calculate the avg temp in weather_data.csv
''')

# 1. Reading weather_data.csv using pandas lib:
weather_data = pandas.read_csv("weather_data.csv")

# 2. Converting "temp" column to list:
temp_list = weather_data["temp"].to_list()

# 3. Calculating "temp" average:
from math import ceil

# Using Vanilla Python:
temp_avg = sum(temp_list) / len(temp_list)
print(round(temp_avg, 2))


# Using pandas:
avg_temp = weather_data["temp"].mean()
print(round(avg_temp, 2))

print('''

Challenge: Calculate the max temp value in weather_data.csv
''')
# Vanilla Python:
temp_list = weather_data["temp"].to_list()
max_temp = max(temp_list)
print(max_temp)
print("")
# Using pandas
temp_max = weather_data["temp"].max()
print(temp_max)

print('''
Printing day column:
''')
print(weather_data.day)

print('''
Extracting a row from weather_data.csv
''')
monday_row = weather_data[weather_data.day == "Monday"]
print(monday_row)

print('''

Challenge: Calculate the max temp DAY of the week in weather_data.csv
''')
max_day = weather_data[weather_data.temp == weather_data.temp.max()]
# OR:
max_temp = weather_data[weather_data["temp"] == weather_data["temp"].max()]
print(max_day)
print("")
print(max_temp)

print("")
print("===============================")
print("")

sunday = weather_data[weather_data.day == "Sunday"]
print(sunday.condition)

print('''

Challenge: Extract Monday temperature in F

''')

# Extracting Monday temperature:
monday_temp = monday_row["temp"]

# Converting temp C to F:
print(monday_temp * (9 / 5) + 32)

print("")
print("===============================")
print("")

# Creating a data frame from scratch:
data_marks = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Create a data frame:
data_frame_marks = pandas.DataFrame(data_marks)
print(data_frame_marks)
data_frame_marks.to_csv("new_data.csv")



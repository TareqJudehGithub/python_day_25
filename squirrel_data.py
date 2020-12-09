import csv
import pandas


# Extract squirrels Primary Fur Color

# Converting Squirrel_Data.csv to Python using pandas lib:

squirrel_data = pandas.read_csv("Squirrel_Data.csv")

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

print("")
# Creating data frame:
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

squirrel_data_frame = pandas.DataFrame(data_dict)
print(squirrel_data_frame)

# Converting data_frame table to .csv:
squirrel_data_frame.to_csv("squirrels_count.csv")

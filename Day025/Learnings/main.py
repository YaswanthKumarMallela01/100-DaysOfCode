# import csv

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

'''If we wanted to read any csv file then pandas is perfect because the data is nicely formatted
and the columns and rows in the data can be easily accessible and the code is minimal and easily 
understandable.'''
data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()  # Converts all the content in the data into dictionary format
print(data_dict)

'''Series is nothing but a particular column in the data. Here 'temp' is a particular column in
weather_data'''
temp_list = data["temp"].to_list()  # Converting series into list
print(temp_list)

'''Pandas has inbuilt methods like max, min, mean, median, mode, average etc.. Refer to pandas
documentation for more methods as pandas is one of the best and perfectly documented 
packages out there in python.'''
print(f"Average of temp: {data["temp"].mean()}")
print(f"Maximum of temp: {data["temp"].max()}")

# Get data in columns
print(data.condition)  # Can also be written as data["condition"]

# Get data in row
print(data[data["day"] == "Monday"])  # Returns the complete data from a row where day column has value Monday
print(data[data.temp == data.temp.max()])  # Returns the complete data from a row where there is a maximum temperature

'''Converting temperature of Monday from Celsius to Fahrenheit'''
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(f"Monday temp in F: {monday_temp_F}")

'''Dataframe is a two-dimensional, mutable, tabular data structure with labeled axes
(rows and columns). It is the primary data structure in the Pandas library for data 
manipulation and analysis in Python.'''
data_dict = {
    "Students": ["Yaswanth", "Vivek", "Akash"],
    "Scores": [85, 95, 98]
}

data_dict_dataframe = pandas.DataFrame(data_dict)
print(data_dict_dataframe)
data_dict_dataframe.to_csv("student_data.csv")

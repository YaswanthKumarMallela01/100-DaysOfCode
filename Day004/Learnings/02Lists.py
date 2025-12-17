import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])  # Prints the 1st state
print(states_of_america[-1])  # Prints the last state

states_of_america[1] = "Pencilvania"  # Changes from "Pennsylvania" to "Pencilvania" in the original list

states_of_america.append("JohnnyLand")  # Adds the new state at the end of the original list
states_of_america.extend(["LaLaLand", "ChocolateLand"])  # Extends the existing list with new list

#  There are so many other functions related to Lists data structure. Explore them from the internet

#  --------------> Who will pay the bills?

persons = ["Jesse", "Skyler", "Gus", "Heisenberg", "Hank"]
print(f"{random.choice(persons)} has to pay the bills.")
#  Give the random choice of a person from the list

#  --------------> Nested Lists

vegetables = ["Carrot", "Cabbage", "Capsicum", "Potato", "Brinjal"]
fruits = ["Apple", "Banana", "Kiwi", "Orange", "DragonFruit"]

eateries = [vegetables, fruits]
print(eateries)

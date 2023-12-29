from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
import pandas as pd
# import plotly.express as px
# from plotly.io import show

from fastf1.ergast import Ergast

ergast = Ergast()
races = ergast.get_race_schedule(2023)  # Races in year 2022
results = []
drivers = []


class driver_stats:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.points = []
        self.points_sum = 0
        self.points_sum_record = [0]
    def __str__(self):
         # ANSI escape code for green text
        green_code = "\033[92m"

        # ANSI escape code to reset text color
        reset_code = "\033[0m"

        # Construct the string with green points_sum and points array
        return f"\n{self.name}, {self.number}\n" \
               f"{green_code}Points Sum: {self.points_sum}{reset_code}\n" \
               f"Points per Round: {self.points}\n" \
               f"Points Sum Record: {self.points_sum_record}"
    
    def plot_points(self):
        plt.plot(range(1, len(self.points) + 2), self.points_sum_record, marker='o')
        plt.title(f"{self.name}'s Points")
        plt.xlabel("Index")
        plt.ylabel("Points")
        plt.show()

lando = driver_stats("Lando Norris", 4)
oscar = driver_stats("Oscar Piastri", 81)
charles = driver_stats("Charles Leclerc", 16)


# For each race in the season
for rnd, race in races['raceName'].items():

    if rnd >= 9:
        temp = ergast.get_race_results(season=2023, round=rnd + 1)
        temp = temp.content[0]
        print(temp)
        temp2 = temp.filter(items=['number', 'position', 'points'])
        for driver in temp2['number']:
            if (driver == 4):
                idx = temp2[temp2['number'] == driver].index[0]
                lando.points_sum += temp2.iloc[idx]['points']
                lando.points.append(temp2.iloc[idx]['points'])
                lando.points_sum_record.append(lando.points_sum)

            elif (driver == 81):
                idx = temp2[temp2['number'] == driver].index[0]
                oscar.points_sum += temp2.iloc[idx]['points']
                oscar.points.append(temp2.iloc[idx]['points'])
                oscar.points_sum_record.append(oscar.points_sum)

            elif (driver == 16):
                idx = temp2[temp2['number'] == driver].index[0]
                charles.points_sum += temp2.iloc[idx]['points']
                charles.points.append(temp2.iloc[idx]['points'])
                charles.points_sum_record.append(charles.points_sum)
    else:
        continue

print(lando)
print(oscar)
print(charles)
lando.plot_points()


    # # If there is a sprint, get the results as well
    # sprint = ergast.get_sprint_results(season=2023, round=rnd + 1)
    # if sprint.content and sprint.description['round'][0] == rnd + 1:
    #     temp = pd.merge(temp, sprint.content[0], on='driverCode', how='left')
    #     # Add sprint points and race points to get the total
    #     temp['points'] = temp['points_x'] + temp['points_y']
    #     temp.drop(columns=['points_x', 'points_y'], inplace=True)

    # # Add round no. and grand prix name
    # temp['round'] = rnd + 1
    # temp['race'] = race.removesuffix(' Grand Prix')
    # temp = temp[['round', 'race', 'driverCode', 'points']]  # Keep useful cols.
    # results.append(temp)

# Append all races into a single dataframe
# results = pd.concat(results)
# races = results['race'].drop_duplicates()
# print(results)
print("")

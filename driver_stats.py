from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
import pandas as pd
# import plotly.express as px
# from plotly.io import show

from fastf1.ergast import Ergast

class driver_stats:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.points = []
        self.points_sum = 0
        self.points_sum_record = []
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
    
    def plot_points_sum(self):
        plt.plot(range(1, len(self.points) + 2), self.points_sum_record, marker='o')
        plt.title(f"{self.name}'s Points")
        plt.xlabel("Index")
        plt.ylabel("Points")
        plt.show()
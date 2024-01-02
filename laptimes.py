# For a given team, plot their laptimes at a particular race over the last 5 years in the form of a violin plot
import fastf1
import fastf1.plotting
import seaborn as sns
from matplotlib import pyplot as plt

# The misc_mpl_mods option enables minor grid lines which clutter the plot
fastf1.plotting.setup_mpl(misc_mpl_mods=False)

# '2013': '#00d2be', '2014': '#00d2be', '2015': '#00d2be', '2016': '#00d2be', '2017': '#00d2be', '2018': '#00d2be',
MERC_PALETTE = {'2019': '#00d2be', '2020': '#00d2be', '2021': '#00d2be',
             '2022': '#00d2be', '2023': '#00d2be'}
# MERC_PALETTE = {'2018': '#00d2be'}

# Years - in this case, the years that Mercedes have existed
# 2013, 2014, 2015, 2016, 2017, 2018, 
years = [2019, 2020, 2021, 2022, 2023]
# years = [2018]

all_laps = []

# create the figure
fig, ax = plt.subplots(figsize=(20, 10))

for idx, year in enumerate(years):
    # Load the race
    race =fastf1.get_session(year, 'Bahrain', 'R')
    race.load()

    team_laps = race.laps.pick_driver('HAM').pick_quicklaps().reset_index()
    team_laps["LapTime(s)"] = team_laps["LapTime"].dt.total_seconds()
    team_laps["Driver"] = year.__str__()

    sns.violinplot(data=team_laps,
                x="Driver",
                y="LapTime(s)",
                inner=None,
                scale="area",
                order=years,
                palette=MERC_PALETTE,
                )
    if idx == 0:
        sns.swarmplot(data=team_laps,
                    x="Driver",
                    y="LapTime(s)",
                    order=years,
                    hue="Compound",
                    palette=fastf1.plotting.COMPOUND_COLORS,
                    hue_order=["SOFT", "MEDIUM", "HARD"],
                    linewidth=0,
                    size=5,
                    )
    else:
        sns.swarmplot(data=team_laps,
                    x="Driver",
                    y="LapTime(s)",
                    order=years,
                    hue="Compound",
                    palette=fastf1.plotting.COMPOUND_COLORS,
                    hue_order=["SOFT", "MEDIUM", "HARD"],
                    legend=False,
                    linewidth=0,
                    size=5,
                    )




ax.set_xlabel("Year")
ax.set_ylabel("Lap Time (s)")
plt.suptitle("Hamilton Lap Times at Bahrain Grand Prix" + "\n" + f"Years: {years[0]}" + " - " + f"{years[-1]}")
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()

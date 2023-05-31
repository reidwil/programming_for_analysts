from league.api import get_summoner_data
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data):
    for team, players in data.items():
        kills = []
        deaths = []
        assists = []
        player_names = []
        
        for player, stats in players.items():
            player_names.append(player)
            kills.append(stats['kills'])
            deaths.append(stats['deaths'])
            assists.append(stats['assists'])
        
        # Create a figure and a set of subplots
        _, ax = plt.subplots()

        # Adjust the positions of the bars
        x = np.arange(len(player_names))
        bar_width = 0.3

        bar1 = ax.bar(x - bar_width, kills, width=bar_width, color='b', align='center', label='kills')
        bar2 = ax.bar(x, deaths, width=bar_width, color='r', align='center', label='deaths')
        bar3 = ax.bar(x + bar_width, assists, width=bar_width, color='g', align='center', label='assists')

        # Adding the numbers at the top of each bar
        for bar in [bar1, bar2, bar3]:
            for rect in bar:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2, height,
                        f'{int(height)}', ha='center', va='bottom')

        # Setting the x-axis as player names
        ax.set_xticks(x)
        ax.set_xticklabels(player_names)
        
        # Adding legend
        ax.legend()
        
        # Setting labels for the axes
        ax.set_xlabel('Players')
        ax.set_ylabel('Count')

        # Setting the title
        ax.set_title(f'Stats for {team}')

        # Finally displaying the plot
        plt.show()

def plot(data):
    # Assuming data is your JSON object with match data
    plot_data(data)

if __name__ == "__main__":
    data = get_summoner_data()[0]
    plot(data)
import sys
from league.api import get_summoner_data
from league.graph import plot

def run():
    data = get_summoner_data()[0]
    plot(data)

if __name__=='__main__':
    sys.exit(run())
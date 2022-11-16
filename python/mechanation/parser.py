import argparse
from player import Pilot

def parse_arguments():
  parser = argparse.ArgumentParser(description='This is the parser')
  parser.add_argument('--health', type=int,
    help='Integer amount of a mechs health')
  
  args = parser.parse_args()
  pilot = Pilot(health=args.health)
  print(pilot.health)

if __name__=='__main__':
    parse_arguments()
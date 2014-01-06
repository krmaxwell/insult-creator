import argparse
import random

columnA = ['lazy', 'stupid', 'insecure', 'idiotic', 'slimy', 'slutty', 'smelly', 'pompous',
           'communist', 'dicknose', 'pie-eating', 'racist', 'elitist', 'white trash', 'drug-loving',
           'butterface', 'tone deaf', 'ugly', 'creepy']
columnB = ['douche', 'ass', 'turd', 'rectum', 'butt', 'cock', 'shit', 'crotch', 'bitch', 'turd',
           'prick', 'slut', 'taint', 'fuck', 'dick', 'boner', 'shart', 'nut', 'sphincter']
columnC = ['pilot', 'canoe', 'captain', 'pirate', 'hammer', 'knob', 'box', 'jockey', 'nazi',
           'waffle', 'goblin', 'blossom', 'biscuit', 'clown', 'socket', 'monster', 'hound', 
           'dragon']

parser = argparse.ArgumentParser(description='Create random insults')
parser.add_argument('runs', metavar='N', type=int, default=1, nargs='?', 
                    help='Number of insults to create')
args = parser.parse_args()

for i in range(0, args.runs):
    print random.choice(columnA) + ' ' + random.choice(columnB) + ' ' + random.choice(columnC)

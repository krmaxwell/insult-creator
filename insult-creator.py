import random

columnA = ['lazy', 'stupid', 'insecure', 'idiotic', 'slimy', 'slutty', 'smelly', 'pompous',
           'communist', 'dicknose', 'pie-eating', 'racist', 'elitist', 'white trash', 'drug-loving',
           'butterface', 'tone deaf', 'ugly', 'creepy']
columnB = ['douche', 'ass', 'turd', 'rectum', 'butt', 'cock', 'shit', 'crotch', 'bitch', 'turd',
           'prick', 'slut', 'taint', 'fuck', 'dick', 'boner', 'shart', 'nut', 'sphincter']
columnC = ['pilot', 'canoe', 'captain', 'pirate', 'hammer', 'knob', 'box', 'jockey', 'nazi',
           'waffle', 'goblin', 'blossom', 'biscuit', 'clown', 'socket', 'monster', 'hound', 
           'dragon']

print random.choice(columnA) + ' ' + random.choice(columnB) + ' ' + random.choice(columnC)

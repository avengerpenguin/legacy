import csv


traits = ['Strength', 'Magic', 'Shadow', 'Influence', 'Wealth', 'Knowlegdge']
classes = ['Warrior', 'Wizard', 'Rogue', 'Patrician', 'Merchant', 'Scholar']


with open('eggs.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for t1, c1 in zip(traits, classes):
        for t2, c2 in zip(traits, classes):
            if t1 == t2:
                continue
            writer.writerow([
                'Opportunity',
                'icons/orb-direction.svg',
                'An opportunity arises. Starting with the highest, each player with 10 or more {t1} may choose to place this card in front of them for +10 {t1}. The player that does is now known as a {c1}. If no player chooses to do this, then place front of all players for a +10 {t2} bonus to all players with 10 or more {t2}, who each gain the title of {c2}.'.format(**locals()),
            ])

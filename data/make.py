import csv


traits = ['Strength', 'Magic', 'Shadow', 'Influence', 'Wealth', 'Knowledge']

with open('it-generated.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for trait in traits:
        writer.writerow([
            title,icon,temp_title,temp_bonus,temp_type,
            perm_title,perm_bonus,perm_type
        ])


classes = ['Warrior', 'Wizard', 'Rogue', 'Patrician', 'Merchant', 'Scholar']
specialisms = {
    'Warrior': {
        'Magic': 'Cleric',#
        'Shadow': 'Revolutionary',#
        'Influence': 'General',
        'Wealth': 'Mercenary',
        'Knowledge': 'Weaponsmith',
    },
    'Wizard': {
        'Strength': 'Battle Mage',#
        'Shadow': 'Dark Sorcerer',
        'Influence': 'Prophet',
        'Wealth': 'High Chancellor',
        'Knowledge': 'Professor of Magic',
    },
    'Rogue': {
        'Strength': 'Assassin',
        'Magic': 'Trickster',
        'Influence': 'Crime Boss',
        'Wealth': 'Thief',
        'Knowledge': 'Mad Scientist',
    },
    'Patrician': {
        'Strength': 'Knight',#
        'Magic': 'Minister for Magic',
        'Shadow': 'Usurper',
        'Wealth': 'Politician',
        'Knowledge': 'Minister for the Arts',
    },
    'Merchant': {
        'Strength': 'Private General',
        'Magic': 'Magic Dealer',
        'Shadow': 'Monopolist',#
        'Influence': 'Lobbyist',#
        'Knowledge': 'Patron',#
    },
    'Scholar': {
        'Strength': 'Martial Artist',
        'Magic': 'Alchemist',#
        'Shadow': 'Art Forger',
        'Influence': 'Artist in Residence',#
        'Wealth': 'Inventor',#
    },
}


# titles = set()
# for title, x in specialisms.items():
#     for trait, special_title in x.items():
#         title_trait = traits[classes.index(title)]
#         titles.add((title, trait, special_title, title_trait))
#
#
# from itertools import product
# title_pairs = product(titles, titles)
#
# legacies = {
#     'Legacy for {} or {}'.format(title1[2], title2[2]): [title1[2], title2[2]]
#     for title1, title2 in title_pairs if title1[
#         0] != title2[0] and len({title1[1], title2[1], title1[3], title2[
#     3]}) == 3 and title1[2] < title2[2]
# }
# print(len(legacies))
# import json
# print(json.dumps(legacies, indent=2, sort_keys=True))
#
# legacies = {
#     'Great Work of Art': ['Artist in Residence', 'Patron'],
#     'Scientific Discovery': ['Alchemist', 'Inventor'],
#     'Dragon Slayer': ['Battle Mage', 'Knight'],
#     'Great Merchant': ['Monopolist', 'Lobbyist'],
#     'Coup Leader': ['Usurper', 'Revolutionary'],
#     'New Leader': ['Politician', ''],
#     'War Hero': ['General', 'Battle Mage'],
# }

legacies = {
    "Legacy for Alchemist or Battle Mage": [
        "Alchemist",
        "Battle Mage"
    ],
    "Legacy for Alchemist or Cleric": [
        "Alchemist",
        "Cleric"
    ],
    "Legacy for Alchemist or Dark Sorcerer": [
        "Alchemist",
        "Dark Sorcerer"
    ],
    "Legacy for Alchemist or High Chancellor": [
        "Alchemist",
        "High Chancellor"
    ],
    "Legacy for Alchemist or Mad Scientist": [
        "Alchemist",
        "Mad Scientist"
    ],
    "Legacy for Alchemist or Magic Dealer": [
        "Alchemist",
        "Magic Dealer"
    ],
    "Legacy for Alchemist or Minister for Magic": [
        "Alchemist",
        "Minister for Magic"
    ],
    "Legacy for Alchemist or Minister for the Arts": [
        "Alchemist",
        "Minister for the Arts"
    ],
    "Legacy for Alchemist or Patron": [
        "Alchemist",
        "Patron"
    ],
    "Legacy for Alchemist or Prophet": [
        "Alchemist",
        "Prophet"
    ],
    "Legacy for Alchemist or Trickster": [
        "Alchemist",
        "Trickster"
    ],
    "Legacy for Alchemist or Weaponsmith": [
        "Alchemist",
        "Weaponsmith"
    ],
    "Legacy for Art Forger or Assassin": [
        "Art Forger",
        "Assassin"
    ],
    "Legacy for Art Forger or Crime Boss": [
        "Art Forger",
        "Crime Boss"
    ],
    "Legacy for Art Forger or Dark Sorcerer": [
        "Art Forger",
        "Dark Sorcerer"
    ],
    "Legacy for Art Forger or Minister for the Arts": [
        "Art Forger",
        "Minister for the Arts"
    ],
    "Legacy for Art Forger or Monopolist": [
        "Art Forger",
        "Monopolist"
    ],
    "Legacy for Art Forger or Patron": [
        "Art Forger",
        "Patron"
    ],
    "Legacy for Art Forger or Professor of Magic": [
        "Art Forger",
        "Professor of Magic"
    ],
    "Legacy for Art Forger or Revolutionary": [
        "Art Forger",
        "Revolutionary"
    ],
    "Legacy for Art Forger or Thief": [
        "Art Forger",
        "Thief"
    ],
    "Legacy for Art Forger or Trickster": [
        "Art Forger",
        "Trickster"
    ],
    "Legacy for Art Forger or Usurper": [
        "Art Forger",
        "Usurper"
    ],
    "Legacy for Art Forger or Weaponsmith": [
        "Art Forger",
        "Weaponsmith"
    ],
    "Legacy for Artist in Residence or Crime Boss": [
        "Artist in Residence",
        "Crime Boss"
    ],
    "Legacy for Artist in Residence or General": [
        "Artist in Residence",
        "General"
    ],
    "Legacy for Artist in Residence or Knight": [
        "Artist in Residence",
        "Knight"
    ],
    "Legacy for Artist in Residence or Lobbyist": [
        "Artist in Residence",
        "Lobbyist"
    ],
    "Legacy for Artist in Residence or Mad Scientist": [
        "Artist in Residence",
        "Mad Scientist"
    ],
    "Legacy for Artist in Residence or Minister for Magic": [
        "Artist in Residence",
        "Minister for Magic"
    ],
    "Great Work of Art": [
        "Artist in Residence",
        "Patron"
    ],
    "Legacy for Artist in Residence or Politician": [
        "Artist in Residence",
        "Politician"
    ],
    "Legacy for Artist in Residence or Professor of Magic": [
        "Artist in Residence",
        "Professor of Magic"
    ],
    "Legacy for Artist in Residence or Prophet": [
        "Artist in Residence",
        "Prophet"
    ],
    "Legacy for Artist in Residence or Usurper": [
        "Artist in Residence",
        "Usurper"
    ],
    "Legacy for Artist in Residence or Weaponsmith": [
        "Artist in Residence",
        "Weaponsmith"
    ],
    "Legacy for Assassin or Battle Mage": [
        "Assassin",
        "Battle Mage"
    ],
    "Legacy for Assassin or Cleric": [
        "Assassin",
        "Cleric"
    ],
    "Legacy for Assassin or Dark Sorcerer": [
        "Assassin",
        "Dark Sorcerer"
    ],
    "Legacy for Assassin or General": [
        "Assassin",
        "General"
    ],
    "Legacy for Assassin or Knight": [
        "Assassin",
        "Knight"
    ],
    "Legacy for Assassin or Martial Artist": [
        "Assassin",
        "Martial Artist"
    ],
    "Legacy for Assassin or Mercenary": [
        "Assassin",
        "Mercenary"
    ],
    "Legacy for Assassin or Monopolist": [
        "Assassin",
        "Monopolist"
    ],
    "Legacy for Assassin or Private General": [
        "Assassin",
        "Private General"
    ],
    "Legacy for Assassin or Usurper": [
        "Assassin",
        "Usurper"
    ],
    "Legacy for Assassin or Weaponsmith": [
        "Assassin",
        "Weaponsmith"
    ],
    "War Hero": [
        "Battle Mage",
        "General"
    ],
    "Dragon Slayer": [
        "Battle Mage",
        "Knight"
    ],
    "Legacy for Battle Mage or Magic Dealer": [
        "Battle Mage",
        "Magic Dealer"
    ],
    "Legacy for Battle Mage or Martial Artist": [
        "Battle Mage",
        "Martial Artist"
    ],
    "Legacy for Battle Mage or Mercenary": [
        "Battle Mage",
        "Mercenary"
    ],
    "Legacy for Battle Mage or Minister for Magic": [
        "Battle Mage",
        "Minister for Magic"
    ],
    "Legacy for Battle Mage or Private General": [
        "Battle Mage",
        "Private General"
    ],
    "Legacy for Battle Mage or Revolutionary": [
        "Battle Mage",
        "Revolutionary"
    ],
    "Legacy for Battle Mage or Trickster": [
        "Battle Mage",
        "Trickster"
    ],
    "Legacy for Battle Mage or Weaponsmith": [
        "Battle Mage",
        "Weaponsmith"
    ],
    "Legacy for Cleric or Dark Sorcerer": [
        "Cleric",
        "Dark Sorcerer"
    ],
    "Legacy for Cleric or High Chancellor": [
        "Cleric",
        "High Chancellor"
    ],
    "Legacy for Cleric or Knight": [
        "Cleric",
        "Knight"
    ],
    "Legacy for Cleric or Magic Dealer": [
        "Cleric",
        "Magic Dealer"
    ],
    "Legacy for Cleric or Martial Artist": [
        "Cleric",
        "Martial Artist"
    ],
    "Legacy for Cleric or Minister for Magic": [
        "Cleric",
        "Minister for Magic"
    ],
    "Legacy for Cleric or Private General": [
        "Cleric",
        "Private General"
    ],
    "Legacy for Cleric or Professor of Magic": [
        "Cleric",
        "Professor of Magic"
    ],
    "Legacy for Cleric or Prophet": [
        "Cleric",
        "Prophet"
    ],
    "Legacy for Cleric or Trickster": [
        "Cleric",
        "Trickster"
    ],
    "Legacy for Crime Boss or Dark Sorcerer": [
        "Crime Boss",
        "Dark Sorcerer"
    ],
    "Legacy for Crime Boss or General": [
        "Crime Boss",
        "General"
    ],
    "Legacy for Crime Boss or Knight": [
        "Crime Boss",
        "Knight"
    ],
    "Legacy for Crime Boss or Lobbyist": [
        "Crime Boss",
        "Lobbyist"
    ],
    "Legacy for Crime Boss or Minister for Magic": [
        "Crime Boss",
        "Minister for Magic"
    ],
    "Legacy for Crime Boss or Minister for the Arts": [
        "Crime Boss",
        "Minister for the Arts"
    ],
    "Legacy for Crime Boss or Monopolist": [
        "Crime Boss",
        "Monopolist"
    ],
    "Legacy for Crime Boss or Politician": [
        "Crime Boss",
        "Politician"
    ],
    "Legacy for Crime Boss or Prophet": [
        "Crime Boss",
        "Prophet"
    ],
    "Legacy for Crime Boss or Revolutionary": [
        "Crime Boss",
        "Revolutionary"
    ],
    "Legacy for Dark Sorcerer or Mad Scientist": [
        "Dark Sorcerer",
        "Mad Scientist"
    ],
    "Legacy for Dark Sorcerer or Magic Dealer": [
        "Dark Sorcerer",
        "Magic Dealer"
    ],
    "Legacy for Dark Sorcerer or Minister for Magic": [
        "Dark Sorcerer",
        "Minister for Magic"
    ],
    "Legacy for Dark Sorcerer or Monopolist": [
        "Dark Sorcerer",
        "Monopolist"
    ],
    "Legacy for Dark Sorcerer or Revolutionary": [
        "Dark Sorcerer",
        "Revolutionary"
    ],
    "Legacy for Dark Sorcerer or Thief": [
        "Dark Sorcerer",
        "Thief"
    ],
    "Legacy for Dark Sorcerer or Usurper": [
        "Dark Sorcerer",
        "Usurper"
    ],
    "Legacy for General or Lobbyist": [
        "General",
        "Lobbyist"
    ],
    "Legacy for General or Martial Artist": [
        "General",
        "Martial Artist"
    ],
    "Legacy for General or Minister for Magic": [
        "General",
        "Minister for Magic"
    ],
    "Legacy for General or Minister for the Arts": [
        "General",
        "Minister for the Arts"
    ],
    "Legacy for General or Politician": [
        "General",
        "Politician"
    ],
    "Legacy for General or Private General": [
        "General",
        "Private General"
    ],
    "Legacy for General or Prophet": [
        "General",
        "Prophet"
    ],
    "Legacy for General or Usurper": [
        "General",
        "Usurper"
    ],
    "Legacy for High Chancellor or Inventor": [
        "High Chancellor",
        "Inventor"
    ],
    "Legacy for High Chancellor or Lobbyist": [
        "High Chancellor",
        "Lobbyist"
    ],
    "Legacy for High Chancellor or Mercenary": [
        "High Chancellor",
        "Mercenary"
    ],
    "Legacy for High Chancellor or Minister for Magic": [
        "High Chancellor",
        "Minister for Magic"
    ],
    "Legacy for High Chancellor or Monopolist": [
        "High Chancellor",
        "Monopolist"
    ],
    "Legacy for High Chancellor or Patron": [
        "High Chancellor",
        "Patron"
    ],
    "Legacy for High Chancellor or Politician": [
        "High Chancellor",
        "Politician"
    ],
    "Legacy for High Chancellor or Private General": [
        "High Chancellor",
        "Private General"
    ],
    "Legacy for High Chancellor or Thief": [
        "High Chancellor",
        "Thief"
    ],
    "Legacy for High Chancellor or Trickster": [
        "High Chancellor",
        "Trickster"
    ],
    "Legacy for Inventor or Lobbyist": [
        "Inventor",
        "Lobbyist"
    ],
    "Legacy for Inventor or Mad Scientist": [
        "Inventor",
        "Mad Scientist"
    ],
    "Legacy for Inventor or Magic Dealer": [
        "Inventor",
        "Magic Dealer"
    ],
    "Legacy for Inventor or Mercenary": [
        "Inventor",
        "Mercenary"
    ],
    "Legacy for Inventor or Minister for the Arts": [
        "Inventor",
        "Minister for the Arts"
    ],
    "Legacy for Inventor or Monopolist": [
        "Inventor",
        "Monopolist"
    ],
    "Legacy for Inventor or Politician": [
        "Inventor",
        "Politician"
    ],
    "Legacy for Inventor or Private General": [
        "Inventor",
        "Private General"
    ],
    "Legacy for Inventor or Professor of Magic": [
        "Inventor",
        "Professor of Magic"
    ],
    "Legacy for Inventor or Thief": [
        "Inventor",
        "Thief"
    ],
    "Legacy for Inventor or Weaponsmith": [
        "Inventor",
        "Weaponsmith"
    ],
    "Legacy for Knight or Lobbyist": [
        "Knight",
        "Lobbyist"
    ],
    "Legacy for Knight or Martial Artist": [
        "Knight",
        "Martial Artist"
    ],
    "Legacy for Knight or Mercenary": [
        "Knight",
        "Mercenary"
    ],
    "Legacy for Knight or Private General": [
        "Knight",
        "Private General"
    ],
    "Legacy for Knight or Prophet": [
        "Knight",
        "Prophet"
    ],
    "Legacy for Knight or Revolutionary": [
        "Knight",
        "Revolutionary"
    ],
    "Legacy for Knight or Weaponsmith": [
        "Knight",
        "Weaponsmith"
    ],
    "Legacy for Lobbyist or Mercenary": [
        "Lobbyist",
        "Mercenary"
    ],
    "Legacy for Lobbyist or Minister for Magic": [
        "Lobbyist",
        "Minister for Magic"
    ],
    "Legacy for Lobbyist or Minister for the Arts": [
        "Lobbyist",
        "Minister for the Arts"
    ],
    "Legacy for Lobbyist or Prophet": [
        "Lobbyist",
        "Prophet"
    ],
    "Legacy for Lobbyist or Thief": [
        "Lobbyist",
        "Thief"
    ],
    "Legacy for Lobbyist or Usurper": [
        "Lobbyist",
        "Usurper"
    ],
    "Legacy for Mad Scientist or Martial Artist": [
        "Mad Scientist",
        "Martial Artist"
    ],
    "Legacy for Mad Scientist or Minister for the Arts": [
        "Mad Scientist",
        "Minister for the Arts"
    ],
    "Legacy for Mad Scientist or Monopolist": [
        "Mad Scientist",
        "Monopolist"
    ],
    "Legacy for Mad Scientist or Patron": [
        "Mad Scientist",
        "Patron"
    ],
    "Legacy for Mad Scientist or Professor of Magic": [
        "Mad Scientist",
        "Professor of Magic"
    ],
    "Legacy for Mad Scientist or Revolutionary": [
        "Mad Scientist",
        "Revolutionary"
    ],
    "Legacy for Mad Scientist or Usurper": [
        "Mad Scientist",
        "Usurper"
    ],
    "Legacy for Mad Scientist or Weaponsmith": [
        "Mad Scientist",
        "Weaponsmith"
    ],
    "Legacy for Magic Dealer or Mercenary": [
        "Magic Dealer",
        "Mercenary"
    ],
    "Legacy for Magic Dealer or Minister for Magic": [
        "Magic Dealer",
        "Minister for Magic"
    ],
    "Legacy for Magic Dealer or Politician": [
        "Magic Dealer",
        "Politician"
    ],
    "Legacy for Magic Dealer or Professor of Magic": [
        "Magic Dealer",
        "Professor of Magic"
    ],
    "Legacy for Magic Dealer or Prophet": [
        "Magic Dealer",
        "Prophet"
    ],
    "Legacy for Magic Dealer or Thief": [
        "Magic Dealer",
        "Thief"
    ],
    "Legacy for Magic Dealer or Trickster": [
        "Magic Dealer",
        "Trickster"
    ],
    "Legacy for Martial Artist or Mercenary": [
        "Martial Artist",
        "Mercenary"
    ],
    "Legacy for Martial Artist or Minister for the Arts": [
        "Martial Artist",
        "Minister for the Arts"
    ],
    "Legacy for Martial Artist or Patron": [
        "Martial Artist",
        "Patron"
    ],
    "Legacy for Martial Artist or Private General": [
        "Martial Artist",
        "Private General"
    ],
    "Legacy for Martial Artist or Professor of Magic": [
        "Martial Artist",
        "Professor of Magic"
    ],
    "Legacy for Martial Artist or Revolutionary": [
        "Martial Artist",
        "Revolutionary"
    ],
    "Legacy for Mercenary or Monopolist": [
        "Mercenary",
        "Monopolist"
    ],
    "Legacy for Mercenary or Patron": [
        "Mercenary",
        "Patron"
    ],
    "Legacy for Mercenary or Politician": [
        "Mercenary",
        "Politician"
    ],
    "Legacy for Mercenary or Thief": [
        "Mercenary",
        "Thief"
    ],
    "Legacy for Minister for Magic or Professor of Magic": [
        "Minister for Magic",
        "Professor of Magic"
    ],
    "Legacy for Minister for Magic or Trickster": [
        "Minister for Magic",
        "Trickster"
    ],
    "Legacy for Minister for the Arts or Patron": [
        "Minister for the Arts",
        "Patron"
    ],
    "Legacy for Minister for the Arts or Professor of Magic": [
        "Minister for the Arts",
        "Professor of Magic"
    ],
    "Legacy for Minister for the Arts or Prophet": [
        "Minister for the Arts",
        "Prophet"
    ],
    "Legacy for Minister for the Arts or Weaponsmith": [
        "Minister for the Arts",
        "Weaponsmith"
    ],
    "Legacy for Monopolist or Politician": [
        "Monopolist",
        "Politician"
    ],
    "Legacy for Monopolist or Revolutionary": [
        "Monopolist",
        "Revolutionary"
    ],
    "Legacy for Monopolist or Trickster": [
        "Monopolist",
        "Trickster"
    ],
    "Legacy for Monopolist or Usurper": [
        "Monopolist",
        "Usurper"
    ],
    "Legacy for Patron or Politician": [
        "Patron",
        "Politician"
    ],
    "Legacy for Patron or Professor of Magic": [
        "Patron",
        "Professor of Magic"
    ],
    "Legacy for Patron or Thief": [
        "Patron",
        "Thief"
    ],
    "Legacy for Patron or Weaponsmith": [
        "Patron",
        "Weaponsmith"
    ],
    "Legacy for Politician or Private General": [
        "Politician",
        "Private General"
    ],
    "Legacy for Politician or Prophet": [
        "Politician",
        "Prophet"
    ],
    "Legacy for Politician or Thief": [
        "Politician",
        "Thief"
    ],
    "Legacy for Private General or Revolutionary": [
        "Private General",
        "Revolutionary"
    ],
    "Legacy for Private General or Thief": [
        "Private General",
        "Thief"
    ],
    "Legacy for Private General or Weaponsmith": [
        "Private General",
        "Weaponsmith"
    ],
    "Legacy for Professor of Magic or Trickster": [
        "Professor of Magic",
        "Trickster"
    ],
    "Legacy for Professor of Magic or Weaponsmith": [
        "Professor of Magic",
        "Weaponsmith"
    ],
    "Legacy for Prophet or Trickster": [
        "Prophet",
        "Trickster"
    ],
    "Legacy for Prophet or Usurper": [
        "Prophet",
        "Usurper"
    ],
    "Legacy for Revolutionary or Thief": [
        "Revolutionary",
        "Thief"
    ],
    "Legacy for Revolutionary or Trickster": [
        "Revolutionary",
        "Trickster"
    ],
    "Coup Leader": [
        "Revolutionary",
        "Usurper"
    ],
    "Legacy for Thief or Usurper": [
        "Thief",
        "Usurper"
    ],
    "Legacy for Trickster or Usurper": [
        "Trickster",
        "Usurper"
    ]
}

with open('opportunities-generated.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for t1, c1 in zip(traits, classes):
        for t2, c2 in zip(traits, classes):
            if t1 == t2:
                continue
            writer.writerow([
                '{c1} or {c2} Opportunity'.format(c1=c1, c2=c2),
                'icons/orb-direction.svg',
                'An opportunity arises. Starting with the highest, each '
                'player with 10 or more {t1} may choose to place this card '
                'in front of them for +10 {t1}. The player that does is now '
                'known as a {c1}. If no player chooses to do this, then '
                'place front of all players for a +10 {t2} bonus to all '
                'players with 10 or more {t2}, who each gain the title of '
                '{c2}.'.format(**locals()),
            ])


with open('agenda-generated.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for c1 in classes:
        for t1 in traits:
            if traits.index(t1) == classes.index(c1):
                continue
            s1 = specialisms[c1][t1]
            writer.writerow([
                'Reveal {t1} Agenda'.format(t1=t1),
                'icons/cloak-dagger.svg',
                'You reveal a secret {t1} agenda. You may only play '
                'this if you are a {c1}. Turn face-up enough face-down'
                ' cards to reveal at least 10 {t1}. '
                'You are now known as a {s1} in addition to being a '
                '{c1}.'.format(
                    **locals()),
            ])


with open('legacy-generated.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for legacy, titles in legacies.items():
        writer.writerow([
            legacy,
            'icons/trophy-cup.svg',
            'You achieve a great legacy: {}. You win the game. '
            'You may only play this if you are a {}'.format(legacy, ' or a '
                                                                  ''.join(
                titles))
        ])

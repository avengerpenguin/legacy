require 'squib'

Squib::Deck.new(cards: 2, layout: 'layouts/layout-fortune.yml') do
  background color: 'white'
  data = csv file: 'data/fortunes.csv'

  text str: data['title'], layout: 'title'
  svg file: data['icon'],
      width: 500, height: 500,
      x: 150, y: 140

  rect x: 20, y: 640, width: 785, height: 465, radius: 8

  text str: data['temp_title'], layout: 'Oneshot'
  text str: data['temp_bonus'], layout: 'OneshotBonus'
  svg file: data['temp_type'], layout: 'OneshotBonusType'

  text str: data['perm_title'], layout: 'Fixture'
  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: 'fortune_'
  showcase file: 'showcase_fortune.png', fill_color: '#0000'
end

#Squib::Deck.new(cards: 3, layout: 'misfortune-layout.yml') do
#  text str: 'Hello, World!'
#  save format: :png
#end

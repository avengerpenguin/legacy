require 'squib'

Squib::Deck.new(layout: 'layout-fortune.yml') do
  background color: 'white'
  data = csv file: 'fortunes.csv'

  rect x: 20, y: 70, width: 785, height: 1035, radius: 8

  text str: data['title'], layout: 'title'
  text str: data['temp'], layout: 'oneshot'
  text str: data['perm'], layout: 'fixture'

  save format: :png
end

#Squib::Deck.new(cards: 3, layout: 'misfortune-layout.yml') do
#  text str: 'Hello, World!'
#  save format: :png
#end

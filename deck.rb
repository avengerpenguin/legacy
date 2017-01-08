require 'squib'

Squib::Deck.new(cards: 2, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/items.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Item', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['temp_title'], layout: 'Oneshot'
  text str: data['temp_bonus'], layout: 'OneshotBonus'
  svg file: data['temp_type'], layout: 'OneshotBonusType'

  #text str: data['perm_title'], layout: 'Fixture'
  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: '1-item-'
end

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/events.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Event', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['ignore_text'], layout: 'Oneshot'

  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: '1-event-'
end

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/buildings.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Building', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['ability_text'], layout: 'RuleText'

  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: '2-building-'
end

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/people.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Person', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['ability_text'], layout: 'RuleText'

  save_png prefix: '2-person-'
end

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/premium-items.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Premium Item', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['ability_text'], layout: 'RuleText'

  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: '2-premium-'
end

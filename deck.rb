require 'squib'

data_items = Squib.csv file: 'data/items.csv'
data_events = Squib.csv file: 'data/events.csv'

deck1_size = data_items.nrows + data_events.nrows

Squib::Deck.new(cards: data_items.nrows, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/items.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Item', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  bleed = inches(0.125)
  rect x: bleed, y: bleed,
       width: inches(2.5), height: inches(3.5), dash: '0.5mm 0.5mm'

  safe = inches(0.25)
  rect x: safe, y: safe,
       width: inches(2.25), height: inches(3.25), dash: '0.1mm 0.1mm'

  rect x: 100, y: 650, width: 625, height: 375, radius: 8

  text str: data['temp_title'], layout: 'Oneshot'
  text str: data['temp_bonus'], layout: 'OneshotBonus'
  svg file: data['temp_type'], layout: 'OneshotBonusType'

  #text str: data['perm_title'], layout: 'Fixture'
  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'

  save_png prefix: '1-item-', count_format: '%03d'
  save_sheet prefix: 'sheet-1-', rows: 4, columns: 4
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

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/challenges.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Challenge', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['ability_text'], layout: 'RuleText'

  save_png prefix: '2-challenge-'
end

Squib::Deck.new(cards: 1, layout: 'layouts/main.yml') do
  background color: 'white'
  data = csv file: 'data/experiences.csv'

  text str: data['title'], layout: 'Title'
  text str: 'Experience', layout: 'Type'
  svg file: data['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  text str: data['perm_bonus'], layout: 'FixtureBonus'
  svg file: data['perm_type'], layout: 'FixtureBonusType'
  text str: data['ability_text'], layout: 'RuleText'

  save_png prefix: '2-experience-'
end

data_opportunity = Squib.csv(file: 'data/opportunities.csv')
data_agenda = Squib.csv(file: 'data/agendas.csv')
data_legacy = Squib.csv(file: 'data/legacies.csv')

deck3_size = data_opportunity.nrows + data_agenda.nrows + data_legacy.nrows
Squib::Deck.new(cards: deck3_size, layout: 'layouts/main.yml') do
  background color: 'white'
  #data = csv file: 'data/opportunities.csv'

  types = Array.new(data_opportunity.nrows, 'Opportunity').concat(
  Array.new(data_agenda.nrows, 'Agenda').concat(
  Array.new(data_legacy.nrows, 'Legacy')))

  bleed = inches(0.125)
  rect x: bleed, y: bleed,
       width: inches(2.5), height: inches(3.5), dash: '0.5mm 0.5mm'

  safe = inches(0.25)
  rect x: safe, y: safe,
       width: inches(2.25), height: inches(3.25), dash: '0.1mm 0.1mm'

  rect x: 100, y: 650, width: 625, height: 375, radius: 8

   text str: data_opportunity['title'].concat(data_agenda['title'].concat(
      data_legacy['title'])), layout:
      'Title'
  text str: types, layout: 'Type'
  svg file: data_opportunity['icon'].concat(data_agenda['icon'].concat(
      data_legacy['icon'])), layout: 'Picture'


  icon_size = 30
  text(str: data_opportunity['ability_text']
                .concat(data_agenda['ability_text'].concat(
      data_legacy['ability_text'])), layout: 'RuleText') do |embed|
    embed.svg key: 'Strength', file: 'icons/crossed-swords.svg', width: icon_size, height: icon_size
    embed.svg key: 'Magic', file: 'icons/fairy-wand.svg', width: icon_size, height: icon_size
    embed.svg key: 'Wealth', file: 'icons/crown-coin.svg', width: icon_size, height: icon_size
    embed.svg key: 'Shadow', file: 'icons/cowled.svg', width: icon_size, height: icon_size
    embed.svg key: 'Knowledge', file: 'icons/white-book.svg', width: icon_size, height: icon_size
    embed.svg key: 'Influence', file: 'icons/public-speaker.svg', width: icon_size, height: icon_size
  end

  save_png prefix: types.map{|x| "3-#{x}-"}
  save_sheet prefix: 'sheet-3-', rows: 4, columns: 4
end

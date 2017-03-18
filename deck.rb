require 'squib'
require 'open-uri'


def get_from_google(sheet_gid)
  google_sheet_id = '1UbQaWcCSOdeHLwQfvljuDZiQwUvRZ1Wjuvg1YPRqyos'
  buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid}").read
  Squib.csv data: buffer
end

icon_size = 30

icon_replace = Proc.new  do |embed|
    embed.svg key: 'Strength', file: 'icons/crossed-swords.svg', width: icon_size, height: icon_size
    embed.svg key: 'Magic', file: 'icons/fairy-wand.svg', width: icon_size, height: icon_size
    embed.svg key: 'Wealth', file: 'icons/crown-coin.svg', width: icon_size, height: icon_size
    embed.svg key: 'Shadow', file: 'icons/cowled.svg', width: icon_size, height: icon_size
    embed.svg key: 'Knowledge', file: 'icons/white-book.svg', width: icon_size, height: icon_size
    embed.svg key: 'Influence', file: 'icons/public-speaker.svg', width: icon_size, height: icon_size
end


gids = %w(
  0
  1654442762
  172189516
  1507136951
  1137630752
  553378969
  1061704561
  1179381931
)

gids.each_index do |index|

  data = get_from_google gids[index]

  Squib::Deck.new(cards: data.nrows, layout: 'layouts/main.yml') do
    background color: 'white'

    bleed = inches(0.125)
    rect x: bleed, y: bleed,
         width: inches(2.5), height: inches(3.5), dash: '0.5mm 0.5mm'

    safe = inches(0.25)
    rect x: safe, y: safe,
       width: inches(2.25), height: inches(3.25), dash: '0.1mm 0.1mm'

    rect x: 100, y: 650, width: 625, height: 375, radius: 8

    data.columns.each do |column|
      if column == 'Icon'
        svg file: data[column].map{|x| "icons/#{x}.svg" if x}, layout: column
      else
        text str: data[column], layout: column, &icon_replace
      end
    end

    save_sheet prefix: "sheet-#{index}-", rows: 4, columns: 4

  end

end

=begin

data_growth = Squib.csv file: 'data/deck-2-growth.csv'
data = get_from_google 1654442762


Squib::Deck.new(cards: data_growth.nrows, layout: 'layouts/main.yml') do
  background color: 'white'

  text str: data_growth['title'], layout: 'Title'
  text str: data_growth['type'], layout: 'Type'
  svg file: data_growth['icon'], layout: 'Picture'

  rect x: 30, y: 650, width: 765, height: 450, radius: 8

  icon_size = 30
  text(str: data_growth['ability_text'], layout: 'RuleText') do |embed|
    embed.svg key: 'Strength', file: 'icons/crossed-swords.svg', width: icon_size, height: icon_size
    embed.svg key: 'Magic', file: 'icons/fairy-wand.svg', width: icon_size, height: icon_size
    embed.svg key: 'Wealth', file: 'icons/crown-coin.svg', width: icon_size, height: icon_size
    embed.svg key: 'Shadow', file: 'icons/cowled.svg', width: icon_size, height: icon_size
    embed.svg key: 'Knowledge', file: 'icons/white-book.svg', width: icon_size, height: icon_size
    embed.svg key: 'Influence', file: 'icons/public-speaker.svg', width: icon_size, height: icon_size
  end


  save_png prefix: '2-challenge-', count_format: '%03d'
  save_sheet prefix: 'sheet-2-', rows: 4, columns: 4
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

=end

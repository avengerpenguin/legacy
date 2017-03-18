group :legacy do
  guard 'rake', task: :default do
    watch %r{deck.rb} # a regular expression that matches our file
    watch %r{icons/.*}        # watch every file inside of our img directory
    watch %r{layouts/.*\.yml}       # Any yml file, anywhere (config or layout)
  end
end

require 'squib'

task default: [:deck, :page]

task :deck do
  load 'deck.rb'
end

task :page do
  html = %Q{
<!DOCTYPE html>
<html>
<body>
<h1> Legacy cards</h1>
<ul>
#{Dir["_output/*.png"].map { |s| "<li><a href=\"#{File.basename(s)}\">#{File.basename(s)}</a></li>"}.join "\n"}
</ul>
</body>
</html>
  }
  File.open('_output/index.html', 'w') { |file| file.write(html) }
end

CURRENT_SEMESTER = 'sp25'

def write_template(type, num)
  titles = {
    'lab' => 'Lab',
    'hw' => 'Homework',
    'disc' => 'Discussion'
  }
  padded_num = num.to_s.rjust(2, "0")
  puts "#{type} #{num} #{padded_num}"
  destination = type == 'disc' ? "disc#{padded_num}.pdf" : "#{type}#{padded_num}/"
  template = <<~YAML
  ---
  title: #{titles[type]} #{num}
  redirect_to: https://c88c.org/#{CURRENT_SEMESTER}/#{type}/#{destination}
  permalink: /#{type}/#{type}#{padded_num}/
  ---
  YAML
  File.open("pages/#{name}.html", 'w') { |file| file.write(template) }
end

def write_proj(name)
  # puts "#{type} #{num} #{padded_num}"
  template = <<~YAML
  ---
  title: #{name.capitalize} Project
  redirect_to: https://c88c.org/#{CURRENT_SEMESTER}/proj/#{name}/
  permalink: /proj/#{name}/
  ---
  YAML
  File.open("pages/#{type}#{padded_num}.html", 'w') { |file| file.write(template) }
end


assignments = ['lab', 'hw', 'disc']
assignments.each do |type|
  (1..12).each { |num| write_template(type, num) }
end

def write_template(type, num)
  titles = {
    'lab' => 'Lab',
    'hw' => 'Homework',
    'disc' => 'Discussion'
  }
  padded_num = num.to_s.rjust(2, "0")
  puts "#{type} #{num} #{padded_num}"
  redirect_file = type == 'disc' ? "disc#{padded_num}.pdf" : ""
  template = <<~YAML
  ---
  title: #{titles[type]} #{num}
  redirect_to: https://c88c.org/sp24/#{type}/#{type}#{padded_num}/#{redirect_file}
  permalink: /#{type}/#{type}#{padded_num}/
  ---
  YAML
  File.open("pages/#{type}#{padded_num}.html", 'w') { |file| file.write(template) }
end

assignments = ['lab', 'hw', 'disc']
assignments.each do |type|
  (1..12).each { |num| write_template(type, num) }
end

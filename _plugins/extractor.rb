# _plugins/extractor.rb

Jekyll::Hooks.register :site, :after_reset do |site|
  puts "Running extraction scripts..."
  
  # Run the python extraction scripts
  system("python3 _scripts/extract_links.py .")
  system("python3 _scripts/extract_lastmod.py .")
  system("python3 _scripts/extract_images.py .")
  
  puts "Extraction scripts completed."
end

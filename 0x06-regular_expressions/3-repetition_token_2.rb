#!/usr/bin/env ruby
# This script uses a RegEx to match strings from `hbtn` to `hbttttttn`

puts ARGV[0].scan(/hbt{1,}n/).join

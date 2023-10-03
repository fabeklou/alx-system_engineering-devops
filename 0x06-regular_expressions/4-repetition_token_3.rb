#!/usr/bin/env ruby
# This script uses a RegEx to match `hbn` and strings from `hbtn` to `hbttttttn`

puts ARGV[0].scan(/hbt*n/).join

#!/usr/bin/env ruby
# This script uses a RegEx to match any string starting with `h` and ends with `n`

puts ARGV[0].scan(/h.n/).join

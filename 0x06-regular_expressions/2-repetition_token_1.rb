#!/usr/bin/env ruby
# This script uses RegEx that match `htn` and `hbtn`

puts ARGV[0].scan(/hb?tn/).join

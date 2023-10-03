#!/usr/bin/env ruby
# This script uses a RegEx to match a 10 digit phone number

puts ARGV[0].scan(/^\d{10}/).join

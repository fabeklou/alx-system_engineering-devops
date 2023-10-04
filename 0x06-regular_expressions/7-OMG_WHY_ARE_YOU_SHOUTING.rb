#!/usr/bin/env ruby
# This script uses a RegEx to match only capital letters

puts ARGV[0].scan(/[A-Z]/).join

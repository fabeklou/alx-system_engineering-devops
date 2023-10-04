#!/usr/bin/env ruby
# This script uses a RegEx groups Capturing to display the [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/).join(',')

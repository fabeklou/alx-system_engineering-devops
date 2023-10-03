#!/usr/bin/env ruby
# This script uses RegEx that match hbt{2,5}n

puts ARGV[0].scan(/hbt{2,5}n/).join

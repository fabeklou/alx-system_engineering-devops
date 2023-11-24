# This manifest creates a <school> file in the </tmp> directory with the string 'I love puppet' as content

file { '/tmp/school':
  content => 'I love puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}

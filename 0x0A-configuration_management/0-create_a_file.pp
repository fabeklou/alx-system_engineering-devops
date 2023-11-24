# This manifest creates a <school> file in the </tmp> directory
file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love puppet',
}

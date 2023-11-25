# This manifest creates a <school> file in the </tmp> directory

file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => 'u=rwx,g=r,o=r',
    content => 'I love puppet',
}

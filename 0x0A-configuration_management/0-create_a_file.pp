# This manifest creates a <school> file

file { '/tmp/school':
    group   => 'www-data',
    owner   => 'www-data',
    mode    => 'u=rwx,g=r,o=r',
    content => 'I love Puppet'
}

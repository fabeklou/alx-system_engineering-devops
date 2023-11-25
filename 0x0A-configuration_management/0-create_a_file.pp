# This manifest creates a <school> file in the </tmp>
#     directory with the string 'I love puppet' as
#     content

$file_path = '/tmp/school'

file { $file_path:
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => 'u=rwx,g=r,o=r'
}

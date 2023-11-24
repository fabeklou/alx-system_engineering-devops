# This manifest creates a <school> file in the </tmp>
#     directory with the string 'I love puppet' as
#     content

$file_path = '/tmp/school'

file { $file_path:
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love puppet',
}

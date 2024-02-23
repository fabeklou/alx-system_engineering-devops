# This manifest creates a < school > file in the < /tmp >
# directory with the string 'I love puppet' as content

$file_path = '/tmp/school'
$file_content = 'I love Puppet'

node default {

    file { 'creating the file school in /tmp':
        path    => $file_path,
        mode    => '0744',
        owner   => 'www-data',
        group   => 'www-data',
        content => $file_content
    }
}

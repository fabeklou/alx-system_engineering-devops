# This manifest make changes to the system-wide
#      configuration file (/etc/ssh/ssh_config)

include stdlib

$passwd_auth = '    PasswordAuthentication no'
$id_file = '    IdentityFile ~/.ssh/school'

file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/home/akagami/Akagami/ALX-PROJECTS/alx-system_engineering-devops/0x0B-ssh/config',
    content => $passwd_auth
}

file_line { 'Declare identity file':
    ensure  => present,
    path    => '/home/akagami/Akagami/ALX-PROJECTS/alx-system_engineering-devops/0x0B-ssh/config',
    content => $id_file
}

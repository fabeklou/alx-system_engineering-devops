# This manifest make changes to the system-wide
#      configuration file (/etc/ssh/ssh_config)

$content = "# Managed by Puppet -V 5.5
    PasswordAuthentication no
    IdentityFile ~/.ssh/school"

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => $content
}

# This manifest set up a client SSH configuration file
#   so that you can connect to a server without typing
#   a password by making changes to the system-wide
#   configuration file (/etc/ssh/ssh_config)

$path = '/etc/ssh/ssh_config'
$content = "# Managed by Puppet -V 5.5
    PasswordAuthentication no
    IdentityFile ~/.ssh/school"

node default {

    file { $path:
        ensure  => present,
        content => $content
    }
}

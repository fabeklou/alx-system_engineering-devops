# This manifest install and configure an Nginx server

$config_file = '/etc/nginx/sites-available/default'
$redirect_me = "    # Managed by Puppet -V 5.5
    location /redirect_me {
        return 301 https://github.com/fabeklou;
    }
"

node default {

    exec { 'Update : Advanced Packaging Tool':
        command => '/bin/apt update -y'
    }

    package { 'Installing Nginx -V 1.18.0':
        ensure   => installed,
        name     => 'nginx',
        provider => 'apt'
    }

    exec { 'Allowing nginx to accept http requests on port 80':
        command => '/sbin/ufw allow \'Nginx HTTP\'',
    }

    file { '/var/www/html/index.html':
        ensure  => present,
        content => 'Hello World!'
    }

    file_line { 'Add redirection context to the default config file':
        ensure => present,
        path   => $config_file,
        line   => $redirect_me,
        after  => 'server_name _;'
    }

    exec { 'restarting the nginx server':
        command => '/sbin/service nginx restart'
    }
}

# This manifest configure an Nginx server to have a
# costum http header response

$config_file = '/etc/nginx/sites-available/default'
$redirect_me = "    # Managed by Puppet -V 5.5
    location /redirect_me {
        return 301 https://github.com/fabeklou;
    }
"
$custom_header = "
    http {
        add_header X-Served-By \"${hostname}\";
"

exec { 'Update : Advanced Packaging Tool':
    command     => '/bin/apt update -y'
}

package { 'Installing Nginx -V 1.18.0':
    ensure   => installed,
    name     => 'nginx',
    provider => 'apt'
}

exec { 'Allowing nginx to accept http requests on port 80':
    command     => '/sbin/ufw allow \'Nginx HTTP\'',
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

file_line { 'creating a custom HTTP header response':
    ensure => present,
    path   => $config_file,
    match  => 'http {',
    line   => $custom_header
}

exec { 'restarting the nginx server':
    command     => '/sbin/service nginx restart'
}

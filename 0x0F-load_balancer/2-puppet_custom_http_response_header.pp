# This manifest configure an Nginx server to have a
# costum http header response

$config_file = '/etc/nginx/sites-available/default'

$custom_header = "
    add_header X-Served-By \"${hostname}\";
"

exec { 'Update : Advanced Packaging Tool':
    command     => '/bin/apt update -y'
}

-> package { 'Ensure Nginx -V 1.18.0 is installed':
    ensure => present,
    name   => 'nginx',
}

-> file_line { 'creating a custom HTTP header response':
    ensure => present,
    path   => $config_file,
    after  => 'index index.html index.htm index.nginx-debian.html;',
    line   => $custom_header
}

-> exec { 'restarting the nginx server':
    command    => '/sbin/service nginx restart'
}

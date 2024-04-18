# This manifest increases the the capacity of the Nginx server

exec { 'capacity increase':
  command => 'sed -i "s/15/2048/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'nginx server restarted':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

# This manifest Changes the OS configuration so that
# it is possible to login with the holberton user
# and open a file without any error message

exec { 'hard files limite increased':
  command => 'sed -i "/holberton hard/s/5/2048/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft files limite increased':
  command => 'sed -i "/holberton soft/s/4/2048/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
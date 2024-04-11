# This manifest fix 500Error returned by Apache web server

exec { 'fix typo in WP config file':
    path    => ['/usr/sbin', '/sbin', '/usr/bin', '/bin'],
    command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}

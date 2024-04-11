# This manifest fix 500Error returned by Apache web server

exec { 'fix typo in WP config file':
    command => "/usr/sbin/sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}

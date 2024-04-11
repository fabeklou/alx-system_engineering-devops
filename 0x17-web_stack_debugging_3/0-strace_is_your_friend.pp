# This manifest fix 500Error returned by Apache web server

$file_path = '/var/www/html/wp-settings.php'

file { 'fix typo in WP config file':
    ensure  => file,
    path    => $file_path,
    content => inline_template("<%= @file_content.gsub('phpp', 'php') %>"),
}

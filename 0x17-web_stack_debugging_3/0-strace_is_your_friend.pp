# This manifest fix 500Error returned by Apache web server

$file_path = '/var/www/html/wp-settings.php'
$line = "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"
$wrong = 'phpp'
$correct = 'php'

file_line { 'fix typo in WP config file':
    path    => $file_path,
    line    => $line,
    match   => $wrong,
    replace => $correct
}

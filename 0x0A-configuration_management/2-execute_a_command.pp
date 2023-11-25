# This manifest kills a process named <killmenow>

exec { 'kill_task':
    command => '/bin/pkill killmenow'
}

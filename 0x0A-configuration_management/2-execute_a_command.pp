# This manifest kills a process named killmenow

node default {
    exec { 'Killing the process < killmenow >':
        command => '/bin/pkill killmenow'
    }
}

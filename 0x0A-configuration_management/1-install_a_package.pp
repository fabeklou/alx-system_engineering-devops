# This manifest installs < flask > version 2.1.0
# and werkzeug version 2.1.1 from < pip3 >

node default {

    exec { 'Installing flask==2.1.0':
        command => '/bin/pip3 install flask==2.1.0'
    }

    exec { 'Installing werkzeug==2.1.1':
        command => '/bin/pip3 install werkzeug==2.1.1'
    }
}

# This manifest installs a version <2.1.0> of the
#     the python framework <flask> using <pip3>

exec {'flask':
    command => '/bin/pip3 install flask==2.1.0'
}

exec {'werkzeug':
    command => '/bin/pip3 install werkzeug==2.1.1'
}

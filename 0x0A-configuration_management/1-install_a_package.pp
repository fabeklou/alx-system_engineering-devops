# This manifest installs version <2.1.0> of <flask> using <pip3>

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    name     => 'flask'
}

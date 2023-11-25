# This manifest installs a version <2.1.0> of the
#     the python framework <flask> using <pip3>

$pckg = 'flask'

package { $pckg:
    ensure   => '2.1.0',
    provider => 'pip3'
}

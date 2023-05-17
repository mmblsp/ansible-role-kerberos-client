import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_installed_packages(host):
    package_list_altlinux = ['libkrb5', 'krb5-kinit', 'krb5-kadmin']
    package_list_astralinux = ['krb5-kdc', 'krb5-admin-server', 'krb5-user']
    package_list_centos = ['krb5-libs', 'krb5-workstation']
    if host.system_info.distribution == 'alt':
        for pkg in package_list_altlinux:
            assert host.package(pkg).is_installed
    elif host.system_info.distribution == 'astralinuxce':
        for pkg in package_list_astralinux:
            assert host.package(pkg).is_installed
    elif host.system_info.distribution == 'centos':
        for pkg in package_list_centos:
            assert host.package(pkg).is_installed

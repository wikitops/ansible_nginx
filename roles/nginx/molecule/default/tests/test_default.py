import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sources_directories(host):
    d = host.file("/etc/nginx")
    assert d.exists
    assert d.is_directory
    assert d.user == 'root'
    assert d.group == 'root'


def test_sites_available_directories(host):
    if host.system_info.distribution != 'centos':
        d = host.file("/etc/nginx/sites-available")

        assert d.exists
        assert d.is_directory
        assert d.user == 'root'
        assert d.group == 'root'


def test_sites_enabled_directories(host):
    if host.system_info.distribution == 'centos':
        d = host.file("/etc/nginx/conf.d")
    else:
        d = host.file("/etc/nginx/sites-enabled")

    assert d.is_directory
    assert d.user == 'root'
    assert d.group == 'root'


def test_service(host):
    s = host.service('nginx')
    assert s.is_enabled
    assert s.is_running

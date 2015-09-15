__author__ = 'luke.beer'
import ConfigParser
import logging
import os

import host

log_file = os.path.dirname(__file__) + 'budweiser.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG)


def create_hosts_from_conf(config_file='hosts.conf'):
    Config = ConfigParser.ConfigParser()
    Config.read(config_file)
    hosts = []
    for section in Config.sections():
        options = Config.options(section)
        x = host.Host(**options)
        hosts.append(x)
    return hosts

__author__ = 'luke.beer'
import logging
import subprocess


class Host:
    def __init__(self, hostname=None, address=None, username=None, source=None, destination=None, match=None):
        self.hostname = hostname
        self.address = address
        self.username = username
        self.source = source
        self.destination = destination
        self.match = match

    def validate(self):
        for param in vars(self):
            if not self.__dict__[param]:
                logging.error("'Host.%s' is not valid" % param)
                return False
        try:
            conn = "%s@%s" % (self.username, self.address)
            cmd = "ls -d %s" % self.source
            result = subprocess.check_output(['/usr/bin/ssh', conn, cmd], stderr=subprocess.STDOUT)
            if result.rstrip() != self.source:
                logging.error(result)
            return True
        except Exception as e:
            logging.error(e)
            return False

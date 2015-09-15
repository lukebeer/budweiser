__author__ = 'luke.beer'
import subprocess
import threading
import logging
import socket
import time

import questions
import states


class Executor(threading.Thread):
    def __init__(self, r, channel):
        threading.Thread.__init__(self)
        self.redis = r
        self.channel = channel
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe([channel])
        self.state = states.State.INIT
        self.name = socket.gethostname()
        self.hosts = []

    def communicate(self, msg='Sup?'):
        msg = '%s :: %s :: %s' % (socket.gethostname(), self.state, msg)
        logging.info(msg)
        self.redis.publish(self.channel, msg)

    def set_state(self, state):
        state_msg = 'State changed from %s to %s' % (self.state, state)
        logging.info(state_msg)
        self.communicate(state_msg)

    def archive(self):
        self.set_state(states.State.ARCHIVE)
        time.sleep(5)

    def compress(self):
        self.set_state(states.State.COMPRESS)
        time.sleep(5)

    def file_sync(self, host):
        self.set_state(states.State.COLLECT)
        self.communicate("%s: Valid config." % host.hostname)
        try:
            destination = "%s/%s" % (host.destination, host.hostname)
            src = "%s@%s:%s/" % (host.username, host.address, host.source)
            result = subprocess.check_output(['/usr/bin/rsync', '-pvvctrz', '--include=\"%s\"' % host.match, src,
                                              destination], stderr=subprocess.STDOUT)
            self.communicate(result)
        except Exception as e:
            self.communicate(e.message)

    def stop(self):
        self.pubsub.unsubscribe()
        self.communicate('Goodbye....')

    def ready(self, item):
        hostname, state, msg = item['data'].split(' :: ', 3)
        if hostname == self.name:
            return
        if msg == questions.Questions.WHAT:
            self.communicate("Hey friend, I'm %s" % self.state)
        else:
            if state == states.State.IDLE:
                return True
            if state in [states.State.COLLECT, states.State.ARCHIVE, states.State.COMPRESS]:
                return False

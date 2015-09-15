__author__ = 'luke.beer'
import time
import redis

import config
import questions
import states
import budweiser


def run(hosts):
    client = budweiser.Executor(redis.Redis(), 'budweiser')
    client.start()
    while True:
        client.communicate(questions.Questions.WHAT)
        for item in client.pubsub.listen():
            if client.ready(item):
                client.archive()
                client.compress()
                for host in client.hosts:
                    client.file_sync(host)
            else:
                time.sleep(10)
                client.communicate(questions.Questions.WHAT)
                continue
        client.set_state(states.State.IDLE)
        time.sleep(60)


if __name__ == "__main__":
    hosts = config.create_hosts_from_conf()
    try:
        run(hosts)
    except:
        raise

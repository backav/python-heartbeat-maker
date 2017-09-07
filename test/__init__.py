#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis import StrictRedis
from HeartbeatMaker import HeartbeatMaker
import arrow
import atexit


def test(it, par=None):
    print('%s:%s:心跳:%s' % (arrow.now(), it, par))


maker = HeartbeatMaker('redis://localhost:6379/0', 'test-beat', test, {"name": "bac"})

maker.clean()
# maker.beat_it('bac', 5)
maker.beat_it('jack', 5, 'test')

atexit.register(maker.stop)

maker.start()

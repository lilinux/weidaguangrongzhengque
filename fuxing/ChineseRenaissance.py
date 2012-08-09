#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import time
import sys

try:
    from praise import head, tail, interupt, error
except Exception:
    head = tail = interupt = error = ''

begin = datetime.datetime(1949, 10, 1)
end = datetime.datetime(2049, 10, 1)
total_seconds = (end - begin).total_seconds()

def rate(now=None):
    if not now:
        now = datetime.datetime.today()
    return (now - begin).total_seconds() / total_seconds

def progress():
    while True:
        current = rate()
        if current >= 1:
            yield 1
            break
        yield current

def bar(length=40, dotted=4, step=2, blank=' ', dot='#'):
    if not hasattr(bar, 'pos'):
        bar.pos = 0
    else:
        bar.pos = (bar.pos + step) % length
    return '[%s%s%s]' % (blank*bar.pos, dot*dotted, blank*(length-bar.pos-step))

def show(interval=0.3, with_bar=bar):
    print head
    for r in progress():
        sys.stdout.write('%s %.10f%%\r'%(bar(), r*100))
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write('%s %.10f%%\r'%(bar(blank='#'), r*100))
    print '\n', tail

if __name__ == '__main__':
    try:
        show()
    except KeyboardInterrupt, e:
        print '\n', interupt
    except Exception, e:
        print '\n', error

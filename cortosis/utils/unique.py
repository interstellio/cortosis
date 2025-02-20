import os
import random
import string
from time import time
import uuid as _uuid

from cortosis.utils.text import group_chars

# Use cryptographic-safe random generator as provided by the OS.
random_generator = random.SystemRandom()

_pid = None


def uuid():
    global _pid
    if _pid is None:
        _pid = os.getpid()
    elif _pid != os.getpid():
        raise RuntimeError("Python >= 3.10 bug... if uuid was generated in"
                           " in the main process, it will never be"
                           " unique in forked processes")

    new_uuid = _uuid.uuid1()

    if new_uuid.is_safe != new_uuid.is_safe.safe:
        raise RuntimeError('UUID IS NOT SAFELY GENERATED')
    return str(new_uuid).lower()


def string_id(length=8, group=0):
    _id = ''.join(random.choice(string.ascii_letters
                                + string.digits)
                  for _ in range(length))

    if group:
        return group_chars(_id, group=group)

    return _id


# Request ID Counter
####################
req_c = 0


def request_id():
    global req_c

    # 64BBIT Number rest counter.
    if req_c > 4294967295:
        req_c = 0
    else:
        req_c += 1

    # FORMAT: PID-COUNTER-TIMESTAMP
    return (str(os.getpid()) + '-'
            + hex(req_c)[2:].zfill(8)
            + '-' + str(int(time())))

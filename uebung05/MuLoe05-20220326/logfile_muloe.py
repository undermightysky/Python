# -*- coding: utf-8 -*-

from datetime import datetime
import time


def log_to_file(msg, fname, encoding='utf-8'):
    with open(fname, mode='a', encoding=encoding) as f:
        f.write(f'{datetime.utcnow().isoformat()}'
                f' - {" ".join(msg.split())}\n')


if __name__ == '__main__':
    file = 'log.txt'

    log_to_file('Start.', file)
    time.sleep(0.5)

    log_to_file('Processing ...', file)
    time.sleep(1)

    log_to_file('Read data.\n   Process data.   \n  Save    data.', file)
    time.sleep(0.3)

    log_to_file('   Done.\n', file)

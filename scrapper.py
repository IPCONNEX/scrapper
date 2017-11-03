#! /Users/omarelmohri/.venvs/lpthw/bin/python

import logging
from tools import ConnectionManager
import signal
import time
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.ERROR)
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)


logging.debug('[*] Initialising the program variables')

cm = ConnectionManager.ConnectionManager()
time.sleep(3)

cm.new_identity()
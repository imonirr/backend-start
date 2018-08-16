#!/usr/bin/env python

import subprocess
import argparse
from os.path import dirname, abspath
from os import chdir

chdir(dirname(dirname(abspath(__file__))))


parser = argparse.ArgumentParser()
parser.add_argument("-isProduction", help="Run in Production Config", default="development")
args = parser.parse_args()

#  if args.isProduction == 'production':
#      print("Production Config")
#      stopProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.production.yml down'
#  else:
print("Development Config")
stopProxyContainers = 'docker-compose -f docker-compose.yml -f docker-compose.override.yml down'


#  subprocess.check_output(['bash', '-c', stopProxyContainers])
subprocess.call(stopProxyContainers.split())

print('backend Down')


import argparse
import subprocess


DBPATH="/Users/tmorales/data/mongoDB"

# Start mongod as a deamon  
subprocess.Popen(["mongod","--storageEngine", "wiredTiger", "--dbpath","{0}".format(DBPATH)])

# shutdown mongodb deamon
subprocess.Popen(["mongod","--shutdown"])

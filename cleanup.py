#find /db/logs/archive_data/* -type f -mtime +5 | xargs rm
from sys import argv
import os, time

script, directory, age = argv
print "Searching directory %s for file older than %s day(s)" % (str(argv[1]), str(argv[2]))

#convert age to sec. 1 day = 24*60*60
age = int(age)*86400

for f in os.listdir(directory):
   now = time.time()
   filepath = os.path.join(directory, f)
   modified = os.stat(filepath).st_mtime
   if modified < now - age:
       if os.path.isfile(filepath):
           os.remove(filepath)
           print 'Deleted: %s (%s)' % (f, modified)


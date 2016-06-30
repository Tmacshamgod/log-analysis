import mail
import subprocess
from shlex import split

def analysis():
    servers = [
		{"server":"10.103.0.1", "path":"/data/platform/collector/apache-flume-1.6.0-bin/logs"},
		{"server":"10.103.0.2", "path":"/data/platform/collector/apache-flume-1.6.0-bin/logs"}, 
	    ]
    for s in servers:
        server = s['server']
        path = s['path']
        subprocess.call(split('./bin.sh ' + server + ' ' + path)) 
    mail.sendmail()

if __name__ == '__main__':
    analysis()

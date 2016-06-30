import tornado.web
from os import listdir, getcwd
from os.path import isfile, join

def getFiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        filenames = getFiles(getcwd() + "/statics/files")
        files = []
        files.extend(
            {"path": self.static_url("files/" + f), "name": f} for f in filenames
        )
        self.render('index.html', files=files)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.download import DownloadHandler
from handlers.hello import HelloHandler

url = [
    (r'/download', DownloadHandler),
    (r'/', HelloHandler),
]

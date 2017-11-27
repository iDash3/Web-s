import sys
import bs4 as bs
import requests
# QT4. Dang.
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.WebKit import *

class Client(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def on_page_load(self):
		self.app.quit()
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()

# sauce = requests.get(URL)
soup = bs.BeautifulSoup(sauce)
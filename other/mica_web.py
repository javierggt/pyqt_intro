#!/usr/bin/env python

# pip install PyQtWebEngine
# https://doc.qt.io/archives/qt-5.6/qtwebengine-webenginewidgets-simplebrowser-example.html

import sys
import os
import netrc
import PyQt5.QtCore as QtC, PyQt5.QtWidgets as QtW, PyQt5.QtNetwork as QtN
import PyQt5.QtWebEngineWidgets as QtWe
import sip  # needs to come _after_ PyQt5 imports


class WebPage(QtWe.QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.authenticationRequired.connect(self.handleAuthenticationRequired)

    def handleAuthenticationRequired(self, requestUrl, auth):
        netrc_file = os.path.expanduser('~/.netrc')
        try:
            info = netrc.netrc(netrc_file)
            (login, account, password) = info.hosts['occweb']
            auth.setPassword(password)
            auth.setUser(login)
        except:
            sip.assign(auth, QtN.QAuthenticator())

    # trick from https://stackoverflow.com/questions/54920726/how-make-any-link-blank-open-in-same-window-using-qwebengine
    def createWindow(self, _type):
        page = WebPage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtC.pyqtSlot(QtC.QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()

app = QtW.QApplication(sys.argv)

web = QtWe.QWebEngineView()
web.resize(1400, 1000)
page = WebPage()
web.setPage(page)
url = sys.argv[1] if len(sys.argv) > 1 else "https://icxc.cfa.harvard.edu/aspect/mica_reports/47/47574"
web.load(QtC.QUrl(url))

web.show()

sys.exit(app.exec_())

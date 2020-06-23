import sys
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG

class Event(QtC.QEvent):
    def __init__(self, text):
        super().__init__(QtC.QEvent.User)
        self.text = text

class Window(QtW.QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QtW.QLabel('Hello World!')
        
        layout = QtW.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
    
    def event(self, event):
        if event.type() == QtC.QEvent.User:
            self.label.setText(event.text)
            return True
        return super().event(event)

    
class Window2(QtW.QWidget):
    
    def __init__(self):
        super().__init__()
        self._text = QtW.QLineEdit()
        layout = QtW.QVBoxLayout()
        layout.addWidget(self._text)
        self.setLayout(layout)
        
        self._text.textChanged.connect(self._set_text)
    
    def _set_text(self):
        event = Event(self._text.text())
        app.postEvent(window_1, event)

app = QtW.QApplication([])
window_1 = Window()
window_2 = Window2()
window_1.show()
window_2.show()
app.exec()


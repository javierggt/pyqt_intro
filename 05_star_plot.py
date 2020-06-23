import numpy as np
import sys
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG

from Quaternion import Quat
from Chandra.Time import DateTime

from utils import get_stars


def symsize(mag):
    # map mags to figsizes, defining
    # mag 6 as 40 and mag 11 as 3
    # interp should leave it at the bounding value outside
    # the range
    return np.interp(mag, [6.0, 11.0], [40.0, 3.0])


class StarView(QtW.QGraphicsView):
    def __init__(self, scene=None):
        super().__init__(scene)

        self._start = None
        self._moving = False
        b1hw = 512.
        self.fov = self.scene().addRect(-b1hw, -b1hw, 2 * b1hw, 2 * b1hw)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self._start is None:
            return

        if pos != self._start:
            self._moving = True

        if self._moving:
            end_pos = self.mapToScene(pos)
            start_pos = self.mapToScene(self._start)
            dx, dy = end_pos.x() - start_pos.x(), end_pos.y() - start_pos.y()

            scene_rect = self.scene().sceneRect()
            new_scene_rect = QtC.QRectF(scene_rect.x() - dx, scene_rect.y() - dy,
                                        scene_rect.width(), scene_rect.height())
            self.scene().setSceneRect(new_scene_rect)
            self._start = pos

            # the following should have worked:
            # self.translate(dx, dy)

    def mouseReleaseEvent(self, event):
        self._start = None

    def mousePressEvent(self, event):
        self._moving = False
        self._start = event.pos()

    def wheelEvent(self, event):
        scale = 1 + 0.5 * event.angleDelta().y() / 360
        self.scale(scale, scale)

    def drawForeground(self, painter, rect):
        black_pen = QtG.QPen()
        black_pen.setWidth(2)
        b1hw = 512.
        # dx = self.transform().dx()
        # dy = self.transform().dy()
        # print(dx, dy) # this is zero because I set the scene rectangle instead of transforming
        center = QtC.QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        center = self.mapToScene(center)
        painter.drawRect(center.x() - b1hw, center.y() - b1hw, 2 * b1hw, 2 * b1hw)
        b2w = 520
        painter.drawRect(center.x() - b2w, center.y() - b1hw, 2 * b2w, 2 * b1hw)
        painter.setPen(QtG.QPen(QtG.QColor('magenta')))
        painter.drawLine(center.x() - 511, center.y(), center.x() + 511, center.y())
        painter.drawLine(center.x(), center.y() - 511, center.x(), center.y() + 511)


class StarPlot(QtW.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtW.QVBoxLayout(self)
        self.setLayout(layout)

        self.scene = QtW.QGraphicsScene(self)
        self.scene.setSceneRect(-100, -100, 200, 200)
        self.view = StarView(self.scene)
        self.layout().addWidget(self.view)

        self.view.scale(0.5, 0.5)
        quaternion = Quat(q=[-0.474674, -0.473931, 0.262471, 0.693674])
        starcat_time = DateTime('2020:001:19:18:21.914')
        self.show_stars(starcat_time, quaternion)

    def show_stars(self, starcat_time, quaternion):
        self.scene.clear()
        self.stars = get_stars(starcat_time, quaternion)
        black_pen = QtG.QPen()
        black_pen.setWidth(2)
        black_brush = QtG.QBrush(QtG.QColor("black"))
        red_pen = QtG.QPen(QtG.QColor("red"))
        red_brush = QtG.QBrush(QtG.QColor("red"))
        for star in self.stars:
            s = symsize(star['MAG'])
            rect = QtC.QRectF(star['row'] - s/2, -star['col'] - s/2, s, s)
            # this hardcoded list would come from the commanded star catalog. Cheating...
            if star['AGASC_ID'] in [237774392, 237776560, 237899472, 237899816, 237900784,
                                    238420640, 238421128, 238300048, 237897848]:
                self.scene.addEllipse(rect, red_pen, red_brush)
            else:
                self.scene.addEllipse(rect, black_pen, black_brush)


def main():
    app = QtW.QApplication(sys.argv)
    w = StarPlot()
    w.resize(800, 600)
    w.show()
    app.exec()


main()

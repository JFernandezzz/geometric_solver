
from PyQt5.QtCore import Qt

from gui.drawings.event_handlers.drawing_event_handler import EventHandler


class PointDrawer(EventHandler):
    def __init__(self, drawing):
        self.drawing = drawing
        self.started = True

    def handle_mouse_moved(self, event):
        pass

    def handle_mouse_pressed(self, event):
        if event.button() == Qt.RightButton:
            return
        if event.button() == Qt.LeftButton:
            self.drawing.start = self.drawing.mapToScene(event.pos())

    def handle_mouse_released(self, event):
        if event.button() == Qt.LeftButton:
            if not self.started:
                self.started = True
            else:
                self.started = True
                self.drawing.end = self.drawing.mapToScene(event.pos())
                self.drawing.launch_add_point(self.drawing.start)
                self.drawing.start = None
                self.drawing.end = None

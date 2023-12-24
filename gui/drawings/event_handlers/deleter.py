from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QGraphicsLineItem

from gui.drawings.event_handlers.drawing_event_handler import EventHandler


class Deleter(EventHandler):
    def __init__(self, drawing):
        EventHandler.__init__(self)
        self.drawing = drawing

    def handle_mouse_moved(self, event):
        pass

    def handle_mouse_pressed(self, event):
        pos = self.drawing.mapToScene(event.pos())
        print('pos', pos)
        item = self.drawing.scene().itemAt(pos, QTransform())
        print('item', item)
        if not isinstance(item, QGraphicsLineItem) or 'id' not in item.__dict__:
            print('item id', item.id)
            self.drawing.launch_delete_point(item.id)
            print('In deleter')
            return
        self.drawing.launch_delete_line(item.id)

    def handle_mouse_released(self, event):
        pass

    def handle_paint_event(self, event, painter):
        pass

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,0,1)
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y -  d / 2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        with self.canvas:
            Color(0,0,1)
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y -  d / 2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
#        touch.ud['line'].points += [touch.x,touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        with parent.canvas:
            Rectangle(source='court.png', pos=(0,100), size=(1024,568))
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear', pos=(475,0))
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()

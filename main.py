import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line, Rectangle

Window.clearcolor = (1, 1, 1, 1)
class paint_app(Widget):
    def build(self):
        self.buttons = buttons()
        self.add_widget(self.buttons)
        self.buttons.build()

class buttons(Widget):
    def build(self):
        self.window = main()
        self.add_widget(self.window)

        clear_btn = Button(text="clear", pos=(0,0), size=(200, 90), font_size=32)
        clear_btn.bind(on_press=self.clear_window)
        self.add_widget(clear_btn)

        orange_btn = Button(background_normal="", background_color= (0.1, 0.4, 1, 1), size=(45, 45), pos=(200, 0))
        orange_btn.bind(on_press=lambda x: self.change_color(color=(0.1, 0.4, 1, 1)))
        self.add_widget(orange_btn)

        blue_btn = Button(background_normal="", background_color= ( 1, 0.6, 0.4, 1), size=(45, 45), pos=(200 + 45, 0))
        blue_btn.bind(on_press=lambda x: self.change_color(color=( 1, 0.6, 0.4, 1)))
        self.add_widget(blue_btn)

        green_btn = Button(background_normal="", background_color= ( 0.6, 1, 0.4, 1), size=(45, 45), pos=(200 + 90, 0))
        green_btn.bind(on_press=lambda x: self.change_color(color=( 0.6, 1, 0.4, 1)))
        self.add_widget(green_btn)

        red_btn = Button(background_normal="", background_color= ( 0, 0, 1, 1), size=(45, 45), pos=(200 + 135, 0))
        red_btn.bind(on_press=lambda x: self.change_color(color=( 0, 0, 1, 1)))
        self.add_widget(red_btn)

        red_btn = Button(background_normal="", background_color= ( 0.09, 0.17, 0.3, 1), size=(45, 45), pos=(200 + 180, 0))
        red_btn.bind(on_press=lambda x: self.change_color(color=( 0.09, 0.17, 0.3, 1)))
        self.add_widget(red_btn)

        yellow_btn = Button(background_normal="", background_color= ( 0, 1, 1, 1), size=(45, 45), pos=(200,45))
        yellow_btn.bind(on_press=lambda x: self.change_color(color=( 0, 1, 1, 1)))
        self.add_widget(yellow_btn)

        black_btn = Button(background_normal="", background_color= ( 0, 0, 0, 1), size=(45, 45), pos=(200 + 45, 45))
        black_btn.bind(on_press=lambda x: self.change_color(color=( 0, 0, 0, 1)))
        self.add_widget(black_btn)

        pink_btn = Button(background_normal="", background_color= ( 1, 0, 1, 1), size=(45, 45), pos=(200 + 90, 45))
        pink_btn.bind(on_press=lambda x: self.change_color(color=( 1, 0, 1, 1)))
        self.add_widget(pink_btn)

        darkblue_btn = Button(background_normal="", background_color= ( 1, 0, 0, 1), size=(45, 45), pos=(200 + 135, 45))
        darkblue_btn.bind(on_press=lambda x: self.change_color(color=( 1, 0, 0, 1)))
        self.add_widget(darkblue_btn)

        darkgreen_btn = Button(background_normal="", background_color= ( 0.19, 1, 0.19, 1), size=(45, 45), pos=(200 + 180, 45))
        darkgreen_btn.bind(on_press=lambda x: self.change_color(color=( 0.19, 1, 0.19, 1)))
        self.add_widget(darkgreen_btn)

        darkgreen_btn = Button(background_normal="", background_color= ( 0.19, 1, 0.19, 1), size=(45, 45), pos=(200 + 180, 45))
        darkgreen_btn.bind(on_press=lambda x: self.change_color(color=( 0.19, 1, 0.19, 1)))
        self.add_widget(darkgreen_btn)

        plus_btn = Button(text="+", size=(150, 45), font_size=32, pos=(200 + 225, 45))
        plus_btn.bind(on_press=self.plus)
        self.add_widget(plus_btn)

        minus_btn = Button(text="-", size=(150, 45), font_size=32, pos=(200 + 225, 0))
        minus_btn.bind(on_press=self.minus)
        self.add_widget(minus_btn)

        eraser_btn = Button(text="Eraser", size=(200, 90), font_size=32, pos=(200 + 375, 0), background_normal="" , background_color=(0.8, 0.8, 0.8, 1), color=(0, 0, 0, 1))
        eraser_btn.bind(on_press=self.eraser)
        self.add_widget(eraser_btn)

        circle_btn = Button(text="Circle", size=(280, 45), font_size=24, pos=(200 + 575, 0))
        circle_btn.bind(on_release=lambda x : self.shape(x="circle"))
        self.add_widget(circle_btn)

        square_btn = Button(text="Square", size=(280, 45), font_size=24, pos=(200 + 575, 45))
        square_btn.bind(on_release=lambda x : self.shape(x="square"))
        self.add_widget(square_btn)

        pen_btn = Button(text="Pen", size=(280, 90), font_size=24, pos=(480 + 575, 0))
        pen_btn.bind(on_release=lambda x : self.shape(x="line"))
        self.add_widget(pen_btn)

    def clear_window(self, obj):
        self.window.canvas.clear()
        
    def change_color(self, color):
        main.color = (color)

    def plus(self, obj):
        main.line_thickness += 2

    def minus(self, obj):
        main.line_thickness -= 2

    def eraser(self, obj):
        main.shape_type = "line"
        main.color = (1, 1, 1, 1)

    def shape(self, x):
        main.shape_type = x
        print(main.shape_type)
    
class main(Widget):
    shape_type = ""
    color = (0, 0, 0, 1)
    line_thickness = 1
    def on_touch_down(self, touch):
        self.canvas.add(Color (rgba=self.color))
        if touch.y > 100:
            if self.shape_type == "line":
                if self.color == (1, 1, 1, 1):
                    self.color = (0, 0, 0, 1)
                touch.ud["line"] = Line(point=(touch.x, touch.y), width=self.line_thickness)
                self.canvas.add(touch.ud["line"])

            if self.shape_type == "circle":
                self.canvas.add(Ellipse(pos=(touch.x - self.line_thickness * 25/2 , touch.y- self.line_thickness * 25/2), size=(self.line_thickness * 25, self.line_thickness * 25)))

            if self.shape_type == "square":
                self.canvas.add(Rectangle(pos=(touch.x - self.line_thickness * 25/2 , touch.y- self.line_thickness * 25/2), size=(self.line_thickness * 25, self.line_thickness * 25)))
    
    def on_touch_move(self, touch):
        if touch.y > 100: 
            if self.shape_type == "line":
                touch.ud["line"].points += touch.x, touch.y

class Paint_app(App):
    def build(self):
        app = paint_app()
        app.build()
        return app
Paint_app().run()

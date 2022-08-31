from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config

class Frontend(App):
    def __init__(self):
        super().__init__()
        self.lb = Label(text = 'Please update data', font_size = 25,size_hint =(0.75, 1))

    def build(self):
        
        Window.size = (1000, 200)
        Window.clearcolor = (255/255, 186/255, 3/255)
        Window.title = "Logic_Sorting"
        
        box = BoxLayout()
        btn1 = Button(text='Update Data', font_size = 25,)
        btn3 = Button(text='Main tabs', font_size = 25,)
        
        
        box.add_widget(btn1)        
        box.add_widget(btn3)
        box.add_widget(self.lb)
        return box


if __name__ == "__main__":
    Frontend().run()
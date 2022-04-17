from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
#from kivy.uix.image import Image , AsyncImage
#from kivy.uix.checkbox import CheckBox
#from kivy.base import runTouchApp
#from kivy.lang import Builder

Window.clearcolor = (200/255, 135/255, 230/255, 0.8)
Window.size = (318,600)
class CreateApp(App):
    def build(self):
        self.title = "First [App] 0.01"
        


if __name__=='__main__':
    CreateApp().run()
from kivy.config import Config

Config.window_icon="images/logo.png"


from kivy.app import App

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button

from kivy.uix.label import Label

from kivy.uix.textinput import TextInput

from kivy.clock import Clock

from kivy.uix.widget import Widget

from kivy.builder import Builder

Builder.load_file("main.kv")



class app(App):

    def build(self):

        return Button(text="Hello world")


if __name__=="__main__":

    app().run()

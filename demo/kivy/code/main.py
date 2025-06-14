import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

kivy.resources.resource_add_path(".")
font1 = kivy.resources.resource_find("SourceHanSerifCN-Medium.otf")

class MyApp(App):
    def build(self):
        Window.fullscreen = 1
        self.title="中文标题"#不能设置font_name
        label1 = Label(text="你好", font_name=font1)
        button1 = Button(text="Kivy示例程序", font_name=font1)
        return button1

if __name__ == '__main__':
    MyApp().run()

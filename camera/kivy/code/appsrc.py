import kivy
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock
import cv2
import numpy as np

kivy.resources.resource_add_path(".")
font = kivy.resources.resource_find("SourceHanSerifCN-Medium.otf")

class MainWidget(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Window.size = (400, 700)  # 设置窗口大小为 800x600
        # 使用canvas设置背景颜色
        rgba_color = get_color_from_hex("#ADD9E6")
        with self.layout.canvas.before:
            Color(*rgba_color)  # 设置为红色，格式为 RGBA
            self.rect = Rectangle(size=Window.size, pos=self.layout.pos)

        self.title="相机操作"
        self.titlelabel = Label(
            text=self.title,
            height=10,
            font_name=font
        )
        self.camera_obj = Camera(
            play=True,
            # resolution=(640, 480),
            size_hint=(1, 5),
        )
        self.camera_obj.bind(on_capture=self.on_capture)
        # 创建 Image 部件用于显示 OpenCV 图像
        self.imageshow = Image(
            size_hint=(1, 5),
        )

        self.button = Button(text="拍照", size_hint=(1, 1), font_name=font)
        self.button.bind(on_press=self.take_picture)
        self.layout.add_widget(self.titlelabel)
        self.layout.add_widget(self.camera_obj)
        self.layout.add_widget(self.imageshow)
        self.layout.add_widget(self.button)

        return self.layout

    def take_picture(self, instance):
        image = self.camera_obj.texture
        cvimg = self.imageToOpenCv(image)
        #> 对图片进行操作
        showimg = self.opencvToImage(cvimg)
        self.imageshow.texture = showimg


    def imageToOpenCv(self, image):
        # 转换为 OpenCV 格式的图片
        image_data = np.frombuffer(image.pixels, dtype=np.uint8)
        image_data = image_data.reshape((image.height, image.width, 4))  # RGBA 格式
        image_data = cv2.cvtColor(image_data, cv2.COLOR_RGBA2BGR)  # 转换为 RGB 格式
        return image_data

    def opencvToImage(self, cvimg):
        # 转换图像格式
        # 将 BGR 转换为 RGB
        cv_image = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        # 翻转图像（可选，取决于你的需求）
        cv_image = cv2.flip(cv_image, 0)
        buf = cv_image.tobytes()
        # 更新纹理
        texture = Texture.create(size=(cvimg.shape[1], cvimg.shape[0]), colorfmt='rgb')
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        return texture

    def show_popup(self, title, text):
        popup_layout = BoxLayout(orientation='vertical')
        popup_label = Label(text=text)
        popup_layout.add_widget(popup_label)

        popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(400, 200))
        popup.open()

    def on_capture(self, instance):
        print("拍照完成")

if __name__ == '__main__':
    MainWidget().run()
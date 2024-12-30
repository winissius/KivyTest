from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        layout = FloatLayout()  # Cria um layout para organizar
        label = Label(text="It's me, Mario!",
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .5, 'center_y': .85})
        img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
                         size_hint=(1, .5),
                         pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(img)  # add label to layout
        layout.add_widget(label)  # add label to layout
        return layout  

if __name__ == '__main__':
    app = MainApp()
    app.run()
from kivy.app import App
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.loader import Loader
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

Builder.load_file('hb.kv')
fs = """$HEADER
    uniform float t;
    uniform sampler2D tex_in;
    uniform sampler2D tex_out;

    void main(void) {
        vec4 cin = texture2D(tex_in, tex_coord0);
        vec4 cout = texture2D(tex_out, tex_coord0);
        gl_FragColor = mix(cout, cin, t);
    }
"""
class Anasayfa(Screen):
    pass

class icindekiler(Screen):
    pass

class birincisayfa(Screen):
    pass

class ikincisayfa(Screen):
    pass

class ucuncusayfa(Screen):
    pass

class dorduncusayfa(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Anasayfa(name='anasayfa'))
sm.add_widget(icindekiler(name='icindekiler'))
sm.add_widget(birincisayfa(name='birincisayfa'))
sm.add_widget(ikincisayfa(name='ikincisayfa'))
sm.add_widget(ucuncusayfa(name='ucuncusayfa'))
sm.add_widget(dorduncusayfa(name='dorduncusayfa'))
class TestApp(App):

    def build(self):
        return sm #On envoie le screen manager pour affichage

if __name__ == '__main__':
    TestApp().run()

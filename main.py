from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.2, 1)

class AbdullahWorld(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Title
        self.add_widget(Label(text='[b]ABDULLAH WORLD[/b]', markup=True, font_size=35, color=(1, 0.8, 0, 1), size_hint=(1, 0.3)))
        self.add_widget(Label(text='Player: Shalayan Gujjar', font_size=18, size_hint=(1, 0.1)))

        # Status
        self.status = Label(text='Welcome to Your World!', font_size=20, size_hint=(1, 0.2))
        self.add_widget(self.status)

        # Buttons
        btn1 = Button(text='🚗 Drive Car', font_size=20, size_hint=(1, 0.2), background_color=(0, 0.8, 0, 1))
        btn1.bind(on_press=self.drive)
        self.add_widget(btn1)

        btn2 = Button(text='🏠 Go Home', font_size=20, size_hint=(1, 0.2), background_color=(0, 0.5, 1, 1))
        btn2.bind(on_press=self.home)
        self.add_widget(btn2)

        btn3 = Button(text='🔫 Start Mission', font_size=20, size_hint=(1, 0.2), background_color=(0.9, 0.1, 0.1, 1))
        btn3.bind(on_press=self.mission)
        self.add_widget(btn3)

    def drive(self, instance):
        self.status.text = '🚗 Driving... Shalayan on the road!'

    def home(self, instance):
        self.status.text = '🏠 Welcome Home, Boss!'

    def mission(self, instance):
        self.status.text = '🔫 Mission Started! Go Go Go!'

class AbdullahWorldApp(App):
    def build(self):
        return AbdullahWorld()

AbdullahWorldApp().run()

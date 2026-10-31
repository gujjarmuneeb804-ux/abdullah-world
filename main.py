from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.1, 0.15, 1)

class UltimateWorld(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 5
        self.spacing = 5
        
        self.money = 5000
        
        self.add_widget(Label(text='[b]ABDULLAH WORLD ULTIMATE[/b]', markup=True, font_size=24, color=(1,0.8,0,1), size_hint=(1,0.1)))
        self.money_label = Label(text=f'Player: Shalayan Gujjar | Money: ${self.money}', font_size=13, size_hint=(1,0.05))
        self.add_widget(self.money_label)
        
        self.status = Label(text='Welcome to Your World! Start a Job!', font_size=16, color=(0,1,0,1), size_hint=(1,0.08))
        self.add_widget(self.status)

        scroll = ScrollView(size_hint=(1, 0.77))
        grid = GridLayout(cols=2, spacing=6, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        items = {
            '🧱 BLOCKS\nAll Types': '100+ Blocks Unlocked: Wood, Stone, Diamond!',
            '🛋️ FURNITURE\nHouse': 'Furniture Placed: TV, Fridge, Sofa!',
            '🐄 ANIMALS\nFarm': 'Animals Added to Farm!',
            '🍔 FOOD\nEat': 'Food Eaten! Health +100',
            '🚗 VEHICLE\nGarage': 'Vehicles Unlocked: Supra, Truck!',
            '👹 MOBS\nFight': 'Mobs Attacking! Defend!',
            '👑 BOSS\nDragon': 'FINAL BOSS SPAWNED! BE CAREFUL!',
            '🔫 GUNS\nArmory': 'Guns Equipped: AK, M4, Sniper!',
            '💼 JOBS\nWork': 'Job Started! +$1000 Earned!',
            '💰 MONEY\nBank': 'Money Doubled! Bank Balance Check!',
            '🌍 COUNTRIES\nTravel': 'Travel: Pakistan, Dubai, USA, UK!',
            '⚙️ MACHINES\nCraft': 'Machines: Cutter, Drill, Mixer Running!',
            '🏭 FACTORIES\nBusiness': 'Factory Started! Producing Products! +$5000/day!'
        }
        
        for name, msg in items.items():
            btn = Button(text=name, font_size=14, size_hint_y=None, height=80, background_color=(0.2,0.4,0.8,1))
            if 'MONEY' in name or 'JOBS' in name or 'FACTORIES' in name:
                btn.bind(on_press=lambda x, m=msg: self.add_money(m))
            else:
                btn.bind(on_press=lambda x, m=msg: self.show_msg(m))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        self.add_widget(scroll)
        
    def show_msg(self, msg):
        self.status.text = msg
        
    def add_money(self, msg):
        self.money += 1000
        self.money_label.text = f'Player: Shalayan Gujjar | Money: ${self.money}'
        self.status.text = msg

class UltimateApp(App):
    def build(self):
        return UltimateWorld()

UltimateApp().run()

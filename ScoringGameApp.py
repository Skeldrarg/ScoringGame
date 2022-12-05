import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from androidtoast import toast

kivy.require('2.1.0') # replace with your current kivy version !

class TeamLayout(BoxLayout):

    points = 0
    teamName = ""
    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def add_points(self, point):
        self.set_points(self.get_points()+point)
        self.ids.points_label.text = str(self.get_points())

    def set_team_name(self):
        if self.ids.teamnameinput.text != "":
            self.teamName = self.ids.teamnameinput.text
            self.remove_widget(self.ids.teamname)
            self.add_widget(Label(text=self.teamName, font_size="30sp"), index=2)
        else:
            toast("Nom de l'équipe vide")

class IntroScreen(Screen):
    pass

class ScoringScreen(Screen):
    pass

class ScoringGameScreenManager(ScreenManager):
    pass

class ScoringGameApp(App):

    def build(self):
        return Builder.load_file("main.kv")

def main():
    ScoringGameApp().run()

if __name__ == '__main__':
    main()

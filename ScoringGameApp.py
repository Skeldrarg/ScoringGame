import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivymd.toast import toast

kivy.require('2.1.0') # replace with your current kivy version !

class TeamLayout(MDBoxLayout):

    points = 0
    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def add_points(self, point):
        self.set_points(self.get_points()+point)
        self.ids.points_label.text = str(self.get_points())

    def set_team_name(self):
        if self.ids.teamnameinput.text != "":
            teamName = self.ids.teamnameinput.text
            self.remove_widget(self.ids.teamname)
            self.add_widget(MDLabel(text=teamName, font_style="H4", halign="center"), index=2)
        else:
            toast("Nom de l'équipe vide")

class IntroScreen(Screen):
    pass

class ScoringScreen(Screen):
    pass

class ScoringGameScreenManager(MDScreenManager):
    pass

class ScoringGameApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")

def main():
    ScoringGameApp().run()

if __name__ == '__main__':
    main()

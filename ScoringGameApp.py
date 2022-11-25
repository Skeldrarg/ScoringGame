import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Team():

    def __init__(self, name):
        self.__name = name
        self.__points = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

class CreateTeamScreen(Screen):
    pass

    def create_team(self, name):
        team = Team(name)
        print(team.get_name())

class ScoringScreen(Screen):
    pass

class ScoringGameScreenManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class ScoringGameApp(App):

    def build(self):
        return kv


if __name__ == '__main__':
    ScoringGameApp().run()
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from openpyxl import Workbook
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from Parsingfile import main
from Sorting import sort_main_file
import os.path
import os
from openpyxl import Workbook
import openpyxl
import datetime
Config.set('graphics', 'resizable', True)
class MyApp(App):
    def __init__(self):
        super().__init__()
        self.lb = Label(text = 'Please update data', font_size = 25,size_hint =(0.75, 1))
    def build(self):
        Window.size = (1000, 200)
        Window.clearcolor = (255/255, 186/255, 3/255)
        Window.title = "test"
        box = BoxLayout()
        btn1 = Button(text='Update Data', font_size = 25, on_press = self.btnf1)
        btn3 = Button(text='Main tabs', font_size = 25, on_press = self.btnf3)
        box.add_widget(btn1)        
        box.add_widget(btn3)
        box.add_widget(self.lb)
        return box
    def  btnf1(self, inctance):
        now = datetime.datetime.now()
        main()
        sort_main_file()        
        self.lb.text = "Last update: \n"+str(now.strftime("%d-%m-%Y %H:%M"))    
    def  btnf3(self, inctance):
        os.system('C:\\logic_sorting\\thirdparty\\main.xlsx')
if __name__ == "__main__":
    MyApp().run()

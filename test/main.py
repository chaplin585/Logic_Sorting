from __future__ import print_function
import os.path
from tkinter import font
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
    
    
    def a():
        return 0
    
        
        




if __name__ == "__main__":
    MyApp().run()
from __future__ import print_function
import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from openpyxl import Workbook
import openpyxl




def main():
    
    wb = Workbook()
    ws = wb.active

    ABC = 'ABCDEFGHIJKL'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SAMPLE_SPREADSHEET_ID = '1iNNHjFAfu3prpC47Jyv81R39wNUV7GJ9aQAv_A_hNF0'
    SAMPLE_RANGE_NAME = 'Answers!A1:L10000000'
    
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
           
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\logic_sorting\src\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        i = 0
        j = 0
        while i < len(values):
            while j < len(values[i]):
                ws[ABC[j]+str(i+1)] = values[i][j] 
                wb.save("C:/logic_sorting/thirdparty/Google Data.xlsx")

                j+=1
            j = 0
            i+=1
        wb.close()

        
    except HttpError as err:
        print(err)
    return 0

if __name__ == '__main__':
    main()
    
    
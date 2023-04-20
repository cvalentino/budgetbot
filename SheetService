from urllib.error import HTTPError
from googleapiclient.discovery import build


class SheetService:

    def __init__(self, creds, spreadsheet_id):
        self.creds = creds
        self.sid = spreadsheet_id
        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()
        self.getCategories()

    def getValues(self, rng, print_values=False):
        try:
            result = self.sheet.values().get(spreadsheetId=self.sid, range=rng).execute()
            values = result.get('values', [])
            if not values:
                print('No data found.')
                return
            if print_values:
                print(values)
            return values
        except HTTPError as err:
            print(err)

    def appendLineItem(self, month, lineitem):
        rng = f'{month}!A1:R'
        value_input_option = 'USER_ENTERED'
        values = lineitem.toSheetObject()
        request = self.service.spreadsheets().values().append(spreadsheetId=self.sid,
                                                              range=rng, valueInputOption=value_input_option, body={'values': values})
        response = request.execute()

    def getCategories(self):
        self.categories = self.getValues('Overview!H1:W1')[0]

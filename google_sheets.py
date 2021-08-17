import requests
from secrets import GOOGLE_API_KEY, SPREADSHEET_ENDPOINT, SPREADSHEET_ID
from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_RANGE = "A1:E"


class GoogleSheets:

    def __init__(self):
        self.endpoint_get = SPREADSHEET_ENDPOINT + SPREADSHEET_RANGE
        self.endpoint_put = SPREADSHEET_ENDPOINT
        self.max_row = 0

    def get_current_rows(self):
        parameters = {
            "key": GOOGLE_API_KEY
        }
        response = requests.get(
            url=self.endpoint_get,
            params=parameters,
        )
        response.raise_for_status()
        print(len(response.json()["values"]))
        self.max_row = len(response.json()["values"])

    def write_new_stats(self, entries):
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        service_account_file = 'keys.json'

        # Create credentials for REST call
        creds = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=scopes
        )

        # Build the service object
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()

        # records to write
        records = {
            "values": entries
        }

        # start writing from A + (self.max_row + 1)
        write_range = f"workouts!A{int(self.max_row) + 1}"

        # Create the request object
        request = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=write_range,
            valueInputOption="USER_ENTERED",
            body=records
        )
        response = request.execute()

        if int(response.get("updatedRows")) > 0:
            return True
        return False

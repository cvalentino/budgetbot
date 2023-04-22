from flask import Flask
from flask_app.services.messagevalidator import MessageValidator
from flask_app.services.messageprocessor import MessageProcessor
from google.oauth2 import service_account
import os
from dotenv import load_dotenv
from flask_app.services.sheetservice import SheetService
from flask_app.services.resources.constants import SCOPES

load_dotenv()
KEY_PATH = os.getenv('key_path')
SPREADSHEET_ID = os.getenv('spreadsheet_id')

creds = service_account.Credentials.from_service_account_file(
    KEY_PATH, scopes=SCOPES)
sheet_service = SheetService(creds, SPREADSHEET_ID)
message_validator = MessageValidator(sheet_service)
message_processor = MessageProcessor(sheet_service, message_validator)

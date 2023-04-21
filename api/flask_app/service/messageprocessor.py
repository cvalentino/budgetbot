from flask_app.service.messagevalidator import MessageValidator
from flask_app.model.lineitem import LineItem


class MessageProcessor:

    def __init__(self, sheet_service):
        self.message_validator = MessageValidator(sheet_service)
        self.sheet_service = sheet_service

    def line_item_from_json(self, json_dict):
        json_dict = self.message_validator.validate_line_item_json(json_dict)
        line_item = LineItem(self.sheet_service.categories)
        for k, v in json_dict.items():
            if k in line_item.dict.keys():
                line_item.dict[k] = v
        return line_item

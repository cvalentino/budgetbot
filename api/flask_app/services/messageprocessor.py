from flask_app.models.lineitem import LineItem
from flask_app.services.resources.messages import *
from datetime import datetime


class MessageProcessor:

    def __init__(self, sheet_service, message_validator):
        self.sheet_service = sheet_service
        self.message_validator = message_validator

    def line_item_from_json(self, json_dict: dict):
        json_dict = self.message_validator.validate_line_item_json(json_dict)
        line_item = LineItem(self.sheet_service.categories)
        line_item.dict[json_dict["category"]] = json_dict["cost"]
        for k, v in json_dict.items():
            if k in line_item.dict.keys():
                line_item.dict[k] = v
        return line_item

    def parse_add_message_into_json(self, message: str):
        split_message = message.split(" ")
        floatable_indecies = self.message_validator.get_floatable_indecies_of(
            split_message)
        cost_index = max(floatable_indecies)
        description = " ".join(split_message[1:cost_index])
        cost = float(split_message[cost_index])
        category = " ".join(split_message[cost_index+1:]).lower()
        now = datetime.now()
        message_dict = {}
        message_dict["month"] = now.strftime("%b").upper()
        message_dict["day"] = now.day
        message_dict["description"] = description
        message_dict["category"] = category
        message_dict["cost"] = cost
        return message_dict

    def post_line_item(self, request_json: dict):
        line_item = self.line_item_from_json(request_json)
        sheet_response = self.sheet_service.appendLineItem(line_item)
        return sheet_response['updates']['updatedRange']
    
    def process_add_message(self, content: str, response_dict: dict):
        content = self.message_validator.validate_add_message(content)
        content_json = self.parse_add_message_into_json(content)
        updated_range = self.post_line_item(content_json)
        response_dict['message'] = ADD_RESPONSE
        response_dict['validation'] = {}
        response_dict['validation']['updated_range'] = updated_range
        response_dict['validation']['line_item'] = content_json

    def consume_message(self, request_json: dict):
        content = self.message_validator.get_message_content(request_json)
        response_dict = {}
        if content.lower().startswith('help'):
            response_dict['message'] = HELP_RESPONSE
        elif content.lower().startswith('add'):
            self.process_add_message(content, response_dict)
        else:
            response_dict['message'] = UNKNOWN_COMMAND
        return response_dict

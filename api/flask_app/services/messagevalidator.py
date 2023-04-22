from flask_app.services.resources.constants import LINE_ITEM_KEYS
import calendar


class MessageValidator:

    def __init__(self, sheet_service):
        self.sheet_service = sheet_service
        self.valid_months = [calendar.month_abbr[i].upper()
                             for i in range(1, 13)]

    def validate_line_item_json(self, json_dict):
        # Filter json_dict fields
        json_dict = {k: v for k, v in json_dict.items() if k in LINE_ITEM_KEYS}
        # Validate required fields are present
        if not all(k in json_dict for k in LINE_ITEM_KEYS):
            raise ValueError(
                "JSON provided is missing one or more required keys")
        # Validate category provided
        elif json_dict["category"] not in [c.lower() for c in self.sheet_service.categories]:
            raise ValueError(
                "Invalid category provided: {}".format(json_dict["category"]))
        # Validate month provided
        elif json_dict["month"] not in self.valid_months:
            raise ValueError(
                "Invalid month provided: {}".format(json_dict["month"]))
        # Validate day provided
        elif type(json_dict["day"]) is not int:
            raise ValueError(
                "Invalid day type provided: {}".format(type(json_dict["day"])))
        elif json_dict["day"] < 1 or json_dict["day"] > 31:
            raise ValueError(
                "Invalid day provided: {}".format(json_dict["day"]))
        # Validate cost provided
        elif type(json_dict["cost"]) not in [float, int]:
            raise ValueError(
                "Invalid cost type provided: {}".format(type(json_dict["cost"])))
        return json_dict

    def validate_add_message(self, content):
        if type(content) is not str:
            raise ValueError(
                "Invalid message type provided: {}".format(type(content)))
        # validate message is in this format: add <Description> <Cost> <Category>
        split_content = content.split(" ")
        # clean up extra whitespace
        split_content = [s.strip() for s in split_content if s.strip()]
        # starts with add
        if split_content[0].lower() != "add":
            raise ValueError(
                "An add message must begin with 'add' not '{}'".format(split_content[0]))
        # has at least 3 other entries (Desc, Cost, Category)
        if len(split_content) < 4:
            raise ValueError(
                "Message provided is missing some information")
        return " ".join(split_content)
    
    def get_message_content(self, request_json):
        if "message" not in request_json.keys():
            raise ValueError(
                "Request JSON missing 'message' key")
        return request_json['message']
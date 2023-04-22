from flask_app.model.lineitem import LineItem


class MessageProcessor:

    def __init__(self, sheet_service, message_validator):
        self.sheet_service = sheet_service
        self.message_validator = message_validator

    def line_item_from_json(self, json_dict):
        json_dict = self.message_validator.validate_line_item_json(json_dict)
        line_item = LineItem(self.sheet_service.categories)
        line_item.dict[json_dict["category"]] = json_dict["cost"]
        for k, v in json_dict.items():
            if k in line_item.dict.keys():
                line_item.dict[k] = v
        return line_item

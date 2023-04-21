from constants import LINE_ITEM_KEYS

class MessageValidator:

    def __init__(self, sheet_service):
        self.sheet_service = sheet_service

    def validate_line_item_json(self, json_dict):
        # Filter json_dict fields
        json_dict = {k: v for k, v in json_dict.items() if k in LINE_ITEM_KEYS}
        # Validate required fields are present
        if not all(k in json_dict for k in LINE_ITEM_KEYS):
            raise ValueError("JSON provided is missing one or more required keys")
        return json_dict


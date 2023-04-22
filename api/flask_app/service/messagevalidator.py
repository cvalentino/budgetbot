from flask_app.constants import LINE_ITEM_KEYS
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
        # Validate day
        elif json_dict["day"] < 1 or json_dict["day"] > 31:
            raise ValueError(
                "Invalid day provided: {}".format(json_dict["day"]))
        return json_dict

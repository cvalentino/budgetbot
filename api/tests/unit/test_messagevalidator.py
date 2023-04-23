from resources.payloads import *
from flask_app import message_validator


def test_valid_add_message():
    content = message_validator.get_message_content(VALID_ADD_MESSAGE)
    result = message_validator.validate_add_message(content)
    assert result == content
    
def test_valid_add_message_extra_spaces():
    content = message_validator.get_message_content(VALID_ADD_MESSAGE_EXTRA_SPACES)
    result = message_validator.validate_add_message(content)
    assert "  " not in result

def test_invalid_add_message_incomplete():
    content = message_validator.get_message_content(INVALID_ADD_MESSAGE_INCOMPLETE)
    error = None
    try: 
        _ = message_validator.validate_add_message(content)
    except Exception as e:
        error = str(e)
    assert error == "Message provided is missing some information"

def test_invalid_add_message_no_cost():
    content = message_validator.get_message_content(INVALID_ADD_MESSAGE_NO_COST)
    error = None
    try: 
        _ = message_validator.validate_add_message(content)
    except Exception as e:
        error = str(e)
    assert error == "Message provided does not include a number"
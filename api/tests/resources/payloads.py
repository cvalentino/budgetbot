VALID_LINEITEM_PAYLOAD = {
    "month": "APR", "day": 21, "description": "TEST-DELTEME", "category": "groceries", "cost": 1.23}
INVALID_LINEITEM_PAYLOAD_BAD_MONTH = {
    "month": "BAD", "day": 21, "description": "TEST-DELTEME", "category": "groceries", "cost": 25.2}
INVALID_LINEITEM_PAYLOAD_BAD_DAY = {
    "month": "JAN", "day": 0, "description": "TEST-DELTEME", "category": "groceries", "cost": 73.34}
INVALID_LINEITEM_PAYLOAD_BAD_CATEGORY = {
    "month": "FEB", "day": 2, "description": "TEST-DELTEME", "category": "shmategory", "cost": 100}
INVALID_LINEITEM_PAYLOAD_MISSING_FIELD = {
    "month": "MAR", "day": 2, "category": "groceries", "cost": 71.78}
INVALID_LINEITEM_PAYLOAD_STRING_DAY = {
    "month": "APR", "day": "NAN", "description": "TEST-DELTEME", "category": "groceries", "cost": 71.78}
INVALID_LINEITEM_PAYLOAD_STRING_COST = {
    "month": "APR", "day": 2, "description": "TEST-DELTEME", "category": "groceries", "cost": "NAN"}

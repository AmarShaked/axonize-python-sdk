from config import DEVICE_ID, PRODUCT_ID, APP_ID, HUB_KEY
from datetime import datetime
from hub_client import send

def create_fake_event():
  payload = {}
  payload["app_id"] = APP_ID
  payload["product_id"] = PRODUCT_ID
  payload["device_id"] = DEVICE_ID
  payload["dateTime"] = str(datetime.now())
  payload["type"] = 8
  payload["name"] = "Humidity"
  payload["value"] = 27
  payload["unit"] = "%"
  return payload

def callback(message, result, user_context):
  print ( "Confirmation received for message with result: %s" % result )


def main():
  payload = create_fake_event()
  send(payload, callback)


if __name__ == '__main__':
  main()

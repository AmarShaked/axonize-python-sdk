from config import HUB_KEY, DEVICE_ID
from json import dumps
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

CONNECTION_STRING = 'HostName=axonizestaginghub.azure-devices.net;DeviceId=%s;SharedAccessKey=%s' % (DEVICE_ID, HUB_KEY)
PROTOCOL = IoTHubTransportProvider.HTTP
MESSAGE_TIMEOUT = 10000

client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
client.set_option("messageTimeout", MESSAGE_TIMEOUT)

def send(payload, callback):
  payload_json = dumps(payload)
  message = IoTHubMessage(payload_json)

  try:
    client.send_event_async(message, callback, 1)
  except IoTHubError as iothub_error:
    print ( "Unexpected error %s from IoTHub" % iothub_error )

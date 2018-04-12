from pubnub import Pubnub

pubnub = Pubnub(
    publish_key = "pub-c-b0397ad5-c7e4-4b7e-b5a3-e7b41637b984",
    subscribe_key = "sub-c-b487e99c-3c9e-11e8-8bb7-3ab51ec5ed79")
channel = "my_channel"
message = "A message"

pubnub.publish(
    channel = channel,
    message = "A message")
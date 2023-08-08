#from twilio import
from twilio.rest import Client
account_sid = "ACac55eabc8847e1c9dc33fcafe05d207a"
auth_token = "31c5bc241bc08596e769f8eef0927006"
# +12546154115
class NotificationManager():
    def __init__(self):
        self.account_id = account_sid
        self.auth_token = auth_token
        # self.client = Client(self.account_id, self.auth_token)

    def message_send(self, lower_Price, flightData):
        try:
            if flightData.price <= lower_Price:
                pound_symbol = "£"
                client = Client(self.account_id, self.auth_token)
                message = client.messages \
                    .create(
                    body=f"Low price alert!Only {pound_symbol}{flightData.price} to fly from London-{flightData.origin_airport} to {flightData.destination_city}-{flightData.destination_airport}, from {flightData.out_date} to {flightData.return_date}",
                    from_='+12542726273',
                    to='+918860317648'
                )
                print(message.status)
        except TypeError:
            pass
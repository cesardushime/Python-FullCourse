from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body="This is a test message! \n"
         " I just wanted to test out my \n"
         "automated message in the sms automation \n"
         "project that I am working on. "
         "\n"
         "Thank you for being our participant\n\n"
         
         "Cesar.Dushimimana!!",
    from_=keys.twilio_number,
    to=keys.my_phone_number)

print(message.body + "was sent to " + keys.my_phone_number + " successfully ")
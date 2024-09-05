from twilio.rest import Client
from config import account_sid, auth_token, fromphone, myphone, apppasswords, receiveremail,email,text
from smtplib import SMTP
e='error amigo'
# with SMTP('smtp.gmail.com', 587) as smtp:
                
#     smtp.starttls()
#     smtp.login(email,apppasswords)
#     smtp.sendmail(email,receiveremail,text)
# with SMTP('smtp.gmail.com', 587) as smtp:       
#     smtp.starttls()
#     smtp.login(email,apppasswords)
#     smtp.sendmail(email,receiveremail,text)
client = Client(account_sid, auth_token)
message = client.messages.create(
from_=f'whatsapp:{fromphone}',
body=e,
to=f'whatsapp:{myphone}'
)
print(message.sid)
# client = Client(account_sid, auth_token)
# message = client.messages.create(
# from_=f'whatsapp:{fromphone}',
# body=e,
# to=f'whatsapp:{myphone}'
# )
# print(message.sid)
from twilio.rest import Client 
 
account_sid = 'ACce98535e0e233ed26da8b45191d3ccbd' 
auth_token = 'ad44aa8990cae29c2402451eb13a3b3d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+14243651465',  
                              body='Hello Wife!!!',      
                              to='+12062939234' 
                          ) 
 
print(message.sid)
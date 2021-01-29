import tweepy

consumer_key = '8AWcilK1tplRJipEUQRpm9517'
consumer_secret = 'iB5PfwP6dJJiZ2xP5cu7bEzXCiMd0LVRbDpSWWboN0Ur3muRN6'
access_token = '1348054932067209216-7cOLLGfsoLG4mlIicOgxNEUAxXz1aL'
access_token_secret = 'Py28q4JGIMho3iOrllyocGen9sNYa9C2rSMyG341Fg9JO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
user_name = 'jessdhanson'

for follower in tweepy.Cursor(api.followers, user_name).items():
    print(follower.name)

# recipient_id = 1224744891084705792
# message = "Hi Jess this is from my little program I'm working on, are you proud???"
# user = api.get_user('jessdhanson')
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)
# api.send_direct_message(recipient_id, message)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
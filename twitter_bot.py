import tweepy
import time



consumer_key='E22Ak6pu2Zz2k9MJnxTrUNFth'
consumer_secret='gFcZCyPMrto62pjeAbKqDYaLFBhvqIKiikT6Z1utOfm54jrWZF'
access_key='1394228586383478786-HhXKFE2AaYHJwVSucAxXwWVBPELmle'
access_secret='qg7EAvybEBxkNO0uVfDCvLpgLJAnl66YmA5XMLQVXwugk'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)


FILE_NAME='last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read=open(file_name,'r')
    last_seen_id=int(f_read.read().strip())
    f_read.close() 
    return last_seen_id
def store_last_seen_id(last_seen_id,file_name):
    f_write=open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    last_seen_id= retrieve_last_seen_id(FILE_NAME)
    mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id=mention.id;
        store_last_seen_id(last_seen_id,FILE_NAME)
        text=mention.full_text.lower()
        if '#scrap' in text:
               original_id=mention.in_reply_to_status_id
               tweet=api.get_status(original_id,tweet_mode='extended')
               a=tweet.full_text
               recipient_name=mention.user.screen_name
               user=api.get_user(recipient_name)
               id=user.id_str
               api.send_direct_message(id,a)
while True:
   reply_to_tweets()
   time.sleep(15)

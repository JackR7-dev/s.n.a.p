import os
import tweepy
import random
import img_generator
import twitter_auth

# function that get a random pic inside OUTPUT folder, upload the pic for the post and get the media_id that will be used to create the tweet
def upload_img_and_return_id():
    random_number = random.randint(0, len(img_generator.dir_list) - 1)
    for n in range(3):
        try:
            img = img_generator.dir_list[random_number]
            img_path = img_generator.output_path + "\\" + img
            media_id = twitter_auth.api.media_upload(filename=img_path).media_id_string
        except Exception as e:
            continue
        else:
            break
    
    return media_id
import tweepy
import schedule
import time
import os
import random
import config
import twitter_auth
import img_generator
import img_upload
from PIL import Image

output_path = "E:\Files\Programming\Projects\S.N.A.P. (Smart Neural Art Poster)\OUTPUT"
# getting the list of elements inside OUTPUT folder
dir_list = os.listdir(output_path)


img_generator.generate_images("A panda eating a rock")
img_generator.verify_images(dir_list)
media_id = img_upload.upload_img_and_return_id()

# creating the tweet and passing the media id as a list even if it's only one string. 
# The function create_tweet require a list when passing a media_ids parameter
twitter_auth.client.create_tweet(media_ids=[media_id])

print("Tweeted")
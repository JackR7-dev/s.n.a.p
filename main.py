import tweepy
import schedule
import time
import os
import random
import config
from PIL import Image

bing_api = '1G3iWtGpFuD8Yj1bItIS4D7XbwijaR94Hs7ByeFi9IVeeDnNTEyfhIjvXkT1FmW0puys8uc9RcGHvPcqr0gElGrUst8W-DaHDDTYdcIyZPwRmrJKf8RTl4YX2eJ0aYk2Pe8Vod3LsALI7hFnAZMvVMlP7jP87pa9sZBSYm9xgpMXjKhn6ixCToaKWp031dWfY1_IEk-xDx-xWXKeq7anP_g'

# setting authentication
auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# setting the client
client = tweepy.Client(
    config.bearer_token,
    config.api_key,
    config.api_key_secret, 
    config.access_token, 
    config.access_token_secret)

output_path = "E:\Files\Programming\Projects\S.N.A.P. (Smart Neural Art Poster)\OUTPUT"
# getting the list of elements inside OUTPUT folder
dir_list = os.listdir(output_path)

# function that generate images based on prompt parameter. It cycle the image list directory so it can delete previuous generated images.
# Then it run a command line to generate images and save it in the OUTPUT folder
def generate_images(prompt):
    for img in dir_list:
        os.remove(output_path + "\\" + img)
    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{bing_api}"'
    os.system(command)
    return os.listdir("OUTPUT")

# function that check if the generated images is corrupted or can't be opened
def verify_images(dir_list):
    for img in dir_list:
        try:
            img_check = Image.open(output_path + "\\" + img)
            img_check.verify()
        except:
            os.remove(output_path + "\\" + img)
    return True

# function that get a random pic inside OUTPUT folder, upload the pic and get the media_id that will be used to create the tweet
def upload_img_and_return_id():
    random_number = random.randint(0, len(dir_list) - 1)
    img = dir_list[random_number]
    img_path = output_path + "\\" + img
    media_id = api.media_upload(filename=img_path).media_id_string
    return media_id

generate_images("A super hero is fighting a villain on the sea")
verify_images(dir_list)
media_id = upload_img_and_return_id()

# creating the tweet and passing the media id as a list even if it's only one string. 
# The function create_tweet require a list when passing a media_ids parameter
client.create_tweet(media_ids=[media_id])

print("Tweeted")
import twitter, json, time, os, random
# Imports the needed requirements.

with open("config.json", "r") as unloaded_config:
    config = json.load(unloaded_config)
# Loads the config.

api = twitter.Api(consumer_key = config["consumerKey"], consumer_secret = config["consumerSecret"], 
access_token_key = config["accessTokenKey"], access_token_secret = config["accessTokenSecret"])
# Defines the Twitter API.

def post():
    try:
        file = random.choice(os.listdir(config["directory"]))
        api.PostUpdate("", file)
        print(f"I have uploaded {file}!")
    except:
        print(f"I have failed to upload {file}. I'll try again in an hour.")
        pass
# Creates the function for finding and posting files.

while True:
    post()
    time.sleep(config["sleepTime"])
# Executes the post function and sleeps for the preset time.

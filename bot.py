import twitter, json, time, os, random
# Imports the needed requirements.

info = "[Info] "
success = "[Success] "
error = "[Error] "
# Defines the prefixes for better logging. 

print(info + "Starting..")
# Prints a message declaring the bot is starting. 

try:
    with open("config.json", "r") as unloaded_config:
        config = json.load(unloaded_config)
        print(success + "Config has been loaded")
except:
    print(error+ "Config could not be loaded")
    return
# Loads the config.

try:
    api = twitter.Api(consumer_key = config["consumerKey"], consumer_secret = config["consumerSecret"], 
    access_token_key = config["accessTokenKey"], access_token_secret = config["accessTokenSecret"])
    print(success + "Connected to the Twitter API")
except:
    print(error + "Connection could not be established to the Twitter API")
    return
# Defines and connects to the Twitter API.

def post():
    try:
        upload = random.choice(os.listdir(config["directory"]))
        if not upload.lower().endswith((".png", ".jpg", ".jpeg", ".mp4")):
            raise Exception
        if config["enableOneTime"] == True:
            file = open("uploaded.txt", "r+")
            for line in file:
                if line == upload:
                    raise Exception
                else:
                    pass
        #api.PostUpdate("", upload)
        if config["enableOneTime"] == True:
            file.write(f"{upload}\n")
            file.close()
        print(success + f"Uploaded {upload}!")
    except:
        print(error + f"Failed to upload {upload}. I'll try again later.")
        pass
# Creates the function for finding and posting files.

sleep_for = config["sleepTime"]

while True:
    post()
    print(info + f"Sleeping for {sleep_for}s")
    time.sleep(sleep_for)
# Executes the post function and sleeps for the preset time.

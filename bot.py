import twitter, json, time, os, random, builtins
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
    exit()
# Loads the config.

try:
    api = twitter.Api(consumer_key = config["consumerKey"], consumer_secret = config["consumerSecret"], 
    access_token_key = config["accessTokenKey"], access_token_secret = config["accessTokenSecret"])
    print(success + "Connected to the Twitter API")
except:
    print(error + "Connection could not be established to the Twitter API")
    exit()
# Defines and connects to the Twitter API.

def post():
    try:
        builtins._pass = True
        upload = random.choice(os.listdir(config["directory"]))
        if not upload.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".mp4")):
            raise Exception
        if config["enableOneTime"] == True:
            file = open("uploaded.txt", "r+")
            if upload in file.read().split(","):
                raise Exception
            else:
                pass
        api.PostUpdate("", upload)
        if config["enableOneTime"] == True:
            file.write(f"{upload},")
            file.close()
        print(success + f"Uploaded {upload}!")
    except:
        print(error + f"Failed to upload {upload}. Trying again..")
        builtins._pass = False
        pass
# Creates the function for finding and posting files.

sleep_for = config["sleepTime"]
# Pulls the period of time to sleep for from config and defines it.

while True:
    post()
    if _pass == False:
        post()
        if _pass == False:
            post()
            if _pass == False:
                print(error + "Failed to upload after three attempts.")
    print(info + f"Sleeping for {sleep_for}s")
    time.sleep(sleep_for)
# Executes the post function and sleeps for the preset time.

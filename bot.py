import tweepy, json, time, os, random, builtins, requests, urllib.request
# Imports the needed requirements.

class log:
    def info(text: str):
        print(f"[Info] {text}")
    def success(text: str):
        print(f"[Success] {text}")
    def error(text: str):
        print(f"[Error] {text}")
# The class for outputting console logs.

log.info("Starting..")
# Prints a message declaring the bot is starting. 

try:
    with open("config.json", "r") as unloaded_config:
        config = json.load(unloaded_config)
        log.success("Config has been loaded")
except:
    log.error("Config could not be loaded")
    exit()
# Loads the config.

try:
    auth = tweepy.OAuthHandler(config["consumerKey"], config["consumerSecret"])
    auth.set_access_token(config["accessTokenKey"], config["accessTokenSecret"])
    api = tweepy.API(auth)
    log.success("Connected to the Twitter API")
except:
    log.error("Connection could not be established to the Twitter API")
    exit()
# Defines and connects to the Twitter API.

log.info(f"User: {api.me().screen_name}")
log.info(f"Followers: {api.me().followers_count}")
time.sleep(1)
# Prints basic information about the account when ready, then pauses for a second.

def post():
    try:
        upload = random.choice(os.listdir(config["directory"]))
        if not upload.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".mp4")):
            raise Exception
        if config["enableOneTime"]:
            with open("uploaded.json", "r") as unloaded_uploads:
                file = json.load(unloaded_uploads)
            if upload in file:
                raise Exception
            else:
                file.append(upload)
        api.update_with_media(config["directory"] + upload)
        if config["enableOneTime"]:
            with open("uploaded.json", "w") as unloaded_uploads:
                json.dump(file, unloaded_uploads)
        log.success(f"Uploaded {upload}!")
        return True
    except:
        try:
            log.error(f"Failed to upload {upload}. Trying again..")
        except:
            log.error("Failed to upload. Trying again..")
        return False
# Defines the function for finding and posting files.

reddit_name=config["redditName"]
builtins.attempts = 0
# Defining vars for Reddit.

def reddit():
    try:
        with requests.get(f"https://www.reddit.com/r/{reddit_name}/new.json", headers={"user-agent": "Simple-Tweeter"}) as url:
            data = json.loads(url.content)["data"]["children"][attempts]["data"]
        url = data["url"]
        upload = url.split("/")[-1]
        urllib.request.urlretrieve(url, upload)
        if config["enableOneTime"]:
            with open("uploaded.json", "r") as unloaded_uploads:
                file = json.load(unloaded_uploads)
            if upload in file:
                raise Exception
            else:
                file.append(upload)
        api.update_with_media(upload)
        os.remove(upload)
        if config["enableOneTime"]:
            with open("uploaded.json", "w") as unloaded_uploads:
                json.dump(file, unloaded_uploads)
        log.success(f"Uploaded {upload}!")
        builtins.attempts += 1
        return True
    except:
        try:
            log.error(f"Failed to upload {upload}. Trying again..")
        except:
            log.error("Failed to upload. Trying again..")
        builtins.attempts += 1
        return False
            
sleep_for = config["sleepTime"]
# Pulls the period of time to sleep for from config and defines it.

while True:
    while True:
        if config["enableReddit"]:
            if reddit():
                break
        else:
            if post():
                break
    log.info(f"Sleeping for {sleep_for}s")
    time.sleep(sleep_for)
#Executes the post function and sleeps for the preset time.

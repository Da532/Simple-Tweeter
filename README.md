# Simple-Tweeter

A bot to randomly tweet images every hour or so. 🐦

## Setup

Setup is simple for the bot. With your Twitter developer application, open config.json and input your consumer key, consumer secret, access token key and access token secret. Along with this you are also needed to specify the path the files will be grabbed from and randomised along with the amount of time in seconds you wish there to be between posts. You also have the option of enabling the OneTime mode. This will make sure the same images are not reposted as their names will already be writted to a text file. This is enabled by default but if you feel as if you do not need this feature you can set it to `false` in the config and delete the text file.

If you are intending to use the Reddit function, set it to `true` in the config and add the Reddit's name.

You are also required to install the module `tweepy` using pip. This is a very simple process and as long as you have Python 3.6 installed to path you should be able to open any command window (terminal / cmd) and enter the following:

`pip install tweepy`

## Bugs?

If you find any, please raise an issue as this is my first project using this API and I could have implemented it better if I spent more time on this project. 

Please enjoy! 😄

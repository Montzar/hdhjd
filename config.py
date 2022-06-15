import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABeWGGJM8vofCuVewpyDRFgL_pwRi2fkVPA1Omw8o_QgObDMGtRquzW7uX6OGr6bLP4LxLHwCcjtkUjwKA8ba-LijS26lWoqoI6mFCdwcDUtMnrG48iViGuhoVmW7HSzwT3Qvo1pcvwcM8e7-0xpOsS7q7XQKJusSjPEHiy9W6WdMZYFHJGOLBcc0zmzWRiPZIW89URtkPekbngabAhNNj67IUWXFh-G3UDh68YuZpmMzANOXjftQnhIBNhh_mM-zI_fJWNeUGlErR-xA9WFg1JoWtPfa37IQ6Ag95KjbuTnXfe1xwMiqkvOw8QD4JhymPsBefersu7icP9E2YXoGNnAAAAAUU_RcQA")
BOT_TOKEN = getenv("BOT_TOKEN","5308671551:AAE531tnS97-OARqxoBJtKKOIyZ_rPGmliU")
BOT_NAME = getenv("BOT_NAME", "Mu5ical")
API_ID = int(getenv("API_ID","19223176"))
API_HASH = getenv("API_HASH","501458c547877e2fb2e3907b83f8d00f")
OWNER_NAME = getenv("OWNER_NAME", "montzer")
ALIVE_NAME = getenv("ALIVE_NAME", "montzer")
BOT_USERNAME = getenv("BOT_USERNAME", "Mu5ical_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mu5ical")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CHTLHB")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Mu5icall")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5313375615").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")

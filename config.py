import os

API_ID = API_ID = 25038096

API_HASH = os.environ.get("API_HASH", "098112aae38be62db58363267a061b59")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7474349630:AAEfHnzQSVgOsWNS8G9a12CdHCvR9RJ96XU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5201266500").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22142564"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "65058bd78a47f97e48cb99ff32ea29fe")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://parvistmalik:Malik@123@cluster0.ylpmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

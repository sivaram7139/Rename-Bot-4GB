import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23246613")

API_HASH = os.environ.get("API_HASH", "b94000048d3e07bd33f1830edb2ef4f0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7741808740:AAGdTXAixCeFP-I0rLB29H3XeUqa28J30jE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "KBCRename_bot") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://kandula:#Bhanu000#@cluster0.rwv5s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1286239869').split()]

PORT = os.environ.get("PORT", "8080")

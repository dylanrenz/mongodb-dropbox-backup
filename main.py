import dropbox
import json
from pymongo import MongoClient
from datetime import date
from datetime import datetime, timedelta
import schedule
import time


def backup_to_dropbox():
 
    print("🔄 Starting backup...")

    # Setup
    APP_KEY = "app_key_placeholder"
    APP_SECRET = "app_secret_placeholder"
    REFRESH_TOKEN = "refresh_token_placeholder"

    # Create Dropbox client using refresh token flow
    dbx = dropbox.Dropbox(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        oauth2_refresh_token=REFRESH_TOKEN
    )
    client = MongoClient("mongo_string_placeholder")
    db = client["collection_name_placeholder"]

    # Date for filename
    today = date.today().isoformat()

    # Backup and upload each collection
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        cursor = collection.find()

        dropbox_file_path = f"/file_path_placeholder/{today}_{collection_name}.json"

        json_lines = ""
        for doc in cursor:
            json_lines += json.dumps(doc, default=str) + "\n"

        try:
            dbx.files_upload(json_lines.encode("utf-8"), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite)
            print(f"✅ Uploaded {collection_name} to Dropbox at {dropbox_file_path}")
        except Exception as e:
            print(f"❌ Failed to upload {collection_name}: {e}")

    print("✅ Backup complete!")

schedule.every().monday.at("06:30").do(backup_to_dropbox)
schedule.every().tuesday.at("06:30").do(backup_to_dropbox)
schedule.every().wednesday.at("06:30").do(backup_to_dropbox)
schedule.every().thursday.at("06:30").do(backup_to_dropbox)
schedule.every().friday.at("06:30").do(backup_to_dropbox)
# Keep the script running continuously to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

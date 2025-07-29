import dropbox
import json
from pymongo import MongoClient
from datetime import date
from datetime import datetime, timedelta
import schedule
import time


def backup_to_dropbox():
 
    print("🔄 Starting backup...")

    
    DROPBOX_TOKEN = "" # Replace with your actual token
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)
    client = MongoClient("") # Replace with your actual MongoDB connection string
    db = client[""] # Replace with your actual database name

    
    today = date.today().isoformat()

    # Backup and upload each collection
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        cursor = collection.find()

        dropbox_file_path = f"/path to file/{today}_{collection_name}.json" #replace with actual path

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
schedule.every().tuesday.at("10:58").do(backup_to_dropbox)
schedule.every().wednesday.at("06:30").do(backup_to_dropbox)
schedule.every().thursday.at("06:30").do(backup_to_dropbox)
schedule.every().friday.at("06:30").do(backup_to_dropbox)
# Keep the script running continuously to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

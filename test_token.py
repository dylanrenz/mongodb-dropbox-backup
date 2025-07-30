import dropbox

# Replace with your actual values
APP_KEY = "placeholder_app_key"
APP_SECRET = "placeholder_app_secret"
REFRESH_TOKEN = "placeholder_refresh_token"

# Create Dropbox client using refresh token flow
dbx = dropbox.Dropbox(
    app_key=APP_KEY,
    app_secret=APP_SECRET,
    oauth2_refresh_token=REFRESH_TOKEN
)

# Try uploading a small test file
try:
    content = b"Hello, Dropbox!"
    path = "/test_upload.txt"
    dbx.files_upload(content, path, mode=dropbox.files.WriteMode.overwrite)
    print(f"✅ Upload successful: {path}")
except Exception as e:
    print(f"❌ Error: {e}")

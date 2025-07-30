from dropbox import DropboxOAuth2FlowNoRedirect

APP_KEY = 'app_key_placeholder'
APP_SECRET = 'secret_key_placeholder'

auth_flow = DropboxOAuth2FlowNoRedirect(
    APP_KEY,
    APP_SECRET,
    token_access_type='offline'  # this gives you a refresh token
)

authorize_url = auth_flow.start()

print("1. Visit this URL and allow access:", authorize_url)
print("2. Paste the code you receive below.")

auth_code = input("Enter the code here: ").strip()
oauth_result = auth_flow.finish(auth_code)

print("✅ Access token:", oauth_result.access_token)
print("✅ Refresh token:", oauth_result.refresh_token)

import urllib.parse

client_id = 'd51b67e2-6768-415c-950f-b1f217a074ba'  # Replace with your actual client ID
redirect_uri = 'http://localhost:3000/ds/callback'  # Replace with your actual redirect URI

base_url = 'https://account-d.docusign.com/oauth/auth'
#base_url = "https://demo.docusign.net/oauth/auth"
params = {
    'response_type': 'code',
    'scope': 'signature',
    'client_id': client_id,
    'redirect_uri': redirect_uri
}

# Construct the OAuth URL
oauth_url = f"{base_url}?{urllib.parse.urlencode(params)}"

print('Visit the following URL to authorize the application:')
print(oauth_url)



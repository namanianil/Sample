import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

client_secret='335bba05-228d-45b1-a631-ea35be5aa459'
app_id='api://bdc56950-a025-42fe-badf-7435447eb7eb'
SCOPES=['User.Read']

client = ConfidentialClientApplication(client_id=app_id,client_credential=client_secret)
authorization_url=client.get_authorization_request_url(SCOPES)
print(authorization_url)

webbrowser.open(authorization_url)
'hello world'

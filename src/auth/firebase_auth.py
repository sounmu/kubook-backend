import json

from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials as fb_credentials

from config import Settings

cred = fb_credentials.Certificate(json.loads(Settings().FIREBASE_SERVICE_ACCOUNT_KEY))
firebase_admin.initialize_app(cred)

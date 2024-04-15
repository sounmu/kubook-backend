"""
참고:
- https://gist.github.com/billydh/734e5cc4d78d46e497b4f0589bc34ac0
- https://firebase.google.com/docs/reference/rest/auth?hl=ko#section-sign-in-email-password
"""

import argparse
import json
import os
import requests
import pprint

from config import Settings

FIREBASE_WEB_API_KEY = Settings().FIREBASE_WEB_API_KEY
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


async def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

    response = r.json()

    try:
        localId = response["localId"]
        return localId
    except KeyError:
        error = response["error"]["message"]
        """
        발생할 수 있는 에러
        - EMAIL_NOT_FOUND: 사용자의 이메일이 존재하지 않음
        - INVALID_PASSWORD: 비밀번호가 틀림
        - USER_DISABLED: 사용자 계정이 비활성화됨
        """
        return error

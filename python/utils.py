import os
import hashlib

import requests
import base64


# Collect vars from system environment variables
USERNAME = os.getenv('GLYNT_USERNAME')
PASSWORD = os.getenv('GLYNT_PASSWORD')


def get_token():
    """Get username and password from the os environment variables, then get
    and return an api auth token and token type.
    """
    resp = requests.post(
        url='https://api.glynt.ai/v6/auth/get-token/',
        headers={'content-type': 'application/json'},
        json={
            'username': USERNAME,
            'password': PASSWORD
        }
    )
    assert resp.status_code == 200
    token = resp.json()['access_token']
    token_type = resp.json()['token_type']
    return (token, token_type)


def get_content_md5(filepath):
    """Given a filepath, return the Content-MD5 for the file's content."""
    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            md5.update(data)
    digest = md5.digest()
    return base64.b64encode(digest).decode('utf-8')


def get_content_b64(filepath):
    """Given a filepath, return the base64 encoded representation of the
    file's content.
    """
    with open(filepath, 'rb') as f:
        content = f.read()
        return base64.b64encode(content).decode('utf-8')

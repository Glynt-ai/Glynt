#!/usr/bin/env python3
import base64
import hashlib
import os

import fire
import requests


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


def upload_document(
    data_pool_id,
    label,
    content_type,
    filepath
):
    token, token_type = get_token()

    content_md5 = get_content_md5(filepath)

    # POST document and store response content
    resp = requests.post(
        url=f'https://api.glynt.ai/v6/data-pools/{data_pool_id}/documents/',
        headers={
            'Authorization': f'{token_type} {token}',
            'content-type': 'application/json'
        },
        json={
            'label': label,
            'content_type': content_type,
            'content_md5': content_md5
        }
    )
    assert resp.status_code == 201
    document = resp.json()

    # PUT document content
    with open(filepath, 'rb') as f:
        resp = requests.put(
            url=document['file_upload_url'],
            headers={
                'content-type': content_type,
                'content-md5': content_md5
            },
            data=f.read()
        )
    assert resp.status_code == 200

    return document


if __name__ == '__main__':
    fire.Fire(upload_document)

#!/usr/bin/env python3
import fire
import requests

from utils import get_token, get_content_b64


def upload_document(
    data_pool_id,
    label,
    content_type,
    filepath
):
    token, token_type = get_token()

    content_b64 = get_content_b64(filepath)

    resp = requests.post(
        url=f'https://api.glynt.ai/v6/data-pools/{data_pool_id}/documents/',
        headers={
            'Authorization': f'{token_type} {token}',
            'content-type': 'application/json'
        },
        json={
            'label': label,
            'content_type': content_type,
            'content': content_b64
        }
    )
    assert resp.status_code == 201
    document = resp.json()

    return document


if __name__ == '__main__':
    fire.Fire(upload_document)

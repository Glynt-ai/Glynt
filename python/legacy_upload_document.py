#!/usr/bin/env python3
import fire
import requests

from utils import get_token, get_content_md5


def legacy_upload_document(
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
    fire.Fire(legacy_upload_document)

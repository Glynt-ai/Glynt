# Python Code Examples

This directory contains code examples for interacting with GLYNT services in
Python3.6+. They require that you have installed the requirements from
requirements.txt to your env (or better yet, a virtual environment). They also
assume that you have exported a valid `GLYNT_USERNAME` and `GLYNT_PASSWORD` to
your OS environment variables.

## upload_document.py

This script uploads a document from your local system to a data pool of your
choice. To run it, make sure you have the ID of the data pool you'd like to
upload to, have the file on your computer, and know it's type (see
https://api.glynt.ai/v6/docs#create-a-document for information on supported
file types and the exact string to use for each) This script is invoked like
so:

```shell
./upload_document.py <data_pool_id> <label> <content_type> <filepath>
```
For example:
```shell
./upload_document.py H75fui my_awesome_document application/pdf /home/myuser/myawesomedoc.pdf
```

## legacy_upload_document.py

This script is an example of the legacy method of uploading a document to Glynt.
See the glynt documentation for details of the differences between this and the
currently recommended method of uploading. It can be run in the same way as
upload_document.py.

```shell
./legacy_upload_document.py <data_pool_id> <label> <content_type> <filepath>
```
For example:
```shell
./legacy_upload_document.py H75fui my_awesome_document application/pdf /home/myuser/myawesomedoc.pdf
```

## utils.py

This module contains utility methods used by the upload scripts to generate the
different data types required by Glynt. This includes methods to generate an
md5 hash or a base64 representation of a document before uploading. It also
includes a method which handles user authorization before making api requests.

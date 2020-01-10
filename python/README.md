# Python Code Examples

This directory contains code examples for interacting with GLYNT services in
Python3.6+. They require that you have installed the requirements from
requirements.txt to your env (or better yet, a virtual environment). They also
assume that you have exported a valid `GLYNT_USERNAME` and `GLYNT_PASSWORD` to
your OS envrinoment variables.

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

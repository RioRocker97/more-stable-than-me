from os import getcwd,environ
from google.cloud import storage
GCP_BUCKET = environ['GCP_B']
GCP_BUCKET_URL = environ['GCP_B_URL']
def upload_to_bucket(name,img_data):
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(GCP_BUCKET)
        blob = bucket.blob(name+'.png')

        blob.upload_from_string(img_data,content_type='image/png')
        print('Imaged Upload !')
        return GCP_BUCKET_URL+name+'.png'
    except Exception as e:
        print('Error Uploading to GCP Storage')
        print(e)
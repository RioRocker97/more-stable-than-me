from os import getcwd,environ
from google.cloud import storage
GCP_BUCKET = environ['GCP_B']
GCP_BUCKET_URL = environ['GCP_B_URL']
def upload_to_bucket(name,img_data):
    try:
        new_name = ''
        for index,item in enumerate(name.split(' ')):
            new_name += item
            if index != len(name.split(' '))-1:
                new_name += '-'
        storage_client = storage.Client()
        bucket = storage_client.bucket(GCP_BUCKET)
        blob = bucket.blob(new_name+'.jpg')

        blob.upload_from_string(img_data,content_type='image/jpeg')
        print('Imaged Upload !')
        return GCP_BUCKET_URL+new_name+'.jpg'
    except Exception as e:
        print('Error Uploading to GCP Storage')
        print(e)
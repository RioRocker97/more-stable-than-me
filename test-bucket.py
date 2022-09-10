from io import BytesIO
from img_storage import upload_to_bucket
from lang_translator import translate
from PIL import Image
from io import BytesIO
img = Image.open('./1.png')
img.convert('RGB')
byte_img = BytesIO()
img.save(byte_img,format='PNG')
prompt = 'new image in jpg'
print(upload_to_bucket(translate(prompt),byte_img.getvalue()))
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline,EulerDiscreteScheduler
from io import BytesIO
from img_storage import upload_to_bucket
from lang_translator import translate
MODEL_ID = 'stabilityai/stable-diffusion-2'
DEVICE = 'cuda'
SCHEDULER = EulerDiscreteScheduler.from_pretrained(MODEL_ID, subfolder="scheduler")
PIPE = StableDiffusionPipeline.from_pretrained(MODEL_ID,scheduler=SCHEDULER,torch_dtype=torch.float16,revision="fp16",use_auth_token=True).to(DEVICE)

def txt2img(prompt:str):
    with autocast(DEVICE):
        image = PIPE(prompt,width=512,height=512).image[0]
        image.convert('RGB')
        byte_img = BytesIO()
        image.save(byte_img,format='PNG')
        return upload_to_bucket(translate(prompt),byte_img.getvalue())

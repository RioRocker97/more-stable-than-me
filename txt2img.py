from io import BytesIO
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from io import BytesIO
from img_storage import upload_to_bucket
MODEL_ID = 'CompVis/stable-diffusion-v1-4'
DEVICE = 'cuda'
PIPE = StableDiffusionPipeline.from_pretrained(MODEL_ID,torch_dtype=torch.float16,revision="fp16",use_auth_token=True).to(DEVICE)

def txt2img(prompt):
    with autocast(DEVICE):
        image = PIPE(prompt)["sample"][0]
        byte_img = BytesIO()
        image.save(byte_img,format='PNG')
        return upload_to_bucket('Whatever',byte_img)

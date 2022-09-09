import torch,argparse
from torch import autocast
from diffusers import StableDiffusionPipeline

parser = argparse.ArgumentParser()
parser.add_argument('prompt',action='store',type=str)
parser.add_argument('filename',action='store',type=str)

args = parser.parse_args()

model_id = 'CompVis/stable-diffusion-v1-4'
device = 'cuda'

pipe = StableDiffusionPipeline.from_pretrained(model_id,torch_dtype=torch.float16,revision="fp16",use_auth_token=True)
pipe = pipe.to(device)

with autocast(device):
    image = pipe(args.prompt,guidance_scale=7.5)["sample"][0]
    image.save(args.filename)
    print('Image Saved !')

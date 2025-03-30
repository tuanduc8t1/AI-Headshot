import sys
import types
import torchvision.transforms.functional as F
import torchvision.transforms
import gradio as gr
from diffusers import FluxPipeline
import torch
import numpy as np
from PIL import Image
from gfpgan import GFPGANer

gfpganer = GFPGANer(
    model_path="/workspace/SimpleTuner/GFPGANv1.4.pth",
    upscale=2,
    arch='clean',
    channel_multiplier=2,
    device='cuda'
)

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16
)
pipe.load_lora_weights("/workspace/SimpleTuner/output/models/checkpoint-400/pytorch_lora_weights.safetensors")
pipe = pipe.to("cuda")

def gen_img(prompt, width, height):
    image = pipe(
        prompt=prompt,
        negative_prompt="blurry, deformed, cartoon, lowres, text, watermark, signature, extra limbs, poorly drawn, ugly, error, out of frame",
        num_inference_steps=25,
        guidance_scale=7.5,
        height=height,
        width=width,
    ).images[0]

    # image_np = np.array(image)
    # restored_img, _, _ = gfpganer.enhance(
    #     image_np,
    #     has_aligned=False,
    #     #only_center_face=True,
    #     paste_back=True
    # )
    # restored_img = restored_img[0]
    # final_image = Image.fromarray(restored_img)
    # image_path = "final_output.png"
    # final_image.save(image_path)
    return image


gr_interface = gr.Interface(
    fn=gen_img,
    inputs=[
        gr.Textbox(label="Enter Prompt"),
        gr.Slider(label="Image Width", minimum=512, maximum=1024, value=1024, step=64),
        gr.Slider(label="Image Height", minimum=512, maximum=1024, value=1024, step=64)
    ],
    outputs=gr.Image(label="Generated Image"),
    title="AI Headshot Generator",
    description="Generate images using Flux"
)

gr_interface.launch(share=True)

import sys
import types
import torchvision.transforms.functional as F
import torchvision.transforms
import gradio as gr
from diffusers import FluxPipeline
import torch
import numpy as np
from PIL import Image

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16
)

pipe.load_lora_weights("/workspace/SimpleTuner/output/models/checkpoint-200/pytorch_lora_weights.safetensors")
pipe = pipe.to("cuda")

def gen_img(prompt, negative_prompt, width, height, num_steps, guidance_scale):
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_steps,
        guidance_scale=guidance_scale,
        height=height,
        width=width,
    ).images[0]
    return image

gr_interface = gr.Interface(
    fn=gen_img,
    inputs=[
        gr.Textbox(label="Enter Prompt"),
        gr.Textbox(label="Negative Prompt"),
        gr.Slider(label="Image Width", minimum=512, maximum=1024, value=1024, step=64),
        gr.Slider(label="Image Height", minimum=512, maximum=1024, value=1024, step=64),
        gr.Slider(label="Number of Steps", minimum=1, maximum=100, value=25, step=1),
        gr.Slider(label="Guidance Scale", minimum=0, maximum=20, value=7.5, step=0.1)
    ],
    outputs=gr.Image(label="Generated Image"),
    title="AI Headshot Generator",
    description="Generate images using Flux"
)

gr_interface.launch(share=True)

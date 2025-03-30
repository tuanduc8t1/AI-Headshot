# This Tutorial is a Work-in-Progress

## Introduction

This guide provides a quick, simplified setup for training a LoRA model for the AI-HEADSHOT project using SimpleTuner. Before you begin, make sure you have set up a Python environment and created an "env" file for SimpleTuner. This document will help you get a basic training environment running, along with sample data if you don't have your own.

## Installation

**SimpleTuner requires Linux or MacOS (Apple Silicon).**

Follow these steps:

1. **Install Required Packages:**  
   Install the necessary packages as described in the project documentation.

2. **Prepare Training Data:**  
   Create valid training data (or use the provided example dataset).

3. **Configure SimpleTuner:**  
   - Copy the `config/config.json.example` file from the project root to `config/config.json`.
   - Fill in your configuration options. (Alternatively, run `configure.py` for an interactive setup.)

4. **Run the Training Script:**  
   Execute the `train.sh` script to start training.

> **Note:** If you are in a region with limited network access, add the following line to your shell configuration (`~/.bashrc` or `~/.zshrc`):
> 
> ```bash
> HF_ENDPOINT=https://hf-mirror.com
> ```

## Hardware Requirements

Ensure your hardware meets the requirements for the resolution and batch size you plan to use. High-end GPUs (24GB VRAM or more) are ideal, but for LoRA training, GPUs with 12GB–16GB can work. More VRAM is generally better; however, beyond 24GB the returns tend to diminish for smaller models.

## Dependencies

Install SimpleTuner following the instructions provided in the project documentation.

## Training Data

A sample dataset with about 10k images (each image’s filename serves as its caption) is available. You can use this or prepare your own images. Images can be placed in a single folder or organized in subdirectories.

### Guidelines for Training Data

#### Training Batch Size

Your maximum batch size depends on your VRAM and image resolution: vram use = batch size * resolution + base requirements
- Use the highest batch size that your hardware allows.
- Higher resolutions use more VRAM, forcing a smaller batch size.
- Ensure each batch contains enough unique images to avoid overexposure to the same data.

#### Selecting Images

- **Quality:** Avoid images with JPEG artifacts, blurriness, watermarks, or unwanted signatures.
- **Noise:** High-quality photographs are ideal; excessive sensor noise or compression artifacts can harm the model.
- **Resolution:** Ideally, use images with resolutions divisible by 64 for better processing, though this is not strictly required.
- **Variety:** Use a varied dataset to improve the model’s performance. Synthetic data can be useful, but mixing it with real images is recommended.

### Captioning

SimpleTuner can generate captions for your images using various methods. Captions may be sourced from:

- The image filename (default)
- A text file with the same name as the image (when using `--caption_strategy=textfile`)
- Other formats (e.g., JSONL, CSV)

*Tip:* Longer captions aren’t always better—using a mix of short and detailed captions is often most effective.

#### Caption Dropout

Caption dropout randomly replaces a caption with an empty string about 10% of the time. This helps improve image generation quality. Increasing dropout to 25% might reduce training steps but can also lead to the model "forgetting" details—use this option with care.

## Advanced Configuration

For users with advanced needs, more options (like mixed precision, offset noise, and zero terminal SNR) are available. This guide focuses on the essentials for the AI-HEADSHOT project.

## Publishing Checkpoints

To automatically push your model to a remote repository after training, set these values in `config/config.json`:

```json
"push_to_hub": true,
"hub_model_name": "your-model-name"





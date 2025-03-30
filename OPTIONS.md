# AI-HEADSHOT LoRA Training Options

This document provides a simplified summary of the command-line options available in SimpleTuner's `train.py` script. These options have been tailored for training a LoRA model for the AI-HEADSHOT project.

## Core Model Options

- **`--model_type`**  
  Select the training type. Options: `lora` (default) or `full`.

- **`--model_family`**  
  Specify the model family. Options include: `pixart_sigma`, `flux`, `sd3`, `sdxl`, `kolors`, `legacy`.

- **`--pretrained_model_name_or_path`**  
  Path to the pretrained model to use as the starting point.

## LoRA-Specific Options

- **`--lora_type`**  
  When training with `--model_type=lora`, choose the adapter type. Options: `standard` or `lycoris`.

- **`--lora_rank`**  
  Dimension for the LoRA update matrices.

- **`--lora_alpha`**  
  Alpha value for the LoRA update (affects learning rate for the LoRA parameters).

- **`--lora_dropout`**  
  Dropout rate to apply on LoRA layers to help prevent overfitting.

## Training Parameters

- **`--num_train_epochs`**  
  Number of times to iterate over the entire training dataset.

- **`--max_train_steps`**  
  Maximum number of training steps. This will override the number of epochs if set.

- **`--learning_rate`**  
  Initial learning rate for the optimizer.

- **`--train_batch_size`**  
  Batch size per device during training.

- **`--gradient_accumulation_steps`**  
  Number of steps to accumulate gradients before performing an update (helps manage memory).

## Optimizer Options

- **`--optimizer`**  
  Select the optimizer. For example: `adamw_bf16`.

- **`--optimizer_config`**  
  Override default optimizer settings with a comma-separated list of key-value pairs.

## Precision and Quantization

- **`--mixed_precision`**  
  Set the training precision. Options: `bf16` (default), `fp16`, or `no`.

- **`--base_model_precision`**  
  Optionally quantize the base model weights. Options include: `no_change`, `int8-quanto`, etc.

## Checkpointing and Resumption

- **`--checkpointing_steps`**  
  Save a checkpoint every X update steps.

- **`--resume_from_checkpoint`**  
  Resume training from a saved checkpoint if available.

## Logging and Monitoring

- **`--logging_dir`**  
  Directory for saving training logs (e.g., TensorBoard logs).

- **`--report_to`**  
  Specify the reporting integration (e.g., `tensorboard`, `wandb`, or `none`).

## Environment Variables (Set in `config.env`)

- **`TRAINING_NUM_PROCESSES`**  
  Number of GPUs available for training.

- **`TRAINING_DYNAMO_BACKEND`**  
  For NVIDIA hardware, set to `inductor` to potentially improve speed.

- **`SIMPLETUNER_LOG_LEVEL`**  
  Set the log level (e.g., `INFO`, `DEBUG`).

- **`VENV_PATH`**  
  Custom path to your Python virtual environment (if not using the default `.venv`).

## Example Command

Below is an example command to train a LoRA model for AI-HEADSHOT using simplified settings:

```bash
python train.py \
  --model_type lora \
  --model_family flux \
  --pretrained_model_name_or_path /path/to/model \
  --lora_type standard \
  --lora_rank 4 \
  --lora_alpha 32 \
  --num_train_epochs 10 \
  --learning_rate 1e-4 \
  --train_batch_size 4

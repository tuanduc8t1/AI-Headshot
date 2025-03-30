title: "SimpleTuner Setup for AI-Headshot (Linux)"
date: "2025-03-30"
description: "Setup guide for using SimpleTuner on a Linux device to train the LORA of the flux model for the AI-Headshot project."
tags:
  - SimpleTuner
  - AI-Headshot
  - Linux
  - LORA
  - flux model
guide:
  - section: "1. Repository Clone & Environment Setup"
    content: |
      Clone the SimpleTuner repository using the release branch:
      ```bash
      git clone --branch=release https://github.com/bghira/SimpleTuner.git
      cd SimpleTuner
      ```

      Create and activate a Python virtual environment:
      ```bash
      python3.11 -m venv .venv
      source .venv/bin/activate
      ```

      Upgrade pip and install Poetry:
      ```bash
      pip install -U poetry pip
      ```

      Configure Poetry to use the current virtual environment:
      ```bash
      poetry config virtualenvs.create false
      ```

      > **Tip:** If you prefer a custom virtual environment path, add the following line to your configuration (e.g., in `config/config.env`):
      > ```bash
      > export VENV_PATH=/path/to/.venv
      > ```
  - section: "2. Installing Dependencies"
    content: |
      Since you’re working on Linux, install the necessary dependencies with:
      ```bash
      poetry install
      ```

      ### GPU Considerations

      #### AMD ROCm Users
      For AMD GPUs (like MI300X), run:
      ```bash
      sudo apt install amd-smi-lib
      pushd /opt/rocm/share/amd_smi
        python3 -m pip install --upgrade pip
        python3 -m pip install .
      popd
      ```

      #### NVIDIA Users (Optional for Hopper/Blackwell Hardware)
      If you have NVIDIA Hopper (or newer) hardware, you can enable FlashAttention3 to boost inference and training performance:
      ```bash
      git clone https://github.com/Dao-AILab/flash-attention
      pushd flash-attention
        pushd hopper
          python setup.py install
        popd
      popd
      ```
      
      > **Note:** The flash-attention build is managed externally. You may need to re-run this setup when updates occur.
  - section: "3. Configuration"
    content: |
      You can configure SimpleTuner in one of two ways:

      ### Option 1: Automated Configuration
      Simply run the configuration script:
      ```bash
      python configure.py
      ```

      ### Option 2: Manual Configuration
      Copy the example config and update as needed:
      ```bash
      cp config/config.json.example config/config.json
      ```
      Then, edit `config/config.json` to match your AI-Headshot project settings.

      > **Important:** If you’re in a region with restricted access to the Hugging Face Hub, add this to your shell configuration (e.g., `~/.bashrc`):
      > ```bash
      > HF_ENDPOINT=https://hf-mirror.com
      > ```
  - section: "4. (Optional) Multi-GPU Training Setup"
    content: |
      For multi-GPU training, add the following to your `config/config.env`:
      ```env
      TRAINING_NUM_PROCESSES=1
      TRAINING_NUM_MACHINES=1
      TRAINING_DYNAMO_BACKEND='no'
      CONFIG_BACKEND='json'
      ```
      Any settings not explicitly set will revert to default values.
  - section: "5. Training Metrics Reporting"
    content: |
      By default, SimpleTuner reports metrics via Weights & Biases. To configure:
      ```bash
      wandb login
      ```
      Follow the instructions to enter your API key.  
      If you wish to disable reporting, run your training with:
      ```bash
      --report-to=none
      ```
  - section: "6. Launching the Training Session"
    content: |
      Start your training session with:
      ```bash
      ./train.sh
      ```
      Logs will be written to `debug.log`.

      > **Reminder:** If you used `configure.py`, no further configuration is needed. Otherwise, refer to the detailed tutorial for additional settings.
  - section: "7. Running Unit Tests"
    content: |
      To ensure your installation is correct, execute:
      ```bash
      poetry run python -m unittest discover tests/
      ```
  - section: "8. Advanced: Managing Multiple Configurations"
    content: |
      For scenarios where you train multiple models or use various datasets, you can manage different configurations using environment variables.

      - **Specify a Configuration Environment:**
        ```bash
        env ENV=default CONFIG_BACKEND=env bash train.sh
        ```
        - `ENV` (defaults to `default`) points to the `SimpleTuner/config/` directory.
        - For an alternate environment (e.g., `pixart`), run:
          ```bash
          env ENV=pixart bash train.sh
          ```

      - **Choose a Configuration Backend:**
        Set `CONFIG_BACKEND` to `env`, `json`, `toml`, or `cmd`. For example:
        ```bash
        env CONFIG_BACKEND=json bash train.sh
        ```

      - **Persisting Settings:**
        Add the following to `config/config.env`:
        ```env
        ENV=default
        CONFIG_BACKEND=json
        ```
  - section: "Summary"
    content: |
      This guide has walked you through setting up SimpleTuner on your Linux device for the AI-Headshot project, focusing on training the LORA of the flux model. From cloning the repository and setting up your environment, to installing dependencies, configuring the system, and launching training—the steps are designed to get you up and running efficiently.

      For additional details or troubleshooting, refer to the [official SimpleTuner documentation](https://github.com/bghira/SimpleTuner).


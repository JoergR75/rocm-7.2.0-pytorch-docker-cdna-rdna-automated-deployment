# ⚙️ ROCm 7.2.0 + OpenCL 2.x + PyTorch (Preview (Nightly)) + Transformers + Docker Setup

[![ROCm](https://img.shields.io/badge/ROCm-7.2.0-ff6b6b?logo=amd)](https://rocm.docs.amd.com/en/docs-7.2.0/about/release-notes.html)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.11.0%20%28Preview%29-ee4c2c?logo=pytorch)](https://pytorch.org/get-started/locally/)
[![Docker](https://img.shields.io/badge/Docker-29.2.0-blue?logo=docker)](https://www.docker.com/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04%20%7C%2024.04-e95420?logo=ubuntu)](https://ubuntu.com/download/server)
[![AMD Radeon AI PRO R9700](https://img.shields.io/badge/AMD-RDNA4%20Radeon(TM)%20AI%20PRO%20R9700-8B0000?logo=amd)](https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html)
[![AMD CDNA MI300 Series](https://img.shields.io/badge/AMD-CDNA%20Instint(TM)%20Architecture-8B0000?logo=amd)](https://www.amd.com/en/technologies/cdna.html)

## 📌 Overview
The script provisions a fully automated, non-interactive AMD GPU software development environment for AI and HPC software engineering on **Ubuntu 22.04** and **24.04**, centered on **ROCm 7.2.0** and **PyTorch** Preview Nightly.

At the platform layer, it installs the AMD GPU kernel driver (**amdgpu-dkms**) and the ROCm 7.2.0 runtime, including **HIP** and **OpenCL 2.x**, ensuring compatibility across **CDNA1**, **CDNA2**, **CDNA3** **CDNA4**, **RDNA3**, **RDNA4** GPUs and **Strix APUs**. The script configures **OpenCL ICD** paths, user group permissions (video, render, sudo), and kernel headers required for compiling GPU-accelerated native extensions.

For the AI framework layer, the script installs **PyTorch 2.11.0 Preview Nightly** (**ROCm 7.2 wheels**) directly from the official PyTorch ROCm nightly repository, enabling access to the latest HIP backends, kernel fusion paths, and compiler features. It complements PyTorch with Transformers, Accelerate, Diffusers, Datasets, SentencePiece, and supporting Python build tooling, allowing immediate development, testing, and profiling of modern LLM, diffusion, and data-parallel workloads.

The developer toolchain is rounded out with C/C++ build and system utilities required for low-level GPU software engineering and extension development, including **cmake**, **libstdc++ dev headers**, **git** / **git-lfs**, **libmsgpack**, and **rocm-bandwidth-test** for validating PCIe and HBM bandwidth. Runtime observability and system inspection are supported via htop, ncdu, and ROCm diagnostics (rocminfo, rocm-smi, amd-smi).

A validation script is generated to verify end-to-end GPU availability, confirming ROCm detection, PyTorch HIP enablement, GPU enumeration, and successful on-device tensor execution.

The setup is fully **non-interactive** and optimized for both **desktop** and **server** deployments. In addition it checks whether ROCm or PyTorch (installed via pip) is already present on the system.
If an existing ROCm installation is detected, it removes ROCm and related packages to ensure a clean environment. It also **detects** and **uninstalls** any PyTorch packages (including ROCm-specific builds) to prevent version conflicts before proceeding with a fresh installation.

---

## 🖥️ Supported Platforms

| **Component**      | **Supported Versions**                                |
|---------------------|------------------------------------------------------|
| **OS**            | Ubuntu 22.04.x (Jammy Jellyfish), Ubuntu 24.04.x (Noble Numbat) |
| **Kernels** tested       | 5.15.0-160 (22.04.5) • 6.8.0-94 (24.04.3)                       |
| **GPUs**          | AMD **CDNA1** • **CDNA2** • **CDNA3** • **CDNA4** • **RDNA3** • **RDNA4**              |
| **APUs**        | AMD **Strix** • **Strix Halo**                                       |
| **ROCm**          | 7.2.0                                                |
| **PyTorch**       | torch 2.11.0.dev20260129+rocm7.1, torchvision 0.25.0.dev20260201+rocm7.1       |       |

**⚠️ Note**: **Ubuntu 20.04.x (Focal Fossa)** is **not supported**. The last compatible ROCm version for 20.04 is **6.4.0**.

---

## ⚡ Features
- Automated **ROCm GPU drivers + HIP + OpenCL SDK** installation
- **PyTorch ROCm Preview Nightly** with GPU acceleration
- Preinstalled **Transformers**, **Accelerate**, **Diffusers**, and **Datasets**
- Integrated **Docker environment** with ROCm GPU passthrough
- **vLLM Docker images** for **RDNA4** & **CDNA**
- Optimized for **AI workloads**, **LLM inference**, and **model fine-tuning**

---

## 🚀 Installation

### 1️⃣ **System preperation**
Install **Ubuntu 22.04.5 LTS** or **Ubuntu 24.04.3 LTS** (Server or Desktop version).

**Recommendations:**
- Use a fresh Ubuntu installation if possible
- Assign the full storage capacity during installation
- Install **OpenSSH** for remote SSH management
- The script automatically checks the system for installed versions of ROCm, PyTorch, and Docker, and removes them if found
  - On a fresh Ubuntu installation, the script automatically skips the deinstallation routine, as illustrated below
    <img width="697" height="188" alt="{DB29AEE6-CF12-4D0D-BA9F-611E73DBE146}" src="https://github.com/user-attachments/assets/48516cb6-e7bd-4c7e-94bb-f3ec9a95b243" />
  - If an existing version is detected, it will be deleted, regardless of whether it is the same or an older release.
    <img width="724" height="312" alt="{ABC66E35-246B-49CD-B988-5C19DA511ACB}" src="https://github.com/user-attachments/assets/c0a87932-fb0e-4adb-8bf9-cbe80d13f528" />
- SBIOS settings:
  - When using Linux, you should disable Secure Boot
  - On WRX80 and WRX90 motherboard solutions, make sure SR-IOV is enabled — there are known issues with Ubuntu Linux detecting the network otherwise

### 2️⃣ **Download the Script from the Repository**
```bash
wget https://raw.githubusercontent.com/JoergR75/rocm-7.2.0-pytorch-docker-cdna-rdna-automated-deployment/refs/heads/main/script_module_ROCm_720_Ubuntu_22.04-24.04_pytorch_server.sh
```

<img width="967" height="275" alt="{88EE1CD5-AD5C-43E7-BF71-84CAB636FC7B}" src="https://github.com/user-attachments/assets/2aee5ebd-1b4b-4066-b030-d5e58d06ddbe" />

### 3️⃣ **Run the Installer**
```bash
bash script_module_ROCm_720_Ubuntu_22.04-24.04_pytorch_server.sh
```
**⚠️ Note**: Entering the user password may be required.

<img width="956" height="327" alt="{036AB9F1-945C-461E-B497-C8F977804405}" src="https://github.com/user-attachments/assets/df538538-32d7-40c3-a67e-cc065c5b8bc0" />

The installation takes ~15 minutes depending on internet speed and hardware performance.

### 4️⃣ **Reboot the System**
After the successful installation, press "y" to reboot the system and activate all installed components.

<img width="962" height="542" alt="{C72A982C-F406-4CFD-AF9E-78706250C21B}" src="https://github.com/user-attachments/assets/dc00f682-b27d-4fc8-8d24-973aa8b9f0c9" />

## 🧪 Testing ROCm + PyTorch

After rebooting, verify your setup:

This script creates a simple diagnostic python file (test.py) to verify that PyTorch with ROCm support is correctly installed and working.

What it does:

- Shows the CPU and installed memory
- Prints the PyTorch version and ROCm version.
- Checks if ROCm is available and how many GPUs are detected.
- Displays the name of the first GPU (if available).
- Creates two random 3×3 tensors directly on the GPU (if available).
- Performs a simple tensor addition operation on the GPU.
- Prints confirmation that the operation was successful and shows the result.

Example usage:
```bash
python3 test.py
```
Expected Output Example:

<img width="901" height="290" alt="{BA60D6AC-8DEA-45C2-BB42-BB2F42A9F346}" src="https://github.com/user-attachments/assets/f2a67558-6cdb-40e2-a3b4-80789344262a" />

More details about the ROCm driver version can be reviewed:
```bash
apt show rocm-libs -a
```

<img width="964" height="472" alt="{851E66D0-2E64-47BF-9D57-DE9298D96EDF}" src="https://github.com/user-attachments/assets/72c9acfb-81b8-4861-a86a-22e76673d06e" />

## ⏻ Setting the right Power Management with `rocm-smi`

ROCm provides basic power and performance management controls via `rocm-smi`.  
For RDNA and CDNA GPUs, predefined performance profiles can be used to balance **power efficiency** and **maximum performance**:

- **Compute** – Optimized for latency-sensitive and “bursty” workloads. It avoids electrical or thermal overshoots that can occur when multiple WGPs are activated simultaneously.
- **3D Full Screen** – Designed for gaming with “inverted bathtub” activity profiles.
- **VR** – Ensures minimum performance requirements are met without consuming more power than necessary.
- **Video** – Historically tuned to minimize power for video playback, but recent profiles optimize **VCN performance** for encoding and transcoding workloads.

Use the following command to verify the active power profile:

```bash
rocm-smi --showprofile
```
The star (*) marks the current profile which is set to **BOOTUP DEFAULT**

<img width="955" height="418" alt="{47D793DA-4B98-4279-A98C-02D5B0E19603}" src="https://github.com/user-attachments/assets/90224340-630a-4555-b448-e84ae54eb91a" />

Set the GPU to the high-performance / compute-optimized power profile.
This profile prioritizes sustained clocks and higher power limits, making it well suited for AI inference, training, and other compute-intensive workloads.
It may increase power consumption but helps ensure consistent performance under load.

```bash
rocm-smi --setprofile 4
```

<img width="939" height="237" alt="{66B98679-C70F-44BC-9C08-CBAFAD62B7C0}" src="https://github.com/user-attachments/assets/049e36aa-2460-4d29-8032-3cc9183eaafc" />

## 📶 ROCm Bandwidth Test

**AMD’s ROCm Bandwidth Test utility** with the **`tb p2p` (Peer-to-peer device memory bandwidth test)** flag runs a complete set of bandwidth diagnostics.

### What it does

`rocm-bandwidth-test` is a diagnostic tool included in ROCm that measures **memory bandwidth performance** between:

- Host (CPU) ↔ GPU(s)  
- GPU ↔ GPU (if multiple GPUs are installed)  
- GPU internal memory  

### `tb p2p` option

Using the `--run tb p2p` flag runs **Peer-to-peer device memory bandwidth test**, including:

- **Host-to-Device (H2D)** bandwidth  
- **Device-to-Host (D2H)** bandwidth  
- **Device-to-Device (D2D)** bandwidth (for multi-GPU)  
- **Bidirectional / concurrent** bandwidth tests  

Run the P2P test
```bash
cd /opt/rocm/bin && ./rocm_bandwidth_test plugin --run tb p2p
```

### Output

The tool prints results in a **matrix format** showing bandwidth (GB/s) between every device pair.

<img width="983" height="1179" alt="{6EAC522F-550D-4881-9C78-11B3A90A555D}" src="https://github.com/user-attachments/assets/039f0f87-79b8-4dd0-856b-d959025b27a4" />

More details about the setup can be verified by
```bash
cd /opt/rocm/bin && ./rocm_bandwidth_test plugin --run tb
```

<img width="861" height="275" alt="{4103D9C7-2ECE-42CF-A231-DC1D7004C7BF}" src="https://github.com/user-attachments/assets/e0a1efaf-9c5c-4c6c-b2d9-8ff14cf1b623" />

⚠️ **Caution:**  
Make sure **"Re-Size BAR"** is enabled in the **SBIOS**.  
If it is disabled, **P2P** will be deactivated, as shown below:

<img width="977" height="777" alt="{FD9B95A3-BEFA-4857-8BBB-8D06A90108F2}" src="https://github.com/user-attachments/assets/cc148322-45b3-4164-b215-521276749f9d" />

More details about the setup can be verified by
```bash
cd /opt/rocm/bin && ./rocm_bandwidth_test plugin --run tb
```

<img width="904" height="274" alt="{3F58A790-E952-4BD9-9F0A-B99FD8F0B081}" src="https://github.com/user-attachments/assets/28b1808a-8216-4d7c-b1ea-db599f140056" />

### ⚙️ How to Enable **Re-Size BAR** in SBIOS (example ASRock WRX90 evo)

1. Enter **SBIOS**

<img width="1007" height="760" alt="{F9649127-0F1F-4E14-8008-1F3782FBBDEF}" src="https://github.com/user-attachments/assets/9685c1a4-ecab-4fea-8e91-dd21b9869c7e" />

3. Navigate to **Advanced**

<img width="1018" height="761" alt="{135D3B4C-0732-4652-A3C0-1224D275A515}" src="https://github.com/user-attachments/assets/b1cdc3ce-b526-4cdc-b44f-71d1119cf6d7" />

5. Go to **PCI Subsystem Settings** and change **Re-Size BAR Support** to **Enable** 

<img width="1016" height="761" alt="{3C54C3DA-8B82-483C-AEA5-D0A511508780}" src="https://github.com/user-attachments/assets/60536e2b-e59f-4486-a1fc-ab3ff33a3cd8" />

## 🐋 Docker Integration

The script sets up a Docker environment with GPU passthrough support via ROCm.

Check Docker installation and version
```bash
docker -v
```

<img width="935" height="58" alt="{5C81E868-4389-4580-988D-A13C34F1963B}" src="https://github.com/user-attachments/assets/2119225b-044c-4e4d-967f-2c6dd554715d" />

### 🤖 vLLM Docker Images

To use vLLM optimized for RDNA4 and CDNA:

Use the container image you need.

**RDNA4** architecture running on Ubuntu 24.04
```bash
docker pull rocm/vllm-dev:rocm7.2_navi_ubuntu24.04_py3.12_pytorch_2.9_vllm_0.14.0rc0
```

<img width="960" height="690" alt="{090CA25D-C862-437F-A61B-1C4C235FE0EB}" src="https://github.com/user-attachments/assets/e03ee8d6-8436-4b51-909d-52d504b655bf" />

Further vLLM Docker versions for RDNA4 can be verified on Docker Hub:  
https://hub.docker.com/r/rocm/vllm-dev/tags?name=navi

or for **CDNA** architecture
```bash
sudo docker pull rocm/vllm:latest
```

Run vLLM with all available AMD GPU access (example for RDNA4 on Ubuntu 24.04)
```bash
sudo docker run -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --security-opt seccomp=unconfined \
    --group-add video \
    rocm/vllm-dev:rocm7.2_navi_ubuntu24.04_py3.12_pytorch_2.9_vllm_0.14.0rc0
```

<img width="954" height="149" alt="{74DEF1F8-EC94-4015-8FF1-8B24B6554763}" src="https://github.com/user-attachments/assets/6e67ae9e-6874-4b30-9d31-22ba4d740c47" />

With `rocm-smi`, you can verify all available GPUs (in this case, 2× Radeon AI PRO R9700 GPUs).

<img width="960" height="412" alt="{5BA15566-340C-4D66-8F07-6E85BA5A09C1}" src="https://github.com/user-attachments/assets/562ac5eb-bb8b-429c-80e4-7d5c7aee044b" />

or `amd-smi`

<img width="946" height="403" alt="{35EFA5E7-C3E2-4EF0-876F-AFDCD5EF68EF}" src="https://github.com/user-attachments/assets/efda1960-d4f6-480f-bb73-82ec663996c3" />

If you need to add a specific GPU, you can use the **passthrough** option.  
First, verify the available GPUs in the `/dev/dri` directory.
```bash
cd /dev/dri && ls
```

<img width="871" height="77" alt="{5CE24323-6294-4E65-9B0F-553A87AED057}" src="https://github.com/user-attachments/assets/30aff011-0a88-442c-a8a4-3e2d7633ba3e" />

Let's choose **GPU2**, also referred to as **"card2"** or **"renderD129"**.
```bash
sudo docker run -it \
    --device=/dev/kfd \
    --device=/dev/dri/card2 \
    --device=/dev/dri/renderD129 \
    --security-opt seccomp=unconfined \
    --group-add video \
    rocm/vllm-dev:rocm7.1.1_navi_ubuntu24.04_py3.12_pytorch_2.8_vllm_0.10.2rc1
```
GPU2 has been added to the container

<img width="1036" height="383" alt="{DDB60941-260E-4E11-B6C8-A00772A25C5E}" src="https://github.com/user-attachments/assets/04feef9e-7191-4658-b9f4-9a72323d4d8c" />

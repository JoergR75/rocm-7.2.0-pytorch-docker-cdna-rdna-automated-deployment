## 🚀 Installation

### 1️⃣ **System preperation**
Install **Ubuntu 22.04.5 LTS** or **Ubuntu 24.04.3 LTS** (Server or Desktop version).
Install the the automates ROCm 
Download and Install the latest vLLM container (RDNA4 build for Ubuntu 24.04.x (~15.97GB))
```bash
sudo docker pull rocm/vllm-dev:rocm7.2_navi_ubuntu24.04_py3.12_pytorch_2.9_vllm_0.14.0rc0
```
start the container
```bash
sudo docker run -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --security-opt seccomp=unconfined \
    --group-add video \
    rocm/vllm-dev:rocm7.2_navi_ubuntu24.04_py3.12_pytorch_2.9_vllm_0.14.0rc0
```

### 2️⃣ **Download the python Benchmark-Script from the Repository**
```bash
wget https://raw.githubusercontent.com/JoergR75/rocm-7.2.0-pytorch-docker-cdna-rdna-automated-deployment/refs/heads/main/vLLM/benchmark_vllm.py
```

<img width="966" height="294" alt="{A2A512A8-09CF-4579-9AA2-169B8C66C3DD}" src="https://github.com/user-attachments/assets/469379ea-0a1e-4caa-89d4-23004a544c3f" />

### 3️⃣ **Run the Benchmark**
Without a required hugging face token
```python
python3 benchmark_vllm.py
```
With required hf token
```python
python3 benchmark_vllm.py \
  --hf-token hf_xxxx
```
**⚠️ Note**: verify if a hf token to access the model will be required. Some models aslo require to accept license notice.

<img width="894" height="215" alt="{2E07A558-C14D-49E9-8B34-6BAC7FBB26B8}" src="https://github.com/user-attachments/assets/4d78ef93-22f3-4af8-a670-fdfaaec6bf01" />

An access token can be created in your user profile under "Access Token". Make sure the following settings are configured:
- Read access to contents of all repos under your personal namespace
- View access requests for all gated repos under your personal namespace
- Read access to contents of all public gated repos you can access

<img width="819" height="531" alt="{22847529-E5E4-42DA-A3BA-2363ECE3E434}" src="https://github.com/user-attachments/assets/26f3cb51-f23d-465f-a834-69f374b7ef39" />


**Bielik 1.5 v3** (3.2 GB - access token required)
<img width="967" height="558" alt="{8F27905B-30A8-4ED4-BBEB-C4019B482010}" src="https://github.com/user-attachments/assets/527b87c5-d5d0-4c28-9b58-5b3b9761b2e8" />

**Bielik 4.5B v3** (9.1 GB - access token required)


**Bielik 11B v3** (20.9 GB - access token required)


Bielik 1.5B v3 (3.2 GB)
<img width="1215" height="594" alt="{510BFB37-9DF7-4884-A238-7C37C6409695}" src="https://github.com/user-attachments/assets/fb5bcf41-7569-4f9f-9eb2-253f2ebfe4f2" />
Bielik 4.5B v3 (9.1 GB)
<img width="1216" height="597" alt="{CCF149C8-015D-4F55-B924-7E7B3551DE17}" src="https://github.com/user-attachments/assets/ff52eb61-c0fe-4706-99d0-b01133e401b5" />
Bielik 11B v3 (20.9 GB)
<img width="1216" height="698" alt="{DA311C88-6888-49AC-868C-AB2834F89D07}" src="https://github.com/user-attachments/assets/f5872752-b8ea-4990-9c0e-53c097debb72" />


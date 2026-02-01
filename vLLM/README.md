## 🚀 Installation

### 1️⃣ **System preperation**
Install **Ubuntu 22.04.5 LTS** or **Ubuntu 24.04.3 LTS** (Server or Desktop version).
Install the the automates ROCm 
Download and Install the latest vLLM container (RDNA4 build for Ubuntu 24.04.x (~13.6GB))
```bash
sudo docker pull rocm/vllm-dev:rocm7.1.1_navi_ubuntu24.04_py3.12_pytorch_2.8_vllm_0.10.2rc1
```
start the container
```bash
sudo docker run -it \
    --device=/dev/kfd \
    --device=/dev/dri \
    --security-opt seccomp=unconfined \
    --group-add video \
    rocm/vllm-dev:rocm7.1.1_navi_ubuntu24.04_py3.12_pytorch_2.8_vllm_0.10.2rc1
```

### 2️⃣ **Download the python Benchmark-Script from the Repository**
```bash
wget https://raw.githubusercontent.com/JoergR75/rocm-7.1.1-pytorch-2.11.0-docker-cdna3-rdna4-automated-deployment/refs/heads/main/vLLM/vLLMbench.py
```
<img width="1216" height="276" alt="{DA9A9447-CA91-4CE5-8095-B545AA24E564}" src="https://github.com/user-attachments/assets/9f960a0a-4415-428f-b308-9534df12e867" />

Install tabulate
```bash
pip3 install tabulate
```
<img width="1012" height="132" alt="{DBE97894-2F06-4929-AC9F-1A04529BDFFF}" src="https://github.com/user-attachments/assets/209cc851-da38-4413-a512-b7d8edebaa03" />

### 3️⃣ **Run the Benchmark**
Without a required hugging face token
```python
python3 vLLMbench.py
```
With required hf token
```python
python3 vLLMbench.py \
  --hf-token hf_xxxx
```
**⚠️ Note**: verify if a hf token to access the model will be required. Some models aslo require to accept license notice.
<img width="894" height="215" alt="{2E07A558-C14D-49E9-8B34-6BAC7FBB26B8}" src="https://github.com/user-attachments/assets/4d78ef93-22f3-4af8-a670-fdfaaec6bf01" />

Bielik 1.5B v3 (3.2 GB)
<img width="1215" height="594" alt="{510BFB37-9DF7-4884-A238-7C37C6409695}" src="https://github.com/user-attachments/assets/fb5bcf41-7569-4f9f-9eb2-253f2ebfe4f2" />
Bielik 4.5B v3 (9.1 GB)
<img width="1216" height="597" alt="{CCF149C8-015D-4F55-B924-7E7B3551DE17}" src="https://github.com/user-attachments/assets/ff52eb61-c0fe-4706-99d0-b01133e401b5" />
Bielik 11B v3 (20.9 GB)
<img width="1216" height="698" alt="{DA311C88-6888-49AC-868C-AB2834F89D07}" src="https://github.com/user-attachments/assets/f5872752-b8ea-4990-9c0e-53c097debb72" />


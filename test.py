#!/usr/bin/env python3

import torch
import subprocess
import re
import os

def get_cpu_model():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()

print("\nInstalled CPU:", get_cpu_model())

def get_total_memory_gb():
    with open("/proc/meminfo") as f:
        for line in f:
            if line.startswith("MemTotal:"):
                # Extract the numeric value in kB
                mem_kb = int(re.findall(r'\d+', line)[0])
                # Convert to GB (1 GB = 1024^2 kB)
                mem_gb = mem_kb / (1024 ** 2)
                return f"Total System-Memory: {mem_gb:.0f} GB"

if __name__ == "__main__":
    print(get_total_memory_gb())

print("PyTorch version:", torch.__version__)
print("ROCm version:", subprocess.getoutput("/opt/rocm/bin/hipconfig --version"))
print("Is ROCm available:", torch.version.hip is not None)
print("Number of GPUs:", torch.cuda.device_count())
print("\nGPU Name:", torch.cuda.get_device_name(0) if torch.cuda.device_count() > 0 else "No GPU detected")

# Create two tensors and add them on the GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

a = torch.rand(3, 3, device=device)
b = torch.rand(3, 3, device=device)
c = a + b

print("\nTensor operation successful on:", device)
print(c)

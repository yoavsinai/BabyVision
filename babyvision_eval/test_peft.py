import torch
from transformers import AutoModelForImageTextToText
from peft import LoraConfig, get_peft_model

model_id = "google/gemma-4-E4B-it"
print(f"Loading {model_id} on GPU...")
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

target_regex = ".*(language_model.*self_attn\\.(q_proj|k_proj|v_proj|o_proj)|language_model.*mlp\\.(gate_proj|up_proj|down_proj)|vision_tower.*self_attn\\.(q_proj|k_proj|v_proj|o_proj)\\.linear|vision_tower.*mlp\\.(gate_proj|up_proj|down_proj)\\.linear)$"

peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=target_regex,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

peft_model = get_peft_model(model, peft_config)
print("\n--- Trainable Parameters ---")
vision_count = 0
language_count = 0
audio_count = 0

for name, param in peft_model.named_parameters():
    if param.requires_grad:
        if "vision_tower" in name:
            vision_count += 1
        elif "language_model" in name:
            language_count += 1
        elif "audio_tower" in name:
            audio_count += 1
        else:
            print(f"Other: {name}")

print(f"Total trainable vision tower params: {vision_count}")
print(f"Total trainable language model params: {language_count}")
print(f"Total trainable audio tower params: {audio_count}")

"""Thin wrapper over Forge's Automatic1111-compatible REST API.

Forge must be running locally with the API enabled (its default install
already serves this API on port 7860 — no extra flags needed on recent
Forge builds; see README.md if yours needs `--api`).
"""
import base64

import requests


class ForgeClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def health_check(self):
        """Raises if Forge isn't reachable. Returns the list of loaded checkpoints."""
        r = requests.get(f"{self.base_url}/sdapi/v1/sd-models", timeout=5)
        r.raise_for_status()
        return r.json()

    def set_checkpoint(self, checkpoint_name):
        if not checkpoint_name or checkpoint_name.startswith("REPLACE_WITH"):
            raise ValueError(
                "No checkpoint configured — edit tools/image-gen/config.yaml "
                "and set the real SDXL checkpoint filename Forge has loaded."
            )
        r = requests.post(
            f"{self.base_url}/sdapi/v1/options",
            json={"sd_model_checkpoint": checkpoint_name},
            timeout=60,
        )
        r.raise_for_status()

    def txt2img(
        self,
        prompt,
        negative_prompt="",
        width=1024,
        height=1024,
        steps=30,
        cfg_scale=7,
        sampler_name="DPM++ 2M Karras",
        seed=-1,
    ):
        """Returns a list of raw PNG bytes, one per generated image (batch size 1 by default)."""
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "sampler_name": sampler_name,
            "seed": seed,
        }
        r = requests.post(f"{self.base_url}/sdapi/v1/txt2img", json=payload, timeout=300)
        r.raise_for_status()
        data = r.json()
        return [base64.b64decode(img) for img in data["images"]]

    def upscale(self, image_bytes, upscaler_1="4x-UltraSharp", target_width=1400, target_height=1050):
        """Runs an image through Forge's extras upscaler. Returns raw PNG bytes."""
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        payload = {
            "image": encoded,
            "upscaler_1": upscaler_1,
            "resize_mode": 1,
            "upscaling_resize_w": target_width,
            "upscaling_resize_h": target_height,
        }
        r = requests.post(f"{self.base_url}/sdapi/v1/extra-single-image", json=payload, timeout=300)
        r.raise_for_status()
        return base64.b64decode(r.json()["image"])


def build_lora_tag(lora_config):
    """lora_config is the {name, weight, ...} dict from config.yaml, or None."""
    if not lora_config:
        return ""
    name = lora_config["name"]
    if name.startswith("REPLACE_WITH"):
        raise ValueError(
            "No LoRA configured — edit tools/image-gen/config.yaml and set "
            "the real LoRA filename you downloaded into Forge's models/Lora folder."
        )
    weight = lora_config.get("weight", 0.8)
    return f" <lora:{name}:{weight}>"

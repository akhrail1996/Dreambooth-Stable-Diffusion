from huggingface_hub import hf_hub_download
downloaded_model_path = hf_hub_download(repo_id="panopstor/EveryDream", filename="sd_v1-5_vae.ckpt")

print(downloaded_model_path)

# Move the sd_v1-5_vae.ckpt to the root of this directory as "model.ckpt"
import subprocess

output = subprocess.run(["readlink", "-f", downloaded_model_path], capture_output=True, text=True)
actual_locations_of_model_blob = output.stdout.strip().split("\n")
out = subprocess.run(["mv", actual_locations_of_model_blob[-1], "model.ckpt"])
print(out)

print("✅ model.ckpt successfully downloaded")

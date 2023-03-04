from huggingface_hub import hf_hub_download
downloaded_model_path = hf_hub_download(repo_id="panopstor/EveryDream", filename="sd_v1-5_vae.ckpt")

print(downloaded_model_path)

# Move the sd_v1-5_vae.ckpt to the root of this directory as "model.ckpt"
import subprocess

actual_locations_of_model_blob = subprocess.run(!readlink -f {downloaded_model_path}, shell=True, stdout=subprocess.PIPE).stdout
print(actual_locations_of_model_blob)

out = subprocess.run("mv " + actual_locations_of_model_blob[-1] + " model.ckpt", shell=True, stdout=subprocess.PIPE)
print(out)

print("✅ model.ckpt successfully downloaded")

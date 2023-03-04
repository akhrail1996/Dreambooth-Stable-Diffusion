from huggingface_hub import hf_hub_download
downloaded_model_path = hf_hub_download(repo_id="panopstor/EveryDream", filename="sd_v1-5_vae.ckpt")

# Move the sd_v1-5_vae.ckpt to the root of this directory as "model.ckpt"
actual_locations_of_model_blob = !readlink -f {downloaded_model_path}
!mv {actual_locations_of_model_blob[-1]} model.ckpt

print("✅ model.ckpt successfully downloaded")

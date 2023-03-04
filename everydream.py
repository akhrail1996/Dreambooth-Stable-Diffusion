from huggingface_hub import hf_hub_download
downloaded_model_path = hf_hub_download(repo_id="panopstor/EveryDream", filename="sd_v1-5_vae.ckpt")

print(downloaded_model_path)

# Move the sd_v1-5_vae.ckpt to the root of this directory as "model.ckpt"
!mv downloaded_model_path model.ckpt

print("✅ model.ckpt successfully downloaded")

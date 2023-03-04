import subprocess
import re

training_images_output = subprocess.run(["find", "training_images/*"], capture_output=True, text=True)
training_images = training_images_output.stdout.strip().split("\n")

date_string_output = subprocess.run(["date", "+%Y-%m-%dT%H-%M-%S"], capture_output=True, text=True)
date_string = date_string_output.stdout.strip().split("\n")

directory_paths_output = subprocess.run(["ls", "-d", "logs/*"], capture_output=True, text=True)
directory_paths = directory_paths_output.stdout.strip().split("\n")

last_checkpoint_file = directory_paths[-1] + "/checkpoints/last.ckpt"
file_name = date_string[-1] + ".ckpt"

file_name = file_name.replace(" ", "_")

subprocess.run(["mkdir", "-p", "trained_models"])
subprocess.run(["mv", last_checkpoint_file, "trained_models/model.ckpt"])

print("Download your trained model from trained_models/" + file_name + " and use in your favorite Stable Diffusion repo!")

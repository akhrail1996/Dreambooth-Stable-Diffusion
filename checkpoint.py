import re

training_images = !find training_images/*
date_string = !date +"%Y-%m-%dT%H-%M-%S"

directory_paths = !ls -d logs/*
last_checkpoint_file = directory_paths[-1] + "/checkpoints/last.ckpt"
file_name = date_string[-1] + "_" + \
            str(len(training_images)) + "_training_images_" + \
            str(max_training_steps) + "_max_training_steps_" + \
            token + "_token_" + \
            class_word + "_class_word.ckpt"

file_name = file_name.replace(" ", "_")

!mkdir -p trained_models
!mv "{last_checkpoint_file}" "trained_models/model.ckpt"

print("Download your trained model from trained_models/" + file_name + " and use in your favorite Stable Diffusion repo!")

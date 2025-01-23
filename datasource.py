import kagglehub

# Download latest version
path = kagglehub.dataset_download("rhuebner/human-resources-data-set")

print("Path to dataset files:", path)
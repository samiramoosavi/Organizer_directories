from pathlib import Path
dir_path = "/opt/test_projec"
dir_path = Path (dir_path)

for item_path in dir_path.iterdir():
    print(item_path.is_file())


print("commnet")



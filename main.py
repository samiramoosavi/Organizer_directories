from pathlib import Path
import sys
import shutil

dir_path = Path(sys.argv[1])

for item_path in dir_path.iterdir():

    if item_path.suffix.lower() in ['.jpg', '.png']:
        target_path = Path(item_path.parent, 'image')
        shutil.move(str(item_path), str(target_path))

print("hello world!")
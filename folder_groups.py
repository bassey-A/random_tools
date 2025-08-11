import os
import shutil

source = "C:\\Users\\basee\\Downloads"
destinations = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".epub", ".txt", ".docx", ".xml", ".xlsx"],
    "Executables": [".zip", ".exe"]
}
for file in os.listdir(source):
    file_path = os.path.join(source, file)
    if os.path.isfile(file_path):
        for folder, extensions in destinations.items():
            if any(file.endswith(ext) for ext in extensions):
                os.makedirs(os.path.join(source, folder), exist_ok=True)
                shutil.move(file_path, os.path.join(source, folder))
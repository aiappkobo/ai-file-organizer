import os
import shutil

# 整理したいフォルダ
target_folder = "整理したいフォルダのパス"

# 拡張子ごとのフォルダ分け
file_types = {
    "画像": [".jpg", ".png", ".jpeg"],
    "動画": [".mp4", ".mov"],
    "ドキュメント": [".pdf", ".docx", ".txt"],
    "その他": []
}

for filename in os.listdir(target_folder):
    file_path = os.path.join(target_folder, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder_name, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(target_folder, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break

        if not moved:
            dest_folder = os.path.join(target_folder, "その他")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))

print("整理完了！")

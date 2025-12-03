import shutil
import os

folder_to_delete = r"E:\MH-Weed16\UAV_split"

# 检查文件夹是否存在
if os.path.exists(folder_to_delete):
    shutil.rmtree(folder_to_delete)
    print(f"{folder_to_delete} 已经被删除。")
else:
    print(f"{folder_to_delete} 不存在，无需删除。")

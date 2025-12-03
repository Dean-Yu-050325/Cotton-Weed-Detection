import os
import shutil
import random

# ==== UAV 文件夹位置（你现在就是这个路径） ====
uav_dir = r"E:\UAV"
# 输出目录（自动生成）
output_dir = r"E:\UAV_split"
# 分割比例 7:3
split_ratio = 0.7
# ============================================

# 创建输出目录
os.makedirs(os.path.join(output_dir, "train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "test"), exist_ok=True)

# 获取所有图片文件
image_files = [f for f in os.listdir(uav_dir)
               if f.lower().endswith((".jpg", ".jpeg", ".png"))]

random.shuffle(image_files)

train_count = int(len(image_files) * split_ratio)
train_list = image_files[:train_count]
test_list = image_files[train_count:]

def copy_files(files, target_folder):
    for name in files:
        src = os.path.join(uav_dir, name)
        dst = os.path.join(output_dir, target_folder, name)
        shutil.copy(src, dst)

# 拷贝文件
copy_files(train_list, "train")
copy_files(test_list, "test")

print("Done!")
print("Total:", len(image_files))
print("Train:", len(train_list), "Test:", len(test_list))

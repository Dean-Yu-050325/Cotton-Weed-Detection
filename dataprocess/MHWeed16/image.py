import os
import random
import shutil

# 原始图片路径
image_dir = r"E:\images"

# 输出路径
output_dir = r"E:\images_split"
train_dir = os.path.join(output_dir, "train")
test_dir = os.path.join(output_dir, "test")

# 创建目录
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 获取所有图片文件
all_images = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# 打乱顺序
random.shuffle(all_images)

# 划分比例
split_ratio = 0.7
split_index = int(len(all_images) * split_ratio)

train_images = all_images[:split_index]
test_images = all_images[split_index:]

# 拷贝文件
for f in train_images:
    shutil.copy(os.path.join(image_dir, f), train_dir)

for f in test_images:
    shutil.copy(os.path.join(image_dir, f), test_dir)

print(f"总图片: {len(all_images)}")
print(f"训练集: {len(train_images)}，测试集: {len(test_images)}")
print(f"划分完成，train/test 文件夹在 {output_dir}")

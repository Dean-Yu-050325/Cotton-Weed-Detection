import os
import random
import shutil

def split_dataset_json(root_dir, output_dir, train_ratio=0.7):
    img_dir = os.path.join(root_dir, "images")
    ann_dir = os.path.join(root_dir, "annotations")

    # 输出结构
    train_img_dir = os.path.join(output_dir, "train/images")
    train_ann_dir = os.path.join(output_dir, "train/annotations")
    test_img_dir = os.path.join(output_dir, "test/images")
    test_ann_dir = os.path.join(output_dir, "test/annotations")

    for d in [train_img_dir, train_ann_dir, test_img_dir, test_ann_dir]:
        os.makedirs(d, exist_ok=True)

    # 获取所有图片
    images = [f for f in os.listdir(img_dir)
              if f.lower().endswith((".jpg", ".png", ".jpeg"))]

    random.shuffle(images)

    split_point = int(len(images) * train_ratio)
    train_imgs = images[:split_point]
    test_imgs = images[split_point:]

    # 处理训练集
    for img in train_imgs:
        base = os.path.splitext(img)[0]
        ann = base + ".json"

        shutil.copy(os.path.join(img_dir, img), os.path.join(train_img_dir, img))

        ann_path = os.path.join(ann_dir, ann)
        if os.path.exists(ann_path):
            shutil.copy(ann_path, os.path.join(train_ann_dir, ann))

    # 处理测试集
    for img in test_imgs:
        base = os.path.splitext(img)[0]
        ann = base + ".json"

        shutil.copy(os.path.join(img_dir, img), os.path.join(test_img_dir, img))

        ann_path = os.path.join(ann_dir, ann)
        if os.path.exists(ann_path):
            shutil.copy(ann_path, os.path.join(test_ann_dir, ann))

    print("Done!")
    print(f"Total images: {len(images)}")
    print(f"Train: {len(train_imgs)}, Test: {len(test_imgs)}")


# ----------- 在这里设置你的路径（桌面路径） -----------
split_dataset_json(
    r"C:\Users\shish\Desktop\cottonweed",
    r"C:\Users\shish\Desktop\cottonweed_split",
    train_ratio=0.7
)

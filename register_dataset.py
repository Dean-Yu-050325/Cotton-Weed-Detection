#!/usr/bin/env python3
"""
快速注册数据集到3LC Tables
运行此脚本后，会输出Table URLs，复制到train.py中即可
"""

import tlc
from pathlib import Path

print("=" * 70)
print("注册数据集到3LC Tables")
print("=" * 70)

# 配置
PROJECT_NAME = "kaggle_cotton_weed_detection"
DATASET_NAME = "cotton_weed_det3"
DATASET_YAML = Path("dataset.yaml")

# 检查文件是否存在
if not DATASET_YAML.exists():
    print(f"❌ 错误: 找不到 {DATASET_YAML}")
    print(f"   当前目录: {Path.cwd()}")
    exit(1)

print(f"\n✅ 找到数据集配置: {DATASET_YAML}")
print(f"   项目名称: {PROJECT_NAME}")
print(f"   数据集名称: {DATASET_NAME}")

# 检查是否已存在表
try:
    existing_train = tlc.Table.from_names(
        project_name=PROJECT_NAME,
        dataset_name=DATASET_NAME,
        table_name=f"{DATASET_NAME}-train1",
    )
    existing_val = tlc.Table.from_names(
        project_name=PROJECT_NAME,
        dataset_name=DATASET_NAME,
        table_name=f"{DATASET_NAME}-val1",
    )
    
    print("\n⚠️  表已存在，使用现有表：")
    print(f"   训练表: {len(existing_train)} 样本")
    print(f"   验证表: {len(existing_val)} 样本")
    
    train_table = existing_train
    val_table = existing_val
    
except Exception:
    # 创建新表
    print("\n📝 创建新的3LC Tables...")
    
    print("\n   创建训练表...")
    train_table = tlc.Table.from_yolo(
        dataset_yaml_file=str(DATASET_YAML),
        split="train",
        task="detect",
        dataset_name=DATASET_NAME,
        project_name=PROJECT_NAME,
        table_name=f"{DATASET_NAME}-train1",
    )
    
    print("   创建验证表...")
    val_table = tlc.Table.from_yolo(
        dataset_yaml_file=str(DATASET_YAML),
        split="val",
        task="detect",
        dataset_name=DATASET_NAME,
        project_name=PROJECT_NAME,
        table_name=f"{DATASET_NAME}-val1",
    )
    
    print("   ✅ 表创建完成！")

# 显示结果
print("\n" + "=" * 70)
print("✅ 数据集注册完成！")
print("=" * 70)

print(f"\n📊 统计信息:")
print(f"   训练表: {len(train_table)} 样本")
print(f"   验证表: {len(val_table)} 样本")

print("\n📋 请复制以下URL到 train.py 文件中：")
print("\n" + "-" * 70)
print("TRAIN_TABLE_URL = \"" + str(train_table.url) + "\"")
print("VAL_TABLE_URL = \"" + str(val_table.url) + "\"")
print("-" * 70)

print("\n💡 下一步:")
print("   1. 复制上面的两个URL")
print("   2. 打开 train.py 文件")
print("   3. 替换第30-31行的URL")
print("   4. 运行: python train.py")


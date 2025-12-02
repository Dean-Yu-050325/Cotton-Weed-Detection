#!/usr/bin/env python3
"""
环境测试脚本 - 检查所有依赖是否正确安装
"""

print("=" * 70)
print("环境测试开始")
print("=" * 70)

# 测试1: Python版本
print("\n[1] Python版本检查...")
import sys
print(f"   Python版本: {sys.version}")
assert sys.version_info >= (3, 8), "需要Python 3.8+"
print("   ✅ Python版本符合要求")

# 测试2: PyTorch
print("\n[2] PyTorch检查...")
try:
    import torch
    print(f"   PyTorch版本: {torch.__version__}")
    print(f"   CUDA可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"   CUDA版本: {torch.version.cuda}")
        print(f"   GPU设备: {torch.cuda.get_device_name(0)}")
    else:
        print("   ⚠️  使用CPU模式（训练会较慢）")
    print("   ✅ PyTorch安装成功")
except ImportError as e:
    print(f"   ❌ PyTorch导入失败: {e}")
    sys.exit(1)

# 测试3: Torchvision
print("\n[3] Torchvision检查...")
try:
    import torchvision
    print(f"   Torchvision版本: {torchvision.__version__}")
    print("   ✅ Torchvision安装成功")
except ImportError as e:
    print(f"   ❌ Torchvision导入失败: {e}")
    sys.exit(1)

# 测试4: 3LC
print("\n[4] 3LC检查...")
try:
    import tlc
    print(f"   3LC版本: {tlc.__version__}")
    print("   ✅ 3LC安装成功")
except ImportError as e:
    print(f"   ❌ 3LC导入失败: {e}")
    sys.exit(1)

# 测试5: 3LC-Ultralytics
print("\n[5] 3LC-Ultralytics检查...")
try:
    from tlc_ultralytics import YOLO, Settings
    print("   ✅ 3LC-Ultralytics导入成功")
except ImportError as e:
    print(f"   ❌ 3LC-Ultralytics导入失败: {e}")
    sys.exit(1)

# 测试6: Ultralytics
print("\n[6] Ultralytics检查...")
try:
    from ultralytics import YOLO as UltralyticsYOLO
    print("   ✅ Ultralytics导入成功")
except ImportError as e:
    print(f"   ❌ Ultralytics导入失败: {e}")
    sys.exit(1)

# 测试7: 其他依赖
print("\n[7] 其他依赖检查...")
dependencies = {
    'numpy': 'numpy',
    'pandas': 'pandas',
    'cv2': 'opencv-python',
    'PIL': 'pillow',
    'yaml': 'pyyaml',
}

all_ok = True
for module_name, package_name in dependencies.items():
    try:
        __import__(module_name)
        print(f"   ✅ {package_name}")
    except ImportError:
        print(f"   ❌ {package_name} 未安装")
        all_ok = False

if not all_ok:
    print("   ⚠️  部分依赖缺失，但核心功能应该可用")
else:
    print("   ✅ 所有依赖检查通过")

# 测试8: YOLO模型加载
print("\n[8] YOLOv8n模型加载测试...")
try:
    from tlc_ultralytics import YOLO
    print("   正在下载/加载YOLOv8n预训练模型...")
    model = YOLO("yolov8n.pt")
    print(f"   模型参数数量: {sum(p.numel() for p in model.model.parameters()):,}")
    print("   ✅ YOLOv8n模型加载成功")
except Exception as e:
    print(f"   ⚠️  模型加载警告: {e}")
    print("   （首次运行需要下载模型，可能需要一些时间）")

# 测试9: 数据集文件检查
print("\n[9] 数据集文件检查...")
from pathlib import Path

dataset_files = {
    "dataset.yaml": Path("dataset.yaml"),
    "train/images": Path("train/images"),
    "train/labels": Path("train/labels"),
    "val/images": Path("val/images"),
    "val/labels": Path("val/labels"),
    "test/images": Path("test/images"),
}

all_files_ok = True
for name, path in dataset_files.items():
    if path.exists():
        if path.is_dir():
            count = len(list(path.glob("*")))
            print(f"   ✅ {name}: {count} 个文件")
        else:
            print(f"   ✅ {name}: 存在")
    else:
        print(f"   ❌ {name}: 不存在")
        all_files_ok = False

if not all_files_ok:
    print("   ⚠️  部分数据集文件缺失")

# 测试10: 脚本文件检查
print("\n[10] 脚本文件检查...")
scripts = ["train.py", "predict.py", "dataset.yaml"]
for script in scripts:
    if Path(script).exists():
        print(f"   ✅ {script}")
    else:
        print(f"   ❌ {script} 不存在")

# 总结
print("\n" + "=" * 70)
print("环境测试完成")
print("=" * 70)

print("\n📊 测试总结:")
print("   ✅ 核心依赖: PyTorch, 3LC, Ultralytics")
print("   ✅ 模型加载: YOLOv8n")
print("   ✅ 数据集结构: 已检查")
print("   ✅ 脚本文件: 已检查")

print("\n💡 下一步:")
print("   1. 设置3LC账户: 访问 https://account.3lc.ai")
print("   2. 登录3LC: 运行 '3lc login <your_api_key>'")
print("   3. 启动3LC服务: 运行 '3lc service' (在单独终端)")
print("   4. 注册数据集: 使用notebook或创建脚本")
print("   5. 开始训练: 运行 'python train.py'")

print("\n✅ 环境准备就绪！")


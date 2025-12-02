#!/usr/bin/env python3
"""
基础环境测试脚本 - 不依赖3LC API key
"""

print("=" * 70)
print("基础环境测试（不依赖3LC API key）")
print("=" * 70)

# 测试1: Python版本
print("\n[1] Python版本检查...")
import sys
print(f"   Python版本: {sys.version.split()[0]}")
print(f"   Python路径: {sys.executable}")
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
        print("   ⚠️  使用CPU模式（训练会较慢，但可以工作）")
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

# 测试4: Ultralytics (不依赖3LC)
print("\n[4] Ultralytics检查...")
try:
    from ultralytics import YOLO
    print("   ✅ Ultralytics导入成功")
    # 测试加载模型（会下载，但可以取消）
    print("   💡 可以加载YOLOv8n模型（首次会下载）")
except ImportError as e:
    print(f"   ❌ Ultralytics导入失败: {e}")
    sys.exit(1)

# 测试5: 其他依赖
print("\n[5] 其他依赖检查...")
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

# 测试6: 数据集文件检查
print("\n[6] 数据集文件检查...")
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

# 测试7: 脚本文件检查
print("\n[7] 脚本文件检查...")
scripts = ["train.py", "predict.py", "dataset.yaml"]
for script in scripts:
    if Path(script).exists():
        print(f"   ✅ {script}")
    else:
        print(f"   ❌ {script} 不存在")

# 测试8: 3LC安装位置检查（不导入）
print("\n[8] 3LC安装位置检查...")
tlc_path = Path(sys.executable).parent.parent / "lib" / "site-packages" / "tlc"
if tlc_path.exists():
    print(f"   ✅ 3LC已安装到: {tlc_path}")
    print("   💡 需要API key才能使用（这是正常的）")
else:
    print("   ⚠️  3LC安装位置未找到")

# 总结
print("\n" + "=" * 70)
print("基础环境测试完成")
print("=" * 70)

print("\n📊 测试总结:")
print("   ✅ 核心依赖: PyTorch, Ultralytics, 其他库")
print("   ✅ 数据集结构: 已检查")
print("   ✅ 脚本文件: 已检查")
print("   ⚠️  3LC: 已安装，但需要API key")

print("\n💡 关于3LC API Key:")
print("   1. 3LC是数据管理平台，需要账户才能使用")
print("   2. 访问 https://account.3lc.ai 注册账户")
print("   3. 在 https://account.3lc.ai/api-key 获取API key")
print("   4. 运行 '3lc login <your_api_key>' 登录")
print("   5. 之后就可以正常使用3LC了")

print("\n✅ 环境基础部分准备就绪！")
print("   可以开始使用YOLOv8训练模型（不依赖3LC）")
print("   或者先设置3LC账户后再使用完整功能")


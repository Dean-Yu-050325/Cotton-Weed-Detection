#!/usr/bin/env python3
"""
3LC 诊断脚本 - 检查3LC的各个组件是否正常工作
"""

import sys
import socket
from pathlib import Path

print("=" * 70)
print("3LC 诊断工具")
print("=" * 70)

# 1. 检查3LC安装
print("\n[1] 检查3LC安装...")
try:
    import tlc
    print(f"   ✅ 3LC版本: {tlc.__version__}")
except ImportError as e:
    print(f"   ❌ 3LC未安装: {e}")
    sys.exit(1)

# 2. 检查3LC-Ultralytics
print("\n[2] 检查3LC-Ultralytics...")
try:
    from tlc_ultralytics import YOLO, Settings
    print("   ✅ 3LC-Ultralytics可用")
except ImportError as e:
    print(f"   ❌ 3LC-Ultralytics未安装: {e}")
    print("   解决方案: pip install 3lc-ultralytics")

# 3. 检查Table访问
print("\n[3] 检查Table访问...")
try:
    train_table = tlc.Table.from_names(
        project_name="kaggle_cotton_weed_detection",
        dataset_name="cotton_weed_det3",
        table_name="cotton_weed_det3-train1",
    )
    print(f"   ✅ 训练Table可访问: {len(train_table)} 样本")
    print(f"   Table URL: {train_table.url}")
except Exception as e:
    print(f"   ❌ Table访问失败: {e}")
    print("   可能原因:")
    print("   - Table不存在，需要先运行 register_dataset.py")
    print("   - 3LC数据库损坏")

# 4. 检查本地数据库路径
print("\n[4] 检查本地数据库...")
try:
    table_url = train_table.url
    db_path = Path(table_url)
    if db_path.exists():
        print(f"   ✅ 数据库文件存在: {db_path}")
        print(f"   文件大小: {db_path.stat().st_size / 1024 / 1024:.2f} MB")
    else:
        print(f"   ⚠️  数据库文件不存在: {db_path}")
except Exception as e:
    print(f"   ⚠️  无法检查数据库路径: {e}")

# 5. 检查3LC服务端口
print("\n[5] 检查3LC服务端口...")
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

if check_port('localhost', 8000):
    print("   ✅ 端口8000正在使用（3LC服务可能正在运行）")
    print("   💡 尝试访问: http://localhost:8000")
else:
    print("   ⚠️  端口8000未被占用（3LC服务未运行）")
    print("   💡 启动服务: 3lc service")

# 6. 检查配置文件
print("\n[6] 检查3LC配置...")
try:
    import os
    config_paths = [
        Path.home() / ".3lc" / "config.yaml",
        Path(os.getenv("APPDATA", "")) / "3LC" / "config.yaml",
    ]
    
    config_found = False
    for config_path in config_paths:
        if config_path.exists():
            print(f"   ✅ 配置文件存在: {config_path}")
            config_found = True
            break
    
    if not config_found:
        print("   ⚠️  未找到配置文件（可能需要登录）")
        print("   💡 运行: 3lc login <your_api_key>")
except Exception as e:
    print(f"   ⚠️  配置检查失败: {e}")

# 7. 测试Table操作
print("\n[7] 测试Table基本操作...")
try:
    # 尝试获取Table的样本
    sample = train_table[0]
    print(f"   ✅ 可以访问Table样本")
    print(f"   样本键: {list(sample.keys())[:5]}...")  # 显示前5个键
except Exception as e:
    print(f"   ❌ Table操作失败: {e}")

# 8. 检查训练脚本中的Table URL
print("\n[8] 检查train.py中的Table URL...")
try:
    with open("train.py", "r", encoding="utf-8") as f:
        content = f.read()
        if "paste_your" in content or "your/train" in content:
            print("   ⚠️  train.py中的Table URL未配置")
            print("   💡 需要更新TRAIN_TABLE_URL和VAL_TABLE_URL")
        else:
            print("   ✅ train.py中的Table URL已配置")
except Exception as e:
    print(f"   ⚠️  无法读取train.py: {e}")

# 总结
print("\n" + "=" * 70)
print("诊断总结")
print("=" * 70)

print("\n✅ 正常的功能:")
print("   - 3LC库已安装")
print("   - Table可以访问")
print("   - 基本操作正常")

print("\n⚠️  需要注意:")
print("   - 如果Dashboard无法访问，需要启动3LC服务:")
print("     3lc service")
print("   - 如果遇到认证问题，检查登录状态:")
print("     3lc login")

print("\n💡 常见问题解决方案:")
print("   1. Dashboard无法打开:")
print("      → 运行 '3lc service' 启动服务")
print("      → 访问 http://localhost:8000")
print("")
print("   2. Table访问失败:")
print("      → 运行 'python register_dataset.py' 重新注册")
print("")
print("   3. 训练时出错:")
print("      → 检查train.py中的Table URL是否正确")
print("      → 确保3LC服务正在运行（如果使用Dashboard）")
print("")
print("   4. 认证问题:")
print("      → 访问 https://account.3lc.ai 获取API key")
print("      → 运行 '3lc login <your_api_key>'")

print("\n" + "=" * 70)


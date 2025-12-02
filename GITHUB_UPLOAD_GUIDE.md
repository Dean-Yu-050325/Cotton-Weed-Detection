# GitHub 上传指南

## 已完成的工作

✅ 已创建 `.gitignore` 文件，排除了以下内容：
- 数据集目录（train/, val/, test/）
- 虚拟环境（cottonweeddetect/）
- 模型权重文件（*.pt）
- 训练结果（runs/）
- 可视化样本（visualized_samples/）
- Python 缓存文件
- 其他临时文件

✅ 已初始化 Git 仓库
✅ 已创建初始提交（包含 17 个文件）

## 上传到 GitHub 的步骤

### 方法一：通过 GitHub 网页创建仓库（推荐）

1. **在 GitHub 上创建新仓库**
   - 访问 https://github.com/new
   - 输入仓库名称（例如：`cotton-weed-detection`）
   - 选择 **Public** 或 **Private**
   - ⚠️ **不要**勾选 "Initialize this repository with a README"（因为我们已经有了）
   - 点击 "Create repository"

2. **添加远程仓库并推送代码**
   
   在项目目录下执行以下命令（将 `YOUR_USERNAME` 和 `YOUR_REPO_NAME` 替换为你的实际值）：

   ```powershell
   # 添加远程仓库
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   
   # 重命名主分支为 main（如果 GitHub 使用 main 作为默认分支）
   git branch -M main
   
   # 推送代码到 GitHub
   git push -u origin main
   ```

   如果 GitHub 使用 `master` 作为默认分支，则使用：
   ```powershell
   git push -u origin master
   ```

### 方法二：使用 SSH（如果已配置 SSH 密钥）

```powershell
# 添加远程仓库（使用 SSH）
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送代码
git branch -M main
git push -u origin main
```

## 验证上传

上传完成后，访问你的 GitHub 仓库页面，应该能看到所有文件（除了被 .gitignore 排除的文件）。

## 后续更新代码

当你修改代码后，使用以下命令更新 GitHub：

```powershell
# 查看更改
git status

# 添加所有更改的文件
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到 GitHub
git push
```

## 注意事项

- ✅ 数据集文件（train/, val/, test/）已被排除，不会上传
- ✅ 虚拟环境（cottonweeddetect/）已被排除
- ✅ 模型权重文件（*.pt）已被排除（文件太大）
- ✅ 训练结果（runs/）已被排除
- ✅ 所有代码文件、配置文件和文档都已包含

## 如果遇到问题

### 问题：需要输入用户名和密码
**解决方案**：使用 Personal Access Token 代替密码
1. 访问 https://github.com/settings/tokens
2. 生成新的 token（选择 `repo` 权限）
3. 使用 token 作为密码

### 问题：分支名称不匹配
**解决方案**：检查 GitHub 仓库的默认分支名称，然后使用相应的命令：
```powershell
# 如果 GitHub 使用 main
git branch -M main
git push -u origin main

# 如果 GitHub 使用 master
git push -u origin master
```

### 问题：远程仓库已存在
**解决方案**：如果之前已经添加过远程仓库，先删除再重新添加：
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```


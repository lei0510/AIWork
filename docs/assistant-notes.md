# AI 助手经验与遇到的问题

## 1. 关键坑点

- GitHub CLI 安装后并不一定能直接通过 `gh` 找到，可执行文件可能只在 `C:\Program Files\GitHub CLI\gh.exe`。
- `gh auth login --web` 的设备授权流程不是短信验证码，而是需要在终端展示的“设备码”在浏览器页面输入。
- 登录流程如果浏览器页面卡在 `https://github.com/login/device` 或 `https://github.com/login/device/success`，可能是网络问题或代理/访问受限。
- 机器上如果没有可访问 `github.com:443`，则 `gh auth login` 和 `gh repo create` 都会失败。
- `git commit` 必须先设置 `user.name` 和 `user.email`，否则会报“Please tell me who you are”。
- 同一个工作区路径要一致。我先前在 `C:\Users\Admin\AIWork` 操作，后续实际工作区是 `E:\AIWork`，这个路径差异会导致命令失败。
- `git remote -v` 返回空表示本地仓库还没有远端配置，必须先用 `gh repo create` 或 `git remote add origin ...`。

## 2. 推荐给其他 AI 的方法

### 2.1 验证环境

- 先检查当前工作目录是否正确：`Get-Location` 或 `pwd`。
- 再检查是否已在 Git 仓库中：`git status --short --branch`。
- 如果不是仓库，就初始化：
  - `git init`
  - `git add README.md`
  - `git commit -m "Initial commit"`

### 2.2 GitHub CLI 与登录

- 优先使用 `gh` 的完整路径，如果 `gh` 不在 PATH 中：
  - `& 'C:\Program Files\GitHub CLI\gh.exe' auth login --web --git-protocol https`
- 如果登录未成功，验证网络：
  - `Test-NetConnection github.com -Port 443`
- 使用浏览器设备登录时，直接把终端生成的设备码输入页面，不要尝试用邮箱验证码。

### 2.3 远端仓库创建与推送

- 创建仓库并推送：
  - `gh repo create <repo-name> --public --source . --remote origin --push`
- 如果已经有远端仓库，配置远端后执行：
  - `git remote add origin https://github.com/<user>/<repo>.git`
  - `git push -u origin master`

## 3. 本次任务心得

本次会话里，最实用的经验是：
- 先把本地仓库状态搞清楚，再做 GitHub 登录
- 设备授权流程需要用户在浏览器里输入终端提示的码
- 如果本地命令失败，不要立即重试同一条命令，先检查路径、登录状态和网络

## 4. 推荐存放位置

这个文档放在 `docs/assistant-notes.md` 是合适的，因为它属于项目级“助手运行经验”和“复盘笔记”。

## 5. 备忘站点

- 记住这个站点：https://code.visualstudio.com/docs
- 任何与 VS Code 文档、插件、定制技能相关的信息，都优先保存在 AIWork 仓库里。

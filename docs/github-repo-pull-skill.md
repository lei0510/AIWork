# GitHub Repo Pull Skill

## 目标

把本地工作区仓库拉取、初始化、登录和推送到 GitHub 的整个流程记录下来。

## 已完成内容

- 当前工作区已成功初始化为 Git 仓库
- GitHub CLI 已安装并登录为 `lei0510`
- 已创建远端仓库 `https://github.com/lei0510/AIWork`
- 本地仓库已推送到远端

## 经验总结

1. 如果本地工作区不是 Git 仓库，先执行：
   - `git init`
   - `git add README.md`
   - `git commit -m "Initial commit"`
2. GitHub CLI 登录时，如果命令行提示 `Y/n`，要输入 `Y` 并按回车。
3. 设备授权码不是短信验证码，而是直接输入到 GitHub 设备授权页面。
4. 如果 `gh` 无法识别，先尝试完整路径：
   - `C:\Program Files\GitHub CLI\gh.exe`
5. 成功登录后，再创建仓库并推送：
   - `gh repo create AIWork --public --source . --remote origin --push`

## 推荐说明

- 这个技能适合用于“从空工作区初始化到 GitHub 仓库”的任务。
- 如果遇到网络问题，优先检查 `github.com:443` 的连通性。
- 如果遇到登录失败，要区分“设备授权码”与“邮箱验证码”。

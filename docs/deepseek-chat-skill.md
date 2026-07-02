# DeepSeek Chat Skill Documentation

## 目标

记录一个可重复的 DeepSeek 聊天自动化技能，以及一个可选脚本工具来辅助发送消息。

## 结构

- `.github/skills/deepseek-chat/SKILL.md`
  - 用于描述 DeepSeek 聊天技能的工作流程、质量检查和使用场景。
- `tools/deepseek-chat/send_deepseek_message.py`
  - Selenium 脚本，用于在 DeepSeek 聊天页面输入消息并发送。

## 使用方法

### 1. 技能调用

你可以直接说：
- “帮我把这句话发到 DeepSeek”
- “在 DeepSeek 页面里输入‘你好吗’并发送”

### 2. 脚本运行

确保系统已安装 ChromeDriver 与 Selenium，然后执行：

```bash
python tools/deepseek-chat/send_deepseek_message.py "你好吗"
```

如果你需要登录流程，可以先在浏览器里登录 DeepSeek，再运行脚本。

## 关键点

- 该脚本假定 DeepSeek 已登录并且页面可访问。
- 输入框选择器使用 `textarea[placeholder="Message DeepSeek"]`。
- 发送方式是模拟键盘按下 Enter。
- 如果 DeepSeek 页面结构变化，可能需要更新选择器。

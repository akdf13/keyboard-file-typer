# Keyboard File Typer

一个基于 `pydirectinput` 的 Windows 小工具，用模拟物理键盘输入的方式，把本地文本逐字符输入到当前焦点窗口。它适合在授权环境中处理无法直接复制粘贴、无法共享文件、但可以手动输入文本的场景，例如虚拟机、远程桌面或受限测试窗口。

> 仅在你拥有授权的环境中使用。这个工具会自动向当前焦点窗口发送键盘事件，运行前请确认焦点位置正确。

## 功能

- 从 `text.txt` 读取待输入内容。
- 倒计时后把内容逐字符输入到当前焦点窗口。
- 支持常见大小写字母、数字、换行和部分符号。
- 提供明文输入和 Base64 输入两个脚本版本。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `shu_ju_ku.py` | 默认按明文读取 `text.txt` 并输入，内置更多符号映射；也可以按代码注释切换为 Base64 输入。 |
| `shu_ju_ku_cn.py` | 读取 `text.txt` 后先转为 Base64，再模拟键盘输入。 |
| `text.example.txt` | 输入文件示例。实际使用时复制为 `text.txt`。 |
| `requirements.txt` | Python 依赖列表。 |

## 环境要求

- Windows
- Python 3.8+
- 英文键盘布局更稳定，建议运行前关闭中文输入法

安装依赖：

```powershell
pip install -r requirements.txt
```

## 使用方法

1. 复制示例输入文件：

   ```powershell
   copy text.example.txt text.txt
   ```

2. 编辑 `text.txt`，写入需要自动输入的内容。

3. 运行脚本：

   ```powershell
   python shu_ju_ku.py
   ```

   或者使用 Base64 输入版本：

   ```powershell
   python shu_ju_ku_cn.py
   ```

4. 脚本开始后会有 3 秒倒计时。在倒计时结束前，把光标点击到目标输入窗口中。

## 使用提示

- 如果目标环境只适合输入 ASCII 文本，优先使用 `shu_ju_ku_cn.py` 的 Base64 模式。
- 如果输出字符不正确，先检查键盘布局和输入法状态。
- 如果内容很长，建议先用短文本测试，确认焦点窗口、换行和符号都正常后再输入完整内容。
- `pydirectinput.FAILSAFE` 在脚本中被关闭，运行时请谨慎操作。

## 许可证

本项目使用 MIT License 开源，详见 [LICENSE](LICENSE)。

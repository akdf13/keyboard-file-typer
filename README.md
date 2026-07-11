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
| `type_text.py` | 按 UTF-8 明文读取 `text.txt` 并输入，支持更多常见符号映射。 |
| `type_base64.py` | 读取 `text.txt` 后先转为 Base64，再模拟键盘输入 ASCII 内容。 |
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
   python type_text.py
   ```

   或者使用 Base64 输入版本：

   ```powershell
   python type_base64.py
   ```

4. 脚本开始后会有 3 秒倒计时。在倒计时结束前，把光标点击到目标输入窗口中。

## 自定义等待时间与打字速度

两个脚本都可以通过修改文件末尾的 `delay` 参数来自定义开始输入前的等待时间：

```python
inject_hardware_scancodes("text.txt", delay=3)
```

`delay=3` 表示等待 3 秒。需要更多时间切换窗口时，可以改为 `5`、`10` 等更大的整数。

打字速度由脚本循环中的两处暂停时间控制：

```python
pydirectinput.keyDown(target_key)
time.sleep(0.005)  # 按键保持时间
pydirectinput.keyUp(target_key)

time.sleep(0.005)  # 两次击键之间的间隔
```

单位均为秒。数值越小，输入越快；数值越大，输入越慢，但在虚拟机、VNC 或远程桌面中通常更稳定。例如：

| 使用场景 | 按键保持时间 | 击键间隔 |
| --- | ---: | ---: |
| 本地窗口、追求速度 | `0.002` | `0.002` |
| 默认设置 | `0.005` | `0.005` |
| 远程环境、优先稳定 | `0.01` | `0.01` |

建议先用短文本测试。若出现漏字、字符顺序异常或目标窗口响应不及时，请逐步增大这两个数值。

## 使用提示

- 如果目标环境只适合输入 ASCII 文本，优先使用 `type_base64.py` 的 Base64 模式。
- 如果输出字符不正确，先检查键盘布局和输入法状态。
- 如果内容很长，建议先用短文本测试，确认焦点窗口、换行和符号都正常后再输入完整内容。
- `pydirectinput.FAILSAFE` 在脚本中被关闭，运行时请谨慎操作。

## 许可证

本项目使用 MIT License 开源，详见 [LICENSE](LICENSE)。

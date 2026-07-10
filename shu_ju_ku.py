import base64
import time
import sys
import os
import pydirectinput

pydirectinput.FAILSAFE = False
pydirectinput.PAUSE = 0

def inject_hardware_scancodes(file_path="text.txt", delay=3):
    if not os.path.exists(file_path):
        print(f"[-] 文件不存在: {file_path}")
        return

    print("[*] 正在读取并进行 Base64 编码...")
    with open(file_path, "rb") as f:
        b64_data = (f.read()).decode("utf-8")
# 默认为明文输入，若需要 Base64 编码请注释上一行，取消注释下一行
#        b64_data = base64.b64encode(f.read()).decode("utf-8")
    print(f"[*] 应输出字符为{b64_data}")
    print(f"[*] 编码完成，总字符数: {len(b64_data)}")
    print(f"\n[!] 请在 {delay} 秒内点击虚拟机内部的记事本空白处...")
    for i in range(delay, 0, -1):
        print(f"    剩余 {i} 秒...")
        time.sleep(1)
    print("\n[*] 🚀 开始发送底层硬件扫描码 (ScanCodes)...")

    total = len(b64_data)
    for index, char in enumerate(b64_data):

        need_shift = False
        target_key = char

        # 跳过 Windows 换行符中的 \r，防止触发两次回车
        if char == '\r':
            continue

        # 1. 拦截大写字母，转换为 Shift + 小写按键
        if char.isupper():
            need_shift = True
            target_key = char.lower()

        # 2. 拦截特殊符号
        elif char == '+':
            need_shift = True
            target_key = '='  # 物理键盘上打出 + 需要 Shift 和 =
        elif char == '/':
            target_key = '/'
        elif char == '=':
            target_key = '='
        elif char == ']':
            target_key = ']'
        elif char == '[':
            target_key = '['
        elif char == '.':
            target_key = '.'

        elif char == '(':
            need_shift = True
            target_key = '9'  # Shift + 9 = (
        elif char == ')':
            need_shift = True
            target_key = '0'  # Shift + 0 = )
        elif char == '*':
            need_shift = True
            target_key = '8'  # Shift + 8 = *
        elif char == '<':
            need_shift = True
            target_key = ','  # Shift + , = <
        elif char == '>':
            need_shift = True
            target_key = '.'  # Shift + . = >
        elif char == '^':
            need_shift = True
            target_key = '6'  # Shift + 6 = ^
        elif char == '%':
            need_shift = True
            target_key = '5'  # Shift + 5 = %
        elif char == '&':
            need_shift = True
            target_key = '7'  # Shift + 7 = &
        elif char == '$':
            need_shift = True
            target_key = '4'  # Shift + 4 = $
        elif char == '#':
            need_shift = True
            target_key = '3'  # Shift + 3 = #
        elif char == '@':
            need_shift = True
            target_key = '2'  # Shift + 2 = @
        elif char == '!':
            need_shift = True
            target_key = '1'  # Shift + 1 = !
        elif char == '_':
            need_shift = True
            target_key = '-'  # Shift + - = _
        elif char == '+':
            need_shift = True
            target_key = '='  # Shift + = = +
        elif char == '{':
            need_shift = True
            target_key = '['  # Shift + [ = {
        elif char == '}':
            need_shift = True
            target_key = ']'  # Shift + ] = }
        elif char == '"':
            need_shift = True
            target_key = "'"  # Shift + ] = }
        elif char == '\n':
            target_key = 'enter' # 映射到回车键
        # ==========================================

        # 3. 严格模拟物理击键的肌肉动作
        if need_shift:
            pydirectinput.keyDown('shift') # 踩下 Shift 离合

        pydirectinput.keyDown(target_key)  # 按下目标键
        time.sleep(0.005)                   # 短暂亦不可缺少的停留 (对付 VNC 校验)
        pydirectinput.keyUp(target_key)    # 抬起目标键

        if need_shift:
            pydirectinput.keyUp('shift')   # 松开 Shift 离合

        # 两次独立击键间的空隙
        time.sleep(0.005)

        if (index + 1) % 50 == 0 or (index + 1) == total:
            print(f"\r[*] 进度: {((index + 1) / total) * 100:.1f}%", end="")

    print("\n\n[+] ✅ 输入执行完毕！")

if __name__ == "__main__":
    inject_hardware_scancodes("text.txt", delay=3)
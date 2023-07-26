import os
import sys
# import subprocess


def delete_ds_store():
    # 获取可执行文件所在目录
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f"当前目录：{current_dir}")

    # 遍历当前目录，删除所有 .DS_Store 文件
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file == '.DS_Store':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"已删除文件：{file_path}")


if __name__ == "__main__":
    delete_ds_store()
    print("已删除当前目录及其子目录下所有的 .DS_Store 文件，您可以关闭此窗口。")

    # # 使用subprocess模块运行关闭终端窗口的命令（适用于macOS）
    # if sys.platform.startswith('darwin'):
    #     subprocess.run("osascript -e 'tell application \"Terminal\" to close first window'", shell=True)

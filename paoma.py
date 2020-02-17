"""
跑马灯
"""

import os
import time


def main():
    text = "北京欢迎您......北京欢迎您......."
    while True:
        os.system("cls")
        print(text)
        time.sleep(0.01)
        text = text[1:]+text[0]

if __name__ == "__main__":
    main()

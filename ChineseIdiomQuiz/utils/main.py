from strictMode import strict
from easyMode import easy

if __name__ == "__main__":
    print("选择难度：1.困难模式；2.简单模式")
    inp = input()
    if int(inp) == 1:
        strict()
    else:
        easy()

# -*- encoding: utf-8 -*-
"""
@File    : demo_mysql.py
@Time    : 2019/10/15 2:40 PM
@Author  : slyu
@Email   : yusulong@threathunter.cn
@Software: PyCharm
"""
import schedule
import time
from utls import InitialPackage, update


if __name__ == "__main__":
    InitialPackage().process("mongodb")
    schedule.every().day.at("10:30").do(update, ("mongodb", "schedule"))
    while True:
        schedule.run_pending()
        time.sleep(1)

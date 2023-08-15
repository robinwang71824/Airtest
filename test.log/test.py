#!/usr/bin/env python3
# -*- encoding=utf8 -*-
import os
import shutil
from github import Github
from github import Auth
from datetime import datetime

__author__ = "esunmoda"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
ST.OPDELAY = 3
ST.THRESHOLD = 0.9
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/NCAIB7000449YV8?cap_method=MINICAP&touch_method=MAXTOUCH&",])
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import os
import logging
logging.basicConfig(filename= datetime.today().strftime("%Y-%m-%d") + "_error_log",level=logging.ERROR)

# script content
print("start...")
err_msg=""
def run_script():
    sum = 0
    all = 27
    try:
        #f = open('password.txt')
        #password = f.read()
        #f.close()
        
        currdir=os.path.dirname(__file__)
        password_path=os.path.join(currdir,'..','password.txt')
        with open(password_path,'r') as f:
            password = f.read()
        
        #開啟app
        start_app("com.esun")
        sleep(5)
        sum += 1
        #輸入密碼
        poco("com.esun:id/et_show_mp").set_text(password)
        sum += 1
        #登入
        touch(Template(r"tpl1690873077664.png", record_pos=(-0.288, -0.155), resolution=(1080, 2400)))
        sum += 1
        sleep(3)
        #關閉訊息通知
        if exists(Template(r"tpl1690873099839.png", record_pos=(-0.381, -0.956), resolution=(1080, 2400))):
            touch(Template(r"tpl1690873099839.png", record_pos=(-0.381, -0.956), resolution=(1080, 2400)))
        #委託下單
        touch(Template(r"tpl1690873133201.png", record_pos=(-0.001, 0.381), resolution=(1080, 2400)))
        sum += 1
        #證券下單
        touch(Template(r"tpl1690873145137.png", record_pos=(0.008, -0.578), resolution=(1080, 2400)))
        sum += 1
        #搜尋
        touch(Template(r"tpl1690873159402.png", record_pos=(0.405, -0.793), resolution=(1080, 2400)))
        sum += 1
        #類股
        touch(Template(r"tpl1690873170952.png", record_pos=(0.116, -0.844), resolution=(1080, 2400)))
        sum += 1
        #食品類股
        touch(Template(r"tpl1690873181033.png", record_pos=(-0.38, -0.281), resolution=(1080, 2400)))
        sum += 1
        #味全
        touch(Template(r"tpl1690873195555.png", record_pos=(-0.088, -0.706), resolution=(1080, 2400)))
        sum += 1
        #取價
        touch(Template(r"tpl1690873215689.png", record_pos=(0.358, -0.245), resolution=(1080, 2400)))
        sum += 1
        #跌停
        touch(Template(r"tpl1690873224470.png", record_pos=(0.34, 0.194), resolution=(1080, 2400)))
        sum += 1
        #買進
        touch(Template(r"tpl1690873237695.png", record_pos=(-0.206, -0.095), resolution=(1080, 2400)))
        sum += 1
        #下單
        touch(Template(r"tpl1690873248999.png", record_pos=(-0.242, 0.99), resolution=(1080, 2400)))
        sum += 1
        #委託下單
        touch(Template(r"tpl1690873267756.png", record_pos=(-0.204, 0.366), resolution=(1080, 2400)))
        sum += 1
        #輸入密碼
        poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.esun:id/et_show_mp").set_text(password)
        sum += 1
        #記憶密碼
        touch(Template(r"tpl1690960004918.png", record_pos=(0.319, 0.005), resolution=(1080, 2400)))
        sum += 1
        #確定
        touch(Template(r"tpl1690960011329.png", record_pos=(-0.195, 0.18), resolution=(1080, 2400)))
        sum += 1
        sleep(5)
        #關閉視窗
        if exists(Template(r"tpl1691569808227.png", record_pos=(0.399, -0.394), resolution=(1080, 2400))):
            touch(Template(r"tpl1691569808227.png", record_pos=(0.399, -0.394), resolution=(1080, 2400)))
        sum += 1
        #返回首頁
        touch(Template(r"tpl1691989827219.png", record_pos=(-0.409, -0.948), resolution=(1080, 2400)))
        sum += 1

        #整股刪單
        #帳務查詢
        touch(Template(r"tpl1691398001629.png", record_pos=(0.001, 0.719), resolution=(1080, 2400)))
        sum += 1
        #委託查詢
        touch(Template(r"tpl1691398010064.png", record_pos=(-0.105, 0.014), resolution=(1080, 2400)))
        sum += 1
        #委託查詢
        touch(Template(r"tpl1691398020644.png", record_pos=(0.32, 0.241), resolution=(1080, 2400)))
        sum += 1
        #刪改按鈕
        touch(Template(r"tpl1691992766630.png", record_pos=(-0.419, -0.455), resolution=(1080, 2400)))
        #poco("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("android:id/content").offspring("com.esun:id/content_frame").offspring("com.esun:id/account_detail_content").offspring("com.esun:id/fL_accounts").child("android.webkit.WebView").offspring("android.widget.GridView").child("android.view.View")[3].offspring("刪改")[0].click()
        sum += 1
        #確認
        touch(Template(r"tpl1691399160175.png", record_pos=(-0.254, 0.934), resolution=(1080, 2400)))
        sum += 1
        #確認
        touch(Template(r"tpl1691399171195.png", record_pos=(-0.179, 0.173), resolution=(1080, 2400)))
        sum += 1
        #關閉
        touch(Template(r"tpl1691399181758.png", record_pos=(0.401, -0.394), resolution=(1080, 2400)))
        sum += 1
        #關閉app
        stop_app("com.esun")
        sum += 1
    except Exception as e:
        log(e,snapshot=True)

    finally:
        # generate html report
        #from airtest.report.report import simple_report
        #simple_report(__file__,logpath=True)
        from airtest.report.report import LogToHtml
        r = LogToHtml(script_root="test.py",export_dir=r"../",lang="zh",plugins=["poco.utils.airtest.report"])
        r.report()
        return sum,all

def build_zip():
    try:
        shutil.make_archive('../A+_report','zip','../test.log')
    except Exception as e:
        logging.error(e)
        global err_msg 
        err_msg = "建立壓縮檔錯誤"

def upload_github():
    try:
        username = "robinwang71824"
        password = "Wanwan1995"
        token = Auth.Token("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")
        g=Github(auth = token)
        repo=g.get_repo("robinwang71824/Airtest")
        with open("../A+_report.zip","rb") as file:
            data = file.read()
        repo.create_file("A+_report.zip","upload report",data,branch="main")
    except Exception as e:
        logging.error(e)
        global err_msg 
        err_msg = "上傳github錯誤"

def send_email():
    import email.message
    try:
        #建立email訊息物件
        msg=email.message.EmailMessage()
        today=datetime.today().strftime("%Y-%m-%d")

        #利用物件建立基本設定
        msg["From"]="rjgwang1995@gmail.com"
        #msg["To"]="senwang-71039@esunsec.com.tw,robinwang-71824@esunsec.com.tw,ronwu-71230@esunsec.com.tw"
        msg["To"]="robinwang-71824@esunsec.com.tw,ronwu-71230@esunsec.com.tw"
        msg["Subject"]=today + "A+_Android每日檢查報告"

        #輸入寄送郵件主要內容
        #msg.add_alternative("<h3>HTML內容</h3>安安這是寄送郵件測試",subtype="html") #HTML信件內容
        msg.set_content( today + "測試報告已完成，欲查看報告請點選連結" + "\nhttps://github.com/robinwang71824/Airtest")

        #連線到SMTP Sevver
        acc="rjgwang1995@gmail.com"
        password="thbmucoarikbyxlf"

        import smtplib
        server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連線
        server.login(acc,password)
        server.send_message(msg)
        #發送完成後關閉連線
        server.close()
    except Exception as e:
        logging.error(e)
        global err_msg 
        err_msg = "寄送信件錯誤"

def line_notify(start_time,end_time,sum,all):
    try:
        import requests
        token = 'QXogxn6zgRQlh7k7JQj5JdwO5XpRPliKvPLENDkBNUv'
        headers = {"Authorization": "Bearer " + token,}
        payload = {'message': "\n" + "Android_A+\n" + f"{start_time}開始\n" + f"{end_time}完成\n" + f"共{all}項，完成{sum}項" + f"\n{err_msg}"}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        print(r.status_code)
        return r.status_code
    except Exception as e:
        logging.error(e)
        #global err_msg 
        #ßerr_msg = "line通知錯誤"
        
if __name__ == '__main__':
    try:
        
        start_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        sum,all = run_script()
        end_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        build_zip()
        #upload_github()
        send_email()
        line_notify(start_time,end_time,sum,all)
    except Exception as e:
        logging.error(e)
   

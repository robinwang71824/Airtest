# -*- encoding=utf8 -*-
__author__ = "esunmoda"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
ST.OPDELAY = 1

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/NCAIB7000449YV8?cap_method=MINICAP&touch_method=MAXTOUCH&",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")
try:
    if exists(Template(r"/Users/esunmoda/Desktop/script/A/A1/A1-1.png")):
        touch(Template(r"/Users/esunmoda/Desktop/script/A/A1/A1-1.png"))

    a=int(poco(text="庫存總市值").parent().child()[1].attr("text"))
    b=int(poco(text="庫存總成本").parent().child()[2].attr("text"))
    print(b)
    c=int(poco(text="銀行餘額").parent().child()[3].attr("text"))
    print(c)
    d=int(poco(text="近三日交割").parent().child()[7].attr("text"))
    print(d)
    e=int(poco(text="今日應收付").parent().child()[8].attr("text"))
    print(e)
    f=int(poco(text="庫存損益").parent().child()[1].attr("text")[:-1])
    print(f)    
    g=int(poco(text="庫存損益").parent().parent().child()[1].attr("text"))
    print(g)   
    
    flag = 0
    if a>=0 and b>=0 and c>=0 and d>=0 and e>=0 and f>=0 and g>=0:
        flag = 1
        log("",desc="完成",snapshot=True)
    if flag == 0:
        raise Exception("帳務顯示數字有誤")
except Exception as e:
    log(e,desc="帳務顯示數字有誤",snapshot=True)

finally:
    # generate html report
    from airtest.report.report import simple_report
    simple_report(__file__,logpath=True)
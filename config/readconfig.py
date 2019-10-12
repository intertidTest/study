import configparser
import os
#获取当前文件的上一级目录
base_dir=os.path.dirname(__file__)
#获取配置文件config.ini地址
config_path=os.path.join(base_dir,'config.ini')
#获取logs（日志）的路径
log_dir=os.path.join(os.path.dirname(base_dir),'logs')
#获取测试数据地址
test_data_load=os.path.join(os.path.dirname(base_dir),'testData')
print(test_data_load)
#获取截图地址
img_path=os.path.join(os.path.dirname(base_dir),'screenshot')
#获取测试报告地址
report_path=os.path.join(os.path.dirname(base_dir),'report')
#测试用例路径
test_path=os.path.join(os.path.dirname(base_dir),'testcase')
print(img_path)
#获取测试url地址
class Myconfig:
    def __init__(self):
        config=configparser.ConfigParser()
        config.read(config_path)
        self.url=config.get('http','url')
        self.dicDatas=config.get('testData','fileName')
myconfig=Myconfig()

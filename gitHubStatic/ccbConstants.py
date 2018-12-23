# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/11/21'

# 定义常量类中的fielPaths 表示git需要获取的地址
def filePaths():
    filePathList=[
    'ebs-api',
    'ebs-biz-service',
    'ebs-ccbctmz-service',
    'ebs-common',
    'ebs-member-service',
    'ebs-selectionTest-service',
    'ebs-system-service',
    'ebs-workflow2-service'
    ]
    return filePathList;

def nameConvert(name):
    nameDict ={
        'yuandd':'袁东东',
        '刘恒志':'刘恒志',
        '87123801.ZH':'',
        'Iamyl':'杨磊',
        'cairw':'蔡如旺',
        'cuixq':'崔晓乾',
        'gongjiabao':'龚家宝',
        'gsx':'郭诗雄',
        'hhh':'何欢欢',
        'hsh':'胡双辉',
        'hsm':'黄士明',
        'huangj':'黄进',
        'hyb':'贺艳彬',
        '杨磊':'杨磊',
        'jcs':'简春水',
        'jiangb':'姜彪',
        'jiayanguang':'贾艳广',
        'lc':'林城',
        'lhb':'龙华彬',
        'libin':'李彬',
        'lihua4.zh':' ',
        'liupan':'刘攀',
        'lll':'刘琳琳',
        'luxiyang':'卢西洋',
        'luxy':'卢西洋',
        'jiayanguang':'贾艳广',


    }
    return nameDict[name];

# 定义常量类中的emailConvert 表示git用eamil 转换成具体的名称
def emailConvert(email):
    emailDict={
        'LHB@ebidding.com.cn':'龙华彬',
        'cairw@ebidding.com.cn':'蔡如旺',
        'cxq@ebidding.com.cn':'崔晓乾 ',
        'gongjiabao@ebidding.net.cn':'龚家宝 ',
        'gsk@ebidding.net.cn':'顾双凯 ',
        'gsx@qq.com':'郭诗雄',
        'gsx@ebidding.net.cn':'郭诗雄',
        'hhh@ebidding.net.cn':'何欢欢 ',
        'hsh@ebidding.net.cn':'胡双辉 ',
        'hsm19950709@gmail.com':'黄士明 ',
        'hsm@ebidding.net.cn':'黄士明',
        'huangj@ebidding.net.cn':'黄进',
        'hyb@ebidding.net.cn':'贺艳彬 ',
        'jcs@ebidding.net.cn':'简春水',
        'jiangb@ebidding.net.cn':'姜彪',
        'lc@yinengcai.com':'林城',
        'lhz@ebidding.com.cn':'刘恒志',
        'libin@ebidding.net.n':'李彬 ',
        'lll@ebidding.net.cn':'刘岭岭',
        'luxy@ebidding.net.cn':'卢西洋 ',
        'qiyang@ebidding.com.cn':'祁洋',
        'songbn@ebidding.com':'宋博宁',
        'smc@ebidding.com.cn':'沈明春',
        'wgy@ebidding.com.cn':'王光英',
        'wjl@ebidding.com.cn':'王进伟',
        'lizhishun.zh@ccb.com':'李志顺',
        'fxl@ebidding.net.cn':'fxl',
        'chenzh@ebidding.com.cn':'陈振辉',
        'wushuang@ebidding.com.cn':'吴双',
        'wyh@ebidding.com.cn':'王宇辉',
        'wzh@ebidding.net.cn':'王志辉',
        'xiawenyu@ebidding.com.cn':'夏文宇',
        'xiawenyu@ebidding.comcn':'夏文宇',
        'xzw@ebidding.net.cn':'徐子文',
        'yanglei@ebidding.com.cn':'杨磊',
        'zhangfan@ebidding.com.cn':'张凡',
        'zhongbiao@yusys.com.cn':'钟彪',
        'zhouxiang@ebidding.com.cn':'周翔',
        'zjq@ebidding.net.cn':'周举琪',
        'zkx@ebidding.com.cn':'郑开鑫',
        'zmq@ebidding.net.cn':'张美琪',
        'lhb@ebidding.com.cn':'龙华彬',
        'zhoulh@ebidding.com.cn':'周玲辉',
        'zsz@ebidding.net.cn':'张帅征'
    }
    if emailDict.get(email)==None:
        return email
    else:
        return emailDict.get(email)

if  __name__ == '__main__':
   print emailConvert('zsz@ebidding.net.c2')
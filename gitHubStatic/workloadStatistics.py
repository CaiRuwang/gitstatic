# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/11/21'

import subprocess
import ccbConstants as constants
import UserWorkInfo as UserWorkInfo

def commitInfo(filePath,sinceDate,endDate):
    #print filePath
    pNames = subprocess.Popen(
        "git log --format='%ae' | sort -u | while read name;do echo \"$name\t\";done",
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=filePath)
    names = []

    while pNames.poll() is None:
        line = pNames.stdout.readline()
        line = line.strip()
        if line:
            name = str(line)
            names.append(name)

    workInfoDic={}
    for name in names:
        line=commitLineInfo(name,filePath,sinceDate,endDate)
        nums=commitNumsInfo(name,filePath,sinceDate,endDate)
        thisName=constants.emailConvert(name)
        #print (thisName +'  '+line +',  commits: '+nums)
        userWorkInfo=parseResult2Object(thisName +'  '+line +',  commits: '+nums)
        print userWorkInfo.userName
    pNames.wait()

# 函数用来统计 提交人 新增代码行数，删除代码行数，以及总行数
def commitLineInfo(name,filePath,sinceDate,endDate):
    commitInfo='';
    pLogs = subprocess.Popen(
        "git log --since =" +sinceDate+ "  --until=" +endDate+ "   --author=" + name + " --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 + $2 } END { printf \", addedLines: %s, removedLines: %s, totalLines: %s\\n\",add,subs,loc};'",
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=filePath)
    while pLogs.poll() is None:
        line = pLogs.stdout.readline()
        line = line.strip()
        if line:
            line = str(line)
            commitInfo=line
    pLogs.wait()
    return commitInfo;

# 函数用来统计 提交人提交代码次数
def commitNumsInfo(name,filePath,sinceDate,endDate):
    commitInfo='';
    pLogs = subprocess.Popen(
        "git log --since =" +sinceDate+ "  --until=" +endDate+ "  --author=" + name + " --pretty=oneline | wc -l",
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=filePath)
    while pLogs.poll() is None:
        line = pLogs.stdout.readline()
        line = line.strip()
        if line:
            line = str(line)
            commitInfo=line
    pLogs.wait()
    return commitInfo;


#获取代码记录行数进行转换 判断如果为空时则默认为0
def parseResultNums(sysOutStr):
    resultNums=0;
    strs=sysOutStr.split(":")
    if(strs[1].isdigit()):
        resultNums=strs[1]
    return resultNums;

# 将字符串转换成对象
def parseResult2Object(resultStr):
    strs=resultStr.split(",");
    userName= strs[0]
    addLines=parseResultNums(strs[1])
    removedLines=parseResultNums(strs[2])
    totalLines=parseResultNums(strs[3])
    commits=parseResultNums(strs[4])
    userWorkInfo= UserWorkInfo.UserWorkInfo(userName,addLines,removedLines,totalLines,commits)
    return userWorkInfo



if  __name__ == '__main__':
    # 考虑当gitHub有多个的情况时需要进行遍历多个git地址 故采用定义常量类定义路径
    for filePath in  constants.filePaths():
         commitInfo("/Users/cairuwang/java/code/ccb_v5/"+filePath,'2018-10-01','2018-11-21')

# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/11/21'

import subprocess
import ccbConstants as constants
import UserWorkInfo as UserWorkInfo

def commitInfo(filePath,sinceDate,endDate,workInfoDic):
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


    for name in names:
        line=commitLineInfo(name,filePath,sinceDate,endDate)
        nums=commitNumsInfo(name,filePath,sinceDate,endDate)
        thisName=constants.emailConvert(name)
        resultStr= thisName +'  '+line +',  commits: '+nums
        resultdo(workInfoDic,resultStr)
        #userWorkInfo=parseResult2Object(resultStr)
        #sprint userWorkInfo.userName
    pNames.wait()
    print len(workInfoDic)



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
    if(is_number(strs[1])):
        resultNums=int(strs[1])
    return resultNums;


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
# 将字符串转换成对象
def parseResult2Object(resultStr):
    strs=resultStr.split(",");
    userName= userNameParse(strs[0])
    addLines=parseResultNums(strs[1])
    removedLines=parseResultNums(strs[2])
    totalLines=parseResultNums(strs[3])
    commits=parseResultNums(strs[4])
    userWorkInfo= UserWorkInfo.UserWorkInfo(userName,addLines,removedLines,totalLines,commits)
    return userWorkInfo

def userNameParse(userName):
    if(userName.isdigit()):
        return  str(userName)
    else:
        return  userName


#将结果集进行处理如果用户已经存在则将结果进行合并 如果结果不存在则放入字典
def resultdo(workInfoDic,resultStr):
    #print resultStr
    userWorkInfo=parseResult2Object(resultStr)
    if(workInfoDic.get(userWorkInfo.userName)):
       oldUserWorkInfo= workInfoDic.get(userWorkInfo.userName)
       addLines=oldUserWorkInfo.addLines+userWorkInfo.addLines
       removedLines=oldUserWorkInfo.removedLines+userWorkInfo.removedLines
       totalLines=oldUserWorkInfo.totalLines+userWorkInfo.totalLines
       commits=oldUserWorkInfo.commits+userWorkInfo.commits
       newUserWorkInfo=UserWorkInfo.UserWorkInfo(userWorkInfo.userName,addLines,removedLines,totalLines,commits)
       workInfoDic.update({userWorkInfo.userName: newUserWorkInfo})
    else:
        workInfoDic.update({userWorkInfo.userName: userWorkInfo})





if  __name__ == '__main__':
    # 考虑当gitHub有多个的情况时需要进行遍历多个git地址 故采用定义常量类定义路径
    workInfoDic={}
    for filePath in  constants.filePaths():
         commitInfo("/Users/cairuwang/java/code/ccb_v5/"+filePath,'2018-10-01','2018-11-21',workInfoDic)
    #print workInfoDic.items();
    for key in workInfoDic:
        print workInfoDic[key].userName +' addLines:'+str(workInfoDic[key].addLines)+' ,removedLineds:'+str(workInfoDic[key].removedLines)+' ,totalLines:'+str(workInfoDic[key].totalLines)+' ,commits: '+str(workInfoDic[key].commits)
# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/06/26'

import subprocess
import ccbConstants as constants

def commitInfo(filePath,sinceDate,endDate):
    print filePath
    pNames = subprocess.Popen(
        "git log --format='%aN' | sort -u | while read name;do echo \"$name\t\";done",
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
        print (name +'  '+line +' ,commits: '+nums)

    pNames.wait()

# 函数用来统计 提交人 新增代码行数，删除代码行数，以及总行数
def commitLineInfo(name,filePath,sinceDate,endDate):
    commitInfo='';
    pLogs = subprocess.Popen(
        "git log --since =" +sinceDate+ "  --until=" +endDate+ "  --author=" + name + " --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 + $2 } END { printf \"added lines: %s, removed lines: %s, total lines: %s\\n\",add,subs,loc};'",
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



if  __name__ == '__main__':
    for filePath in  constants.filePaths():
         commitInfo("/Users/cairuwang/java/code/ccb_v5/"+filePath,'2018-10-01','2018-11-21')

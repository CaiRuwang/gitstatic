# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/06/26'

import subprocess

def totalNums(filePath,sinceData,endData):
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
        pLogs = subprocess.Popen(
            "git log --since =" +sinceData+ "  --until=" +endData+ "  --author=" + name + " --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 + $2 } END { printf \"added lines: %s, removed lines: %s, total lines: %s\\n\",add,subs,loc};'",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=filePath)
        while pLogs.poll() is None:
            line = pLogs.stdout.readline()
            line = line.strip()
            if line:
                line = str(line)
                print(name + " " + line)
        pLogs.wait()

    pNames.wait()

if  __name__ == '__main__':
    totalNums("/Users/cairuwang/java/code/ccb_v5/ebs-ccbctmz-service",'2018-10-01','2018-11-21')
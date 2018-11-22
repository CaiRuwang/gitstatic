# -*- coding: utf-8 -*-
__Author__ = "vans"
__Date__ = '2018/06/26'

import subprocess

def totalCommitNums(filePath):
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
            "git log --since ==2018-10-01 --until==2018-11-21  --author=" + name + " --pretty=oneline | wc -l ",
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
    totalCommitNums("/Users/cairuwang/java/code/ccb_v5/ebs-ccbctmz-service")
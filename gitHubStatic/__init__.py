# -*- coding: utf-8 -*-
import subprocess

# git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --since ==2018-05-05 --until==2018-07-05 --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 + $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
gitDir = "/Users/cairuwang/java/code/ccb_v5/ebs-ccbctmz-service"
pNames = subprocess.Popen(
    "git log --format='%aN' | sort -u | while read name;do echo \"$name\t\";done",
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=gitDir)
names = []

while pNames.poll() is None:
    line = pNames.stdout.readline()
    line = line.strip()
    if line:
        name = str(line)
        names.append(name)

for name in names:
    pLogs = subprocess.Popen(
        "git log --since ==2018-10-01 --until==2018-11-21  --author=" + name + " --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 + $2 } END { printf \"added lines: %s, removed lines: %s, total lines: %s\\n\",add,subs,loc};'",
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=gitDir)
    while pLogs.poll() is None:
        line = pLogs.stdout.readline()
        line = line.strip()
        if line:
            line = str(line)
            print(name + " " + line)
    pLogs.wait()

pNames.wait()

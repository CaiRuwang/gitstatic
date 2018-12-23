# -*- coding: utf-8 -*-





if  __name__ == '__main__':
    str="123456  , addedLines: 324, removedLines: , totalLines: 324, commits: 4"
    strs=str.split(",")
    for i  in strs:
        if i.find(":")>=0:
            print i.split(":")[1]
        else:
            print i
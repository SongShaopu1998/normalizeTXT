#!/usr/bin/env python 3.x
# -*- coding: utf-8 -*-
# @Time     : 2020/5/17 21:07
# @Author   : shaopu
# @Email    : songshaopu1998@gmail.com
# @File     : normalize.py
# @Software : PyCharm
import re

if __name__ == '__main__':
    new_content = ''
    with open('TOC.txt', 'r', encoding='UTF-8') as f:
        content = f.read()
        space = content.replace(' ', '-').replace('\t', '    ')
        # print(content)
        # enter = re.findall('\n', content)
        line = space.split('\n')
        Max = len(line[0].encode('gbk'))
        for k in range(len(line)):
            temp = len(line[k].encode('gbk'))
            if temp >= Max:
                Max = temp
        # print(enter)
        # print(len(line))
        for i in range(len(line)):
            line2str = line[i]
            len_line2str = len(line2str.encode('gbk'))
            # print(len(line[i]))
            # print(len(line2str))
            if len_line2str < Max:
                dif = Max - len_line2str
                str2line = list(line2str)
                for j in range(dif):
                    str2line.insert(-2, '-')
                    dif = Max - len(''.join(str2line).encode('gbk'))
                    if dif == 0:
                        line2str = ''.join(str2line)
                        break
            new_content += (line2str + '\n')
        print(new_content)

    with open('TOC.txt', 'w', encoding='utf-8') as f:
        f.write(new_content)

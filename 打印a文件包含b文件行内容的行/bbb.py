#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import os
with open("b.txt") as f:
	for i in f:
       		with open("a.txt") as ff:
       			for k in ff:
				if k.replace('\n','') in i.replace('\n',''):
       					with open("dd.txt", 'a') as fff:
                            fff.write(i)
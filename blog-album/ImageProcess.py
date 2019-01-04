#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ? 2017 Register <registerdedicated(at)gmail.com>
#
# Distributed under terms of the GPLv3 license.

"""
"""
# coding=utf-8
from PIL import Image
import shutil
import os

class Graphics:
    '''ͼƬ������
    ����
    -------
    infile: �����ļ�·��
    outfile: ����ļ�·��
    '''
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def fixed_size(self, width, height):
        """���չ̶��ߴ紦��ͼƬ"""
        im = Image.open(self.infile)
        out = im.resize((width, height),Image.ANTIALIAS)
        out.save(self.outfile)


    def resize_by_width(self, w_divide_h):
        """���տ�Ƚ��������������"""
        im = Image.open(self.infile)
        (x, y) = im.size
        x_s = x
        y_s = x/w_divide_h
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(self.outfile)


    def resize_by_height(self, w_divide_h):
        """���ո߶Ƚ��������������"""
        im = Image.open(self.infile)
        (x, y) = im.size
        x_s = y*w_divide_h
        y_s = y
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(self.outfile)


    def resize_by_size(self, size):
        """��������ͼƬ�ļ���С���д���(��λKB)"""
        size *= 1024
        im = Image.open(self.infile)
        size_tmp = os.path.getsize(self.infile)
        q = 100
        while size_tmp > size and q > 0:
            print (q)
            out = im.resize(im.size, Image.ANTIALIAS)
            out.save(self.outfile, quality=q)
            size_tmp = os.path.getsize(self.outfile)
            q -= 5
        if q == 100:
            shutil.copy(self.infile, self.outfile)


    def cut_by_ratio(self):
        """����ͼƬ������зָ�
        ------------
        ȡ�м�Ĳ��֣��ü���������
        """
        im = Image.open(self.infile)
        (x, y) = im.size
        if x > y:
            region = (int(x/2-y/2), 0, int(x/2+y/2), y)
            #����ͼƬ
            crop_img = im.crop(region)
            #������к��ͼƬ
            crop_img.save(self.outfile)
        elif x < y:
            region = (0, int(y/2-x/2), x, int(y/2+x/2))
            #����ͼƬ
            crop_img = im.crop(region)
            #������к��ͼƬ
            crop_img.save(self.outfile)

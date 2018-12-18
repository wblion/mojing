#!/usr/bin/python
#-*- coding=utf-8 -*-
import os
class Config(object):
    APP_ID= '14482581'
    API_KEY= 'CB5qHm5bZnnS3cnvQpjfSWRh'
    SECRET_KEY= 'QpOZGI667BvBaGr27DrGfispsaqTpG2X'
    TU_LING_KEY= "b0b7b615e0b949728dd98ecfb7896b9a"

    mijing_mode = "/home/pi/share/code/mojing/util/snowboy/resources/mojing.pmdl"
    snowboy_mode = "/home/pi/share/code/mojing/util/snowboy/resources/snowboy.umdl"
    audio = r"/home/pi/share/code/tmp/auido.mp3"
    listen_voice_path=r"/home/pi/share/code/tmp/record.wav"
    ao_voice_path = r"/home/pi/share/code/mojing/util/snowboy/resources/ao.mp3"
    nihao_voice_path = r"/home/pi/share/code/mojing/util/snowboy/resources/nihao.mp3"
    wahaha_voice_path = r"/home/pi/share/code/mojing/util/snowboy/resources/wahaha.mp3"
    en_voice_path = r"/home/pi/share/code/mojing/util/snowboy/resources/en.mp3"
    all_return_voice=[ao_voice_path,wahaha_voice_path,nihao_voice_path,en_voice_path]
    #custom=u"当然是你了，你自己啥样，自己没有一点B数么，哈哈哈"
    custom=""



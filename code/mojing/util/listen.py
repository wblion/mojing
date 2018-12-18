#-*- coding=utf-8 -*-

import mojing.env.Config as Config
reload(Config)
import os
def go_listen():
    listen_voice_path = Config.Config.listen_voice_path
    os.system('arecord -f S16_LE -d 2 -r 16000 %s' % (listen_voice_path))

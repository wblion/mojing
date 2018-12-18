#-*- coding=utf-8 -*-
import sys
sys.path.append(r"/home/pi/share/code")
import mojing.env.Config as Config
reload(Config)
import mojing.util.snowboy.wb_demo as wb_demo
try:
    import mojing.util.listen as listen
    reload(listen)
    import pyaudio
except:
    print "ops"

import os
import time
#import mp3play
import requests
from json import loads
import json
from aip import AipSpeech

import time
import wave
import contextlib
import random

audio=Config.Config.audio
listen_voice_path=Config.Config.listen_voice_path
ll_voice_paths=Config.Config.all_return_voice

#@@fname = '/tmp/test.wav'
def get_wav_time(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration =float(frames / float(rate))
        print(duration)
        return duration

# def play_audio_file(fname):
#     CHUNK_SIZE = 1024
#     FORMAT = pyaudio.paInt16
#     RATE = 16000
#
#     p = pyaudio.PyAudio()
#     output = p.open(format=FORMAT,
#                             channels=1,
#                             rate=RATE,
#                             output=True) # frames_per_buffer=CHUNK_SIZE
#     with open(fname, 'rb') as fh:
#         while fh.tell() != "FILE_SIZE": # get the file-size from the os module
#             AUDIO_FRAME = fh.read(CHUNK_SIZE)
#             output.write(AUDIO_FRAME)

def play_audio_file(fname):
    """Simple callback function to play a wave file. By default it plays
    a Ding sound.

    :param str fname: wave file name
    :return: None
    """

    print fname
    ding_wav = wave.open(fname, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(), input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    play_time = get_wav_time(fname)
    time.sleep(play_time)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()




def speak_word(word_text):
    cover2mps(word_text)
    #play_audio_file(audio)
    play_mp3(audio)

def cover2mps(word_text):
    #word_text=u"你好可爱啊，可以跟我做朋友么"
    APP_ID = Config.Config.APP_ID
    API_KEY = Config.Config.API_KEY
    SECRET_KEY = Config.Config.SECRET_KEY

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result  = client.synthesis(word_text, 'zh', 1, {
        'vol': 5,"per":4,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(audio, 'wb') as f:
            f.write(result)


def play_mp3(filename):
    os.system('mpg123 %s' % (filename))


def think(text):
    #session=requests.session()
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            },
            "selfInfo": {
                "location": {
                    "city": "",
                    "province": "",
                    "street": ""
                }
            }
        },
        "userInfo": {
            "apiKey": Config.Config.TU_LING_KEY,
            "userId": "123456lll"
        }
    }
    response = requests.post(url=url, data=json.dumps(data)).json()
    final_result=think_to_text(response)
    return  final_result


def think_to_text(return_result):
    for i in return_result["results"]:
        if i["resultType"] == "text":
            word_text = i["values"]["text"]
            print word_text
            return word_text

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def voice_to_text(filePath):
    #word_text=u"你好可爱啊，可以跟我做朋友么"
    APP_ID = Config.Config.APP_ID
    API_KEY = Config.Config.API_KEY
    SECRET_KEY = Config.Config.SECRET_KEY

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result  = client.asr(get_file_content(filePath), 'wav', 16000, {'dev_pid': 1536,})
    print result["err_msg"]
    if "success" in result["err_msg"]:
        return result["result"][0]
def mode_callbacks(text,out_info):
    if text=="mojing":
        print "mojing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        xianlioao(out_info)
        pass
    if text=="snowboy":
        print "niyao gan sha !!!!!!!!"
        pass



def xianlioao(out_info):
    print "..............."
    custom=Config.Config.custom
    out_info(u".")
    huida=random.choice(ll_voice_paths)
    print huida
    play_mp3(huida)
    listen.go_listen()
    print "ting ok"
    works=voice_to_text(listen_voice_path)
    print works
    if works:
        out_info(u"我: "+works)
        print "xiang !!!!!!!!!!!!!!!!!"
        print custom
        if custom:
            out_info(u"魔镜: " + custom)
            speak_word(custom)
        else:
            final_result = think(works)
            if final_result:
                out_info(u"魔镜: " + final_result)
                speak_word(final_result)

def go(out_info):
    mijing_mode=Config.Config.mijing_mode
    snowboy_mode = Config.Config.snowboy_mode
    #mijing_mode="/home/pi/share/code/mojing/util/snowboy/resources/mojing.pmdl"
    #snowboy_mode="/home/pi/share/code/mojing/util/snowboy/resources/snowboy.umdl"
    callbacks = [lambda: mode_callbacks("mojing",out_info),
                 lambda: mode_callbacks("snowboy",out_info)]
    models=[mijing_mode,snowboy_mode]

    wb_demo.go_start(models,callbacks)


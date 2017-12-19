# -*- coding: utf-8 -*-

"""
基于PyGame的播放模块
"""
import pygame

pygame.init()

class Player(object):
    '''
    播放器实现类
    '''

    def __init__(self):
        pass

    def play(self, uri):
        '''
        播放
        :param uri:播放资源地址
        :return:
        '''
        file_path=uri.replace('file://','')
        pygame.mixer.init()
        track=pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def stop(self):
        '''
        停止
        :return:
        '''
        pygame.mixer.music.stop()

    def pause(self):
        '''
        暂停
        :return:
        '''
        pygame.mixer.music.pause()

    def resume(self):
        '''
        回复播放
        :return:
        '''
        pygame.mixer.music.play()

    def add_callback(self, name, callback):
        '''
        播放状态回调
        :param name: {eos, ...}
        :param callback: 回调函数
        :return:
        '''
        if not callable(callback):
            return

        def on_message(bus, message):
            callback()

        self.bus.connect('sync-message::{}'.format(name), on_message)

    @property
    def duration(self):
        '''
        播放时长
        :return:
        '''
        pass

    @property
    def position(self):
        '''
        播放位置
        :return:
        '''
        pass

    @property
    def state(self):
        '''
        播放状态
        :return:
        '''
        # GST_STATE_VOID_PENDING        no pending state.
        # GST_STATE_NULL                the NULL state or initial state of an element.
        # GST_STATE_READY               the element is ready to go to PAUSED.
        # GST_STATE_PAUSED              the element is PAUSED, it is ready to accept and process data.
        #                               Sink elements however only accept one buffer and then block.
        # GST_STATE_PLAYING             the element is PLAYING, the GstClock is running and the data is flowing.
        if pygame.mixer.music.get_busy():
            return 'PLAYING'
        else:
            return 'FINISHED'

if __name__=='__main__':
    player=Player()
    player.play('./du.mp3')
    while 1:
        pass

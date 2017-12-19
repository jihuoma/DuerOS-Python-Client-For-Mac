# -*- coding: utf-8 -*-

"""
基于sox的播放模块
"""
import os


class Player(object):
    '''
    播放器实现类
    '''

    def __init__(self):
        self.uri = ''
        # self.player = Gst.ElementFactory.make("playbin", "player")

        # self.bus = self.player.get_bus()
        # self.bus.add_signal_watch()
        # self.bus.enable_sync_message_emission()
        # self.bus.connect('sync-message::eos', self.on_eos)

    def play(self, uri):
        '''
        播放
        :param uri:播放资源地址
        :return:
        '''
        self.uri = uri
        self.state_str = 'PLAYING'
        file_path = uri.replace('file://', '')
        play_params = ['play', file_path,'&']
        cmd = ' '.join(play_params)
        os.system(cmd)
        self.state_str = 'FINISHED'

    def stop(self):
        '''
        停止
        :return:
        '''
        #os.system('pkill play')
        self.state_str = 'FINISHED'

    def pause(self):
        '''
        暂停
        :return:
        '''
        #os.system('pkill play')
        self.state_str = 'FINISHED'

    def resume(self):
        '''
        回复播放
        :return:
        '''
        self.play(self.uri)

    def add_callback(self, name, callback):
        '''
        播放状态回调
        :param name: {eos, ...}
        :param callback: 回调函数
        :return:
        '''
        pass
        # if not callable(callback):
        #     return

        # def on_message(bus, message):
        #     callback()

        # self.bus.connect('sync-message::{}'.format(name), on_message)

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
        return self.state_str

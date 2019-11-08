# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov  1 2019)
## 片场素材整理助手 Clapperboard Info 0.1 beta by 关键帧 Daniel
##

###########################################################################
import os
import wx
import wx.xrc
from aip import AipSpeech
from ffmpy3 import FFmpeg
import ffmpeg
import sys
class Main_Frame ( wx.Frame ):
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY , title=u"片场素材整理助手 Clapperboard Info 0.1 beta" ,
                            pos=wx.DefaultPosition , size=wx.Size ( 700 , 600 ) ,
                            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHints ( wx.DefaultSize , wx.DefaultSize )
        self.SetForegroundColour ( wx.SystemSettings.GetColour ( wx.SYS_COLOUR_INACTIVEBORDER ) )
        self.SetBackgroundColour ( wx.SystemSettings.GetColour ( wx.SYS_COLOUR_GRAYTEXT ) )

        self.m_menubar1 = wx.MenuBar ( 0 )
        self.SetMenuBar ( self.m_menubar1 )

        Grid_main = wx.GridSizer ( 0 , 1 , 0 , 0 )

        box_lift = wx.BoxSizer ( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap ( self , wx.ID_ANY , wx.Bitmap ( u"top.jpg" , wx.BITMAP_TYPE_ANY ) ,
                                           wx.DefaultPosition , wx.DefaultSize , 0 )
        box_lift.Add ( self.m_bitmap1 , 0 , wx.ALL | wx.EXPAND , 5 )

        self.text_selectvideo_dir = wx.StaticText ( self , wx.ID_ANY , u"选择视频素材所在的文件夹 (Select Folder)" ,
                                                    wx.DefaultPosition , wx.DefaultSize , 0 )
        self.text_selectvideo_dir.Wrap ( -1 )

        self.text_selectvideo_dir.SetForegroundColour ( wx.Colour ( 255 , 255 , 255 ) )

        box_lift.Add ( self.text_selectvideo_dir , 0 , wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5 )

        box_Lift = wx.BoxSizer ( wx.VERTICAL )

        self.videofootage_dirPicker = wx.DirPickerCtrl ( self , wx.ID_ANY , wx.EmptyString , u"Select a folder" ,
                                                         wx.DefaultPosition , wx.DefaultSize , wx.DIRP_DEFAULT_STYLE )
        box_Lift.Add ( self.videofootage_dirPicker , 0 , wx.ALL | wx.EXPAND , 5 )

        self.staticline_dirpiker = wx.StaticLine ( self , wx.ID_ANY , wx.DefaultPosition , wx.DefaultSize ,
                                                   wx.LI_HORIZONTAL )
        box_Lift.Add ( self.staticline_dirpiker , 0 , wx.EXPAND | wx.ALL , 5 )

        box_mid1 = wx.BoxSizer ( wx.VERTICAL )

        self.text_selectaudio_dir = wx.StaticText ( self , wx.ID_ANY , u"选择音频素材所在的文件夹 (Select Folder)" ,
                                                    wx.DefaultPosition , wx.DefaultSize , 0 )
        self.text_selectaudio_dir.Wrap ( -1 )

        self.text_selectaudio_dir.SetForegroundColour ( wx.Colour ( 100 , 177 , 255 ) )

        box_mid1.Add ( self.text_selectaudio_dir , 0 , wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5 )

        self.audiofootage_dirPicker = wx.DirPickerCtrl ( self , wx.ID_ANY , wx.EmptyString , u"Select a folder" ,
                                                         wx.DefaultPosition , wx.DefaultSize , wx.DIRP_DEFAULT_STYLE )
        box_mid1.Add ( self.audiofootage_dirPicker , 0 , wx.ALL | wx.EXPAND , 5 )

        box_mid2 = wx.BoxSizer ( wx.VERTICAL )

        grid_mid_a = wx.GridSizer ( 0 , 5 , 0 , 0 )

        box_a_01 = wx.BoxSizer ( wx.VERTICAL )

        grid_mid_a.Add ( box_a_01 , 1 , wx.EXPAND , 5 )

        self.videolist_button = wx.Button ( self , wx.ID_ANY , u"预处理视频 \nPreprocessing video" , wx.DefaultPosition ,
                                            wx.DefaultSize , 0 )
        grid_mid_a.Add ( self.videolist_button , 0 , wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL ,
                         5 )

        box_a_02 = wx.BoxSizer ( wx.VERTICAL )

        grid_mid_a.Add ( box_a_02 , 1 , wx.EXPAND , 5 )

        self.audiolist_button = wx.Button ( self , wx.ID_ANY , u"预处理音频 \nPreprocessing audio" , wx.DefaultPosition ,
                                            wx.DefaultSize , 0 )
        grid_mid_a.Add ( self.audiolist_button , 0 , wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL ,
                         5 )

        box_a_03 = wx.BoxSizer ( wx.VERTICAL )

        grid_mid_a.Add ( box_a_03 , 1 , wx.EXPAND , 5 )

        box_mid2.Add ( grid_mid_a , 1 , wx.EXPAND , 5 )

        box_mid1.Add ( box_mid2 , 1 , wx.EXPAND , 5 )

        box_Lift.Add ( box_mid1 , 1 , wx.EXPAND , 5 )

        box_b_02 = wx.BoxSizer ( wx.VERTICAL )

        self.staticline_b02 = wx.StaticLine ( self , wx.ID_ANY , wx.DefaultPosition , wx.DefaultSize ,
                                              wx.LI_HORIZONTAL )
        box_b_02.Add ( self.staticline_b02 , 0 , wx.EXPAND | wx.ALL , 5 )

        self.SelectExportFolder = wx.StaticText ( self , wx.ID_ANY , u"选择保存列表的路径 (Select Folder)" , wx.DefaultPosition ,
                                                  wx.DefaultSize , 0 )
        self.SelectExportFolder.Wrap ( -1 )

        self.SelectExportFolder.SetForegroundColour ( wx.Colour ( 128 , 255 , 0 ) )

        box_b_02.Add ( self.SelectExportFolder , 0 , wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5 )

        self.export_dirPicker = wx.DirPickerCtrl ( self , wx.ID_ANY , wx.EmptyString , u"Select a folder" ,
                                                   wx.DefaultPosition , wx.DefaultSize , wx.DIRP_DEFAULT_STYLE )
        box_b_02.Add ( self.export_dirPicker , 0 , wx.ALL | wx.EXPAND , 5 )

        box_b_03 = wx.BoxSizer ( wx.VERTICAL )

        self.export_button = wx.Button ( self , wx.ID_ANY , u"识别并导出 Identify and export" , wx.DefaultPosition ,
                                         wx.DefaultSize , 0 )
        box_b_03.Add ( self.export_button , 0 , wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND , 5 )

        self.about_button = wx.Button ( self , wx.ID_ANY , u"清空临时文件" , wx.DefaultPosition , wx.DefaultSize , 0 )
        box_b_03.Add ( self.about_button , 0 , wx.ALL | wx.EXPAND , 5 )

        box_b_02.Add ( box_b_03 , 1 , wx.EXPAND , 5 )

        box_Lift.Add ( box_b_02 , 1 , wx.EXPAND , 5 )

        box_lift.Add ( box_Lift , 1 , wx.EXPAND , 5 )

        Grid_main.Add ( box_lift , 1 , wx.EXPAND , 5 )

        self.SetSizer ( Grid_main )
        self.Layout ( )
        self.m_statusBar3 = self.CreateStatusBar ( 1 , wx.STB_SIZEGRIP , wx.ID_ANY )

        self.Centre ( wx.BOTH )

        # Connect Events
        self.videofootage_dirPicker.Bind ( wx.EVT_DIRPICKER_CHANGED , self.footage_dirPickerOnDirChanged )
        self.audiofootage_dirPicker.Bind ( wx.EVT_DIRPICKER_CHANGED , self.audiofootage_dirPickerOnDirChanged )
        self.videolist_button.Bind ( wx.EVT_BUTTON , self.videolist_buttonOnButtonClick )
        self.audiolist_button.Bind ( wx.EVT_BUTTON , self.audiolist_buttonOnButtonClick )
        self.export_dirPicker.Bind ( wx.EVT_DIRPICKER_CHANGED , self.export_dirPickerOnDirChanged )
        self.export_button.Bind ( wx.EVT_BUTTON , self.export_buttonOnButtonClick )
        self.about_button.Bind ( wx.EVT_BUTTON , self.about_buttonOnButtonClick )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def footage_dirPickerOnDirChanged(self , event):
        event.Skip ( )

    def audiofootage_dirPickerOnDirChanged(self , event):
        event.Skip ( )

    def videolist_buttonOnButtonClick(self , event):
        def mkdir_va_output():
            existence1 = os.path.exists ( output_clip )
            existence2 = os.path.exists ( output_audio )
            if existence1 and existence2:  # 两者都存在
                print ( '目录已存在,即将保存！' )
                return True
            elif existence1 and not existence2:  # 只存在output_clip
                os.makedirs ( output_audio )  # 创建目录output_audio
                print ( '只存在output_clip！创建目录output_audio' )
                return True
            elif existence2 and not existence1:  # 只存在output_clip
                os.makedirs ( output_clip )  # 创建目录output_audio
                print ( '只存在output_audio！创建目录output_cilp' )
                return True
            elif not existence1 and existence2:  # 两个目录都不存在
                os.makedirs ( output_audio )  # 创建目录output_audio
                os.makedirs ( output_clip )  # 创建目录output_clip
                print ( '创建片段存放目录' )
                return True
            else:
                os.makedirs ( output_audio )  # 创建目录output_audio
                os.makedirs ( output_clip )  # 创建目录output_clip
                print ( '目录都已存在,即将保存！' )
            return False

        output_clip = r'C:/output_clip'
        output_audio = r'C:/output_audio'
        mkdir_va_output ( )
        print ( '完成' )
        self.dir_video = self.videofootage_dirPicker.GetPath ( )
        filepath_in = self.dir_video  # 待转换文件路径
        output_clip_dir = r'C:/output_clip'  # 输出片段路径
        file_Suffix = [ '.mp4' , '.MP4' , '.mov' , '.MOV' , '.mts' , '.MTS' , '.XMF' , '.xmf' ]

        file_names = [ name for name in os.listdir ( self.dir_video ) for item in file_Suffix if
                       os.path.splitext ( name ) [ 1 ] == item ]

        for i in range ( len ( file_names ) ):
            change_file = filepath_in + "\\" + file_names [ i ]
            output_file = output_clip_dir + "\\" + file_names [ i ].replace ( '.mp4' , '.MP4' ).replace ( '.mov' ,
                                                                                                          '.MP4' ).replace (
                '.mts' , '.MP4' )
            ff = FFmpeg ( inputs={change_file: None} ,
                          outputs={output_file: ' -y  -ss  00:00:00 -t  00:00:10 -c copy'} )
            print ( ff.cmd )
            ff.run ( )


        def videocilp_wav():
            output_clip_dir = r'C:/output_clip'  # 已输出片段路径
            wav_path_dir = r'C:/output_audio'  # 待转换音频输出的路径
            file_Suffix = [ '.mp4' , '.MP4' ]
            wav_file_names = [ name for name in os.listdir ( output_clip_dir )
                               for item in file_Suffix
                               if os.path.splitext ( name ) [ 1 ] == item ]
            for j in range ( len ( wav_file_names ) ):
                videocilp_name = output_clip_dir + "/" + wav_file_names [ j ]
                wav_output_file = wav_path_dir + "/" + wav_file_names [ j ].replace ( '.MP4' , '.wav' )
                probe = ffmpeg.probe ( videocilp_name )
                audio_stream = next ( (stream for stream in probe [ 'streams' ] if stream [ 'codec_type' ] == 'audio') ,
                                      None )
                if audio_stream is None:
                    print ( 'No audio stream found' , file=sys.stderr )
                else:
                    aa = FFmpeg (
                        inputs={videocilp_name: None} ,
                        outputs={wav_output_file: '-y -vn -ar 16000  -ab 192 -ac 1 -f wav'}
                    )
                    print ( aa.cmd )
                    aa.run ( )
                    print ( '转换完成' )

        videocilp_wav()
        event.Skip ( )

    def audiolist_buttonOnButtonClick(self , event):
        self.dir_audio = self.audiofootage_dirPicker.GetPath ( )
        wav_path_dir = r'C:/output_audio'  # 音频输出的路径
        file_Suffix = [ '.wav' , '.WAV' ]
        wav_file_names = [ name for name in os.listdir ( self.dir_audio )
                           for item in file_Suffix
                           if os.path.splitext ( name ) [ 1 ] == item ]
        for j in range ( len ( wav_file_names ) ):
            videocilp_name = self.dir_audio + "/" + wav_file_names [ j ]
            wav_output_file = wav_path_dir + "/" + wav_file_names [ j ].replace ( '.wav' , '.wav' )
            aa = FFmpeg (
                inputs={videocilp_name: None} ,
                outputs={wav_output_file: '-y -vn -ar 16000 -ab 192 -ac 1 -aframes 1000'}
            )
            print ( aa.cmd )
            aa.run ( )
            print ( '转换完成' )
        event.Skip ( )

    def export_dirPickerOnDirChanged(self , event):
        event.Skip ( )

    def export_buttonOnButtonClick(self , event):

        # 从百度AI开放平台创建应用处获取
        APP_ID = '17675420'
        API_KEY = 'EXBpFXF6Y90FjknjKXdsza1z'
        SECRET_KEY = 'fKzClqKpu8oNLKE3PaBTxhdFruDkMxwS'

        client = AipSpeech ( APP_ID , API_KEY , SECRET_KEY )
        file_Path = r'C:/output_audio/'


        def get_file_content(file_Path):
            with open ( file_Path , 'rb' ) as fp:
                return fp.read ( )

        self.dir = self.export_dirPicker.GetPath ( )
        f = open ( self.dir + "\\" + "文件内容识别结果.txt" , "a+" )
        print ( str ( '音频片段位置' ) + ' ' + str ( file_Path ) , file=f )
        file_Suffix = [ '.wav' ]
        wav_file_names = [ name for name in os.listdir ( file_Path )
                           for item in file_Suffix
                           if os.path.splitext ( name ) [ 1 ] == item ]
        for j in range ( len ( wav_file_names ) ):
            change_file = file_Path + "/" + wav_file_names [ j ]
            result = client.asr ( get_file_content ( change_file ) , 'wav' , 16000 , {'dev_pid': 1536 , } )
            text_error = result [ 'err_no' ]

            f = open (self.dir + "\\" + "文件内容识别结果.txt" , "a+" )
            if text_error == 3300:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*输入参数不正确*' , file=f )
            elif text_error == 3301:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*音频质量过差*' , file=f )

            elif text_error == 3302:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*鉴权失败*' , file=f )

            elif text_error == 3303:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*语音服务器后端问题*' , file=f )

            elif text_error == 3304:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*用户的请求QPS超限*' , file=f )

            elif text_error == 3305:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*用户的日pv（日请求量）超限*' , file=f )

            elif text_error == 3307:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*语音服务器后端识别出错问题*' , file=f )

            elif text_error == 3308:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*音频过长*' , file=f )

            elif text_error == 3309:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*输入参数不正确*' , file=f )
                print ( '*音频数据问题*' )
            elif text_error == 3310:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*输入的音频文件过大*' , file=f )

            elif text_error == 3311:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*采样率rate参数不在选项里*' , file=f )

            elif text_error == 3312:
                print ( str ( wav_file_names [ j ] ) + ' ' + '*音频格式format参数不在选项里*' , file=f )

            elif text_error == 0:
                TEXT = (result [ 'result' ] [ 0 ])
                print ( file_Path )
                print (wav_file_names [ j ] )
                print ( TEXT )
                print (str ( wav_file_names [j] ) + ' ' + str ( TEXT ) , file=f)
                event.Skip ( )


    def about_buttonOnButtonClick(self , event):
        os.chdir ( 'C:/output_audio' )
        for i in os.listdir ('C:/output_audio'):
            if i.endswith ('.wav'):
                os.remove ( i )
        os.chdir ('C:/output_clip')
        for z in os.listdir ('C:/output_clip'):
            if z.endswith ('.MP4'):
                os.remove (z)
        print('临时文件已清空')
        event.Skip ( )

class App ( wx.App ) :
    def OnInit(self) :
        frame = Main_Frame ( None )  # calss
        frame.Show ( )
        return True


app = App ( )
app.MainLoop ( )
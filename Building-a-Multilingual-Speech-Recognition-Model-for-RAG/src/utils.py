import sys
import os
import uuid
from moviepy.editor import *

AUDIO_FOLDER_PATH = "..\audios"
VIDEO_FOLDER_PATH = "..\videos"


def getAudio(self, videoPath):
    """
         This method takes video and extract audio from it

         videoPath -> Name of video from which audio is to be extracted.Video must be in Video Folder. 
    """
    try:
        audioFile = videoPath.split(".")[0]+".wav"
        audioPath = os.path.join(
            AUDIO_FOLDER_PATH, audioFile)

        video = VideoFileClip(videoPath)

        audio = video.audio

        audio.write_audiofile(audioPath)

        return audioPath
    except Exception as e:
        print("Exception Occured in getAudio method :", e)


def saveAudio(self, audio_file):
    """
        This method saves a audioFile in system and returns saved address

        audio_file-> Audio file recieved in the method
    """
    try:
        fileName = uuid.uuid4()+".wav"
        audioFilePath = os.path.join(AUDIO_FOLDER_PATH, fileName)
        audio_file.save(audioFilePath)
        return audioFilePath
    except Exception as e:
        print("Exception occured at saveAudio method ", e)


def saveVideo(self, video_file):
    """
        This method saves a videoFile in system and returns saved address

        video_file-> Video file recieved in the method
    """
    try:
        fileName = uuid.uuid4()+".mp4"
        videoFilePath = os.path.join(VIDEO_FOLDER_PATH, fileName)
        video_file.save(videoFilePath)
        return videoFilePath
    except Exception as e:
        print("Exception occured at saveAudio method ", e)

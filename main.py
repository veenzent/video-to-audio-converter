from moviepy.editor import *
from datetime import datetime

def mp4_to_mp3_converter(mp4: str, mp3: str):
    """
    Convert mp4 to mp3
    
    :param mp4: path to mp4 file
    :type mp4: str
    :param mp3: path to save converted mp3 file
    :type mp3: str
    """
    video = VideoFileClip(mp4)

    # extract audio from video
    video.audio.write_audiofile(mp3)
    return


mp4 = "C:/Users/veen_zent/Downloads/Video/2 HOURS EARLY MORNING SPONTENEOUS WORSHIP -- THEOPHILUS SUNDAY.mp4"    # "path/to/video/file.mp4"
mp3 = "C:/Users/veen_zent/Downloads/Video/2 HOURS EARLY MORNING SPONTENEOUS WORSHIP -- THEOPHILUS SUNDAY.mp3"  # "path/to/save/audio/file.mp3"

mp4_to_mp3_converter(mp4, mp3)
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import argparse




def MakeClip(_video,_mins,_seconds,_length):
    targetname = _video.split(".")[0] + "_cut_S_" + (str)((_mins * 60) + _seconds) +  "_L_" +(str)(_length) + ".mkv"
    ffmpeg_extract_subclip(_video,((_mins * 60) + _seconds) ,((_mins * 60) + _seconds) + _length,targetname)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='video name, mins, seconds, length')
    parser.add_argument('name',help='Video name and file ext')

    parser.add_argument('minute', type=int, help='minutes timestamp to start the clip')

    parser.add_argument('second', type=int, help='seconds timestamp to start the clip')
    
    parser.add_argument('length', type=int, help='length of the new clip')


                    
    args = parser.parse_args()

    

    MakeClip(args.name,args.minute,args.second,args.length)
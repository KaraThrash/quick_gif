from moviepy.editor import * 
import argparse


def MakeAGif(_video,_mins,_seconds,_length,_fps,_resize):

    clip = VideoFileClip(_video).subclip( ((_mins * 60) + _seconds) ,((_mins * 60) + _seconds) + _length).resize(_resize)
    clip.write_gif(_video.split(".")[0] + "_gif.gif", _fps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='video name, START:mins, START:seconds, gif length, fps, scale')
    parser.add_argument('filepath')
    parser.add_argument('floats', type=float, nargs='+')
    args = parser.parse_args()

    if len(args.floats) > 2:
        

        videoFilePath = args.filepath
        minute = args.floats[0]
        second = args.floats[1]
        length = args.floats[2]

        fps = 8 
        rescale = .5
        if len(args.floats) > 3:
            fps = args.floats[3]
        if len(args.floats) > 4:
            rescale = args.floats[4]

        MakeAGif(videoFilePath,minute,second,length,fps,rescale)

    
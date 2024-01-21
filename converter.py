from moviepy.editor import VideoFileClip
import numpy as np

from PIL import Image

def resize_clip(clip, height, method):
    def resize(img):
        img_pil = Image.fromarray(img)
        img_resized = img_pil.resize((int(img.shape[1] * height / img.shape[0]), height), resample=method)
        return np.array(img_resized)
    
    return clip.fl_image(resize)

def convert_avi_to_mkv_fast(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4)


def convert_avi_to_mkv_slow(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    # video_clip_resized = resize_clip(video_clip, height=2160, method=Image.BICUBIC)  # Ou use Image.
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", bitrate="30M", preset="slow", threads=4)
    # video_clip_resized.write_videofile(output_file, codec="libx264", audio_codec="aac", bitrate="30M", preset="slow", threads=4)



# if __name__ == "__main__":
#     input_video = "./Homem.Aranha.E01.Noite.Do.Lagarto.avi"
#     output_video = "./Homem.Aranha.E01.Noite.Do.Lagarto_4k.mkv"

#     convert_avi_to_mkv(input_video, output_video)

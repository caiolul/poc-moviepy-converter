from moviepy.editor import VideoFileClip
import numpy as np
from moviepy.video.fx.all import colorx
from PIL import Image


def resize_clip(clip, height, upscale, method, size_default=None):
    def resize(img):
        img_pil = Image.fromarray(img)
        if size_default is not None:
            size = size_default
        else:
            if upscale == True:
                size = (int(img.shape[1] * height / img.shape[0]), height)
            else:
                size = (int(img.shape[1] / (img.shape[0] / height)), height)

        img_resized = img_pil.resize(size, resample=method)
        return np.array(img_resized)

    return clip.fl_image(resize)


def convert_avi_to_mkv_fast(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    video_clip.write_videofile(
        output_file, codec="libx264", audio_codec="aac", preset="ultrafast", threads=4
    )


def convert_avi_to_mkv_slow(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    # video_clip_resized = resize_clip(video_clip, height=2160, method=Image.BICUBIC)  # Ou use Image.
    video_clip.write_videofile(
        output_file,
        codec="libx264",
        audio_codec="aac",
        bitrate="30M",
        preset="slow",
        threads=4,
    )
    # video_clip_resized.write_videofile(output_file, codec="libx264", audio_codec="aac", bitrate="30M", preset="slow", threads=4)


def improve_quality_test(input_file, output_file):
    clip = VideoFileClip(input_file)
    # Configs de contrate e brilho
    clip = colorx(clip, factor=1.5)  # Fator de contraste
    clip = clip.fx(lambda c: c.fl_image(lambda frame: frame * 1.2))  # Ajuste de brilho

    # Ajuste de cor
    clip = clip.fx(colorx, factor=1.5)

    # Filtro de nitidez
    clip = resize_clip(clip, height=1080, upscale=True, method=Image.BICUBIC)
    clip = resize_clip(clip, height=480, upscale=False, method=Image.BICUBIC)
    clip = resize_clip(
        clip, height=None, upscale=True, method=Image.BICUBIC, size_default=clip.size
    )
    clip.write_videofile(
        output_file,
        codec="libx264",
        audio_codec="aac",
        bitrate="30M",
        preset="slow",
        threads=4,
    )

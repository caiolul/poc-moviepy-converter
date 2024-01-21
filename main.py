import os
from converter import convert_avi_to_mkv_slow

if __name__ == "__main__":
    folder_videos = input("Digite o caminho da pasta: ")

    filenames = [file for file in os.listdir(folder_videos) if file.endswith(".avi")]

    for name in filenames:
        input_video = os.path.join(folder_videos, name)
        output_video = os.path.join(folder_videos, name[:-4] + ".mkv")
        print(input_video, output_video)
        convert_avi_to_mkv_slow(input_video, output_video)

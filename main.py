import os
from converter import (
    convert_avi_to_mkv_slow,
    convert_avi_to_mkv_fast,
    improve_quality_test,
)

if __name__ == "__main__":
    folder_videos = input("Digite o caminho da pasta: ")
    # folder_videos = """D:\Homem Aranha avi\teste_converter"""
    print("Selecione uma das opções abaixo:")
    print("1 - Converter para MKV com qualidade alta")
    print("2 - Converter para MKV com qualidade baixa")
    print("3 - Melhorar a qualidade do vídeo")
    option = input("Opção: ")
    filenames = [file for file in os.listdir(folder_videos) if file.endswith(".avi")]

    for name in filenames:
        input_video = os.path.join(folder_videos, name)
        output_video = os.path.join(folder_videos, name[:-4] + ".mkv")
        print(input_video, output_video)
        if option == "1":
            convert_avi_to_mkv_slow(input_video, output_video)
        elif option == "2":
            convert_avi_to_mkv_fast(input_video, output_video)
        elif option == "3":
            improve_quality_test(input_video, output_video)

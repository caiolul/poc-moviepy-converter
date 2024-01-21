.PHONY: run_converter

run_converter:
    @read -p "Digite o caminho da pasta: " folder_videos; \
    python main.py "$$folder_videos"

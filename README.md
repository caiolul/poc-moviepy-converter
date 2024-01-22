# AVI to MKV Video Converter

## Description

This project is a Python script that converts videos from AVI to MKV format using the MoviePy library.

## Requirements

- Python 3.11.6
- Necessary Python libraries (refer to the requirements.txt file)

## Installation

1. Clone the repository:

```bash
git clone git@github.com:caiolul/poc-moviepy-converter.git
```
   
   
2. Install the necessary libraries:

```bash
 pip install -r requirements.txt
 ```
 
## Usage

1. Run the script:

```bash
python main.py
```
2. Specify the path to the folder containing the AVI videos.

```bash
Enter the path to the folder containing the AVI videos: 
```

3. Select the conversion settings.

```bash
Select the conversion settings:
1 - Convert with higth quality but slower
2 - Convert with medium quality but faster
3 - Improve the quality of the video (WIP)

```
This will prompt you to enter the path to the folder containing AVI videos.

The converted videos will be saved in the same directory with the MKV extension.

If you wish to change the conversion settings, update the `converter.py` file with your configurations

# Project Structure

- main.py: Main Python script.
- converter.py: Module containing conversion functions.
- Makefile: Configuration file for make.


# Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.
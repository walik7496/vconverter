# Video Converter App

A simple graphical user interface (GUI) for converting video files using `ffmpeg`. This app allows users to select a video file, specify an output extension, and start the conversion process. It supports a variety of video formats and tracks the conversion progress with a progress bar.

## Features

- **Input File Selection**: Choose a video file using a file dialog.
- **Output Extension**: Enter the desired output file extension (e.g., `.mp4`, `.avi`).
- **Conversion Progress**: View the conversion progress in real-time.
- **Abort Conversion**: Stop the conversion process at any time.
- **Supported Formats**: The app supports a wide range of video formats, including `.mp4`, `.avi`, `.mov`, `.mkv`, and more.

## Requirements

- **Python 3.x** (Tested on Python 3.7+)
- **FFmpeg**: Ensure `ffmpeg` is installed and available in your system's PATH. You can download it from [here](https://ffmpeg.org/download.html).

## Installation

1. Install Python 3.x: [Download Python](https://www.python.org/downloads/)
2. Install the required Python libraries using `pip`:

   ```bash
   pip install tkinter
   ```
3. Download ffmpeg.exe from FFmpeg Official Website and make sure it is accessible via your system's PATH. You can also place the ffmpeg.exe file in the same directory as this script.

## Usage

1. Run the `video_converter.py` script.
2. In the GUI, click **Select** to choose an input video file.
3. Enter the desired output extension (e.g., `.mp4`, `.avi`) in the **Output extension** field.
4. Click **Convert** to start the conversion process.
5. The progress bar will update in real-time. Once the conversion is complete, you will see a message in the status text area.
6. If needed, click **Break** to stop the conversion process.

## Code Explanation

- **File Dialog**: Used for selecting the input video file.
- **Progress Bar**: Tracks the conversion progress by reading the output from the `ffmpeg` command.
- **FFmpeg**: Handles the actual video conversion process. The app calls `ffmpeg` with the selected input file and desired output format.

## Troubleshooting

- **Missing `ffmpeg`**: If `ffmpeg` is not installed or not accessible from the command line, you will see an error. Ensure `ffmpeg` is installed and added to your system's PATH.
- **Unsupported Formats**: If the selected file format is not supported, you will receive an error message. Make sure the file you select is a supported video format.
- **Progress Bar Not Updating**: Ensure that `ffmpeg` is outputting the progress information correctly. If the progress bar is not updating, check that your `ffmpeg` version supports real-time conversion monitoring.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

If you have any questions or need further assistance, feel free to open an issue or reach out directly to the repository owner.

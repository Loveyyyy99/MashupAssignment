# Mashup Generator - Project Documentation

## Overview

The Mashup Generator is a Python-based audio processing application that automatically creates mashups from YouTube videos of one or more artists. The system provides both a command-line interface and a web-based interface for user interaction.

## Methodology

The Mashup Generator follows a modular pipeline-based approach consisting of six main steps:

### Step 1: Input Collection

The user provides the following information:
- Singer name (single or multiple artists)
- Number of videos to process
- Duration per track (in seconds)
- Email address (for web version only)

### Step 2: Video Downloading

- The program uses `yt-dlp` to search YouTube for videos
- Downloads the specified number of videos for the given artist(s)
- Files are stored in the `cli/downloads/` directory

### Step 3: Audio Extraction and Cutting

- `FFmpeg` is used to extract audio from downloaded videos
- Only the first N seconds (user-defined duration) are retained from each video
- Each audio clip is re-encoded to ensure proper timestamps
- Output files are saved in the `cli/cut_audios/` directory

### Step 4: Audio Merging

- All clipped MP3 files are merged using FFmpeg
- Re-encoding is performed to avoid DTS (Decode Time Stamp) errors
- Final mashup file is saved as `cli/final_output/mashup.mp3`

### Step 5: Email Delivery (Web Version)

- The final MP3 file is compressed into a ZIP archive
- The ZIP file is sent to the user's email using Gmail SMTP
- Environment variables are used for secure credential management

### Step 6: UI Feedback

The web interface provides real-time feedback:
- Loading spinner during processing
- Success message upon completion
- Error messages if any issues occur

## Project Description

The Mashup Generator is designed with modularity in mind, providing flexibility in how users interact with the system.

### Key Features

- **Dual Interface**: Command Line Interface (CLI) and web-based interface using Flask
- **Automatic Processing**: Downloads, extracts, cuts, and merges audio automatically
- **Email Delivery**: Sends the final mashup directly to the user's email
- **User-Friendly UI**: Clean interface with visual processing indicators
- **Multi-Artist Support**: Can process videos from multiple artists simultaneously

### System Architecture

The system is organized into modular components:
- `mashup_core.py` - Core processing logic
- `cli/` - Command line version implementation
- `webapp/` - Flask web application

## Input and Output

### Input Specifications

#### CLI Version
```bash
python 102303335.py "Artist Name" 5 30 output.mp3

```
<img width="1259" height="376" alt="image" src="https://github.com/user-attachments/assets/d6ba51cb-9cb5-4626-9a47-a1838f3e7938" />

**Parameters:**
- **Artist Name** - Singer name or multiple singers separated by commas
- **5** - Number of videos to download
- **30** - Duration per track in seconds
- **output.mp3** - Output filename

#### Web Version

The web interface accepts the following fields:
- Singer Name(s)
- Number of Videos
- Duration per Track (seconds)
- Email Address

### Output Specifications

The system produces:
- Final merged MP3 file (`mashup.mp3`)
- ZIP archive (`mashup.zip`) for web version
- Email notification with attached mashup file

#### Example

**Input:**

<img width="852" height="771" alt="image" src="https://github.com/user-attachments/assets/10e55c7b-1671-4d63-98f7-8974e47fcb6e" />



**Output:**

<img width="825" height="347" alt="image" src="https://github.com/user-attachments/assets/f748cd5e-9b5c-4875-a3c1-ff73e9ff494f" />
<img width="1405" height="453" alt="image" src="https://github.com/user-attachments/assets/42431260-5231-44fe-b5f7-e9ef0d0cec61" />


## Screenshots of the Interface

1. **Figure 1**: Web Interface - Input Form

   
 <img width="852" height="771" alt="image" src="https://github.com/user-attachments/assets/4543b7cf-df0a-47c6-ac52-db1710995771" />

2. **Figure 2**: Processing Screen with Loading Indicator

   
   <img width="852" height="771" alt="image" src="https://github.com/user-attachments/assets/45a6e32c-7044-4346-bd02-ed650b006b05" />

3. **Figure 3**: Success Message after Email Sent

   
   <img width="852" height="771" alt="image" src="https://github.com/user-attachments/assets/78b208b5-0a1b-4799-8a3d-9b5d55638545" />


## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- FFmpeg installed and accessible in system PATH
- Gmail account for email functionality (web version)

### Required Python Packages
```bash
pip install yt-dlp
pip install flask
pip install python
```

## Usage

### Command Line Interface
```bash
python 102303335.py "<Artist Name>" <num_videos> <duration> <output_file>
```
<img width="1259" height="376" alt="image" src="https://github.com/user-attachments/assets/d6ba51cb-9cb5-4626-9a47-a1838f3e7938" />
<img width="1321" height="500" alt="image" src="https://github.com/user-attachments/assets/98d8f94c-1269-4313-8c0f-ce6f01060f5b" />

### Web Interface

1. Start the Flask application
2. Navigate to the web interface in your browser
3. Fill in the required fields
4. Submit the form
5. Wait for processing to complete
6. Check your email for the mashup file

## Project Structure
```
mashup-generator/
├── mashup_core.py
├── 102303335.py
├── cli/
│   ├── downloads/
│   ├── cut_audios/
│   └── final_output/
└── webapp/
    ├── app.py
    ├── templates/
    └── static/
```

## Error Handling

The system includes error handling for:
- Invalid artist names or video searches
- Network connectivity issues
- FFmpeg processing errors
- Email delivery failures
- File system operations

## Technical Dependencies

- **yt-dlp**: YouTube video downloading
- **FFmpeg**: Audio extraction, cutting, and merging
- **Flask**: Web framework
- **SMTP**: Email delivery
- **Python standard library**: File operations, process management

## License

This project is provided for educational purposes.

## Acknowledgments

- yt-dlp developers for YouTube downloading capability
- FFmpeg project for audio processing tools
- Flask framework for web interface development

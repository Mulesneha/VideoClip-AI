🎬 AI Video Shorts Generator

An AI-powered tool that converts long videos into short, engaging clips using transcription and segment detection. Built with Python, Gradio, and MoviePy.

<img width="956" height="473" alt="image" src="https://github.com/user-attachments/assets/14fff0da-bc0a-4bec-b823-db404cce78a4" />

 📁 Project Structure:
 VideoClip-AI/
│── app.py
│── requirements.txt
│── README.md
│── .venv/
│
└── outputs/
    ├── short_0.mp4
    ├── short_1.mp4
    
🚀 Features
📤 Upload long videos
🧠 AI-based transcript generation (customizable)
✂️ Automatic segment detection
🎬 Generates multiple short clips
🌐 Simple Gradio web interface
💾 Downloads output as MP4 files

🏗️ Tech Stack
Python 3.10+
Gradio
MoviePy
(Optional) Whisper / NLP model for transcription
FFmpeg

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/video-shorts-ai.git
cd video-shorts-ai
2. Create virtual environment
python -m venv .venv

Activate it:

Windows (PowerShell)
.venv\Scripts\Activate.ps1
Windows (CMD)
.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

Or manually:

pip install gradio moviepy
4. Install FFmpeg (Important ⚠️)

MoviePy requires FFmpeg.

Windows: https://ffmpeg.org/download.html
Or using chocolatey:
choco install ffmpeg
▶️ Run the project
python app.py

Then open:
http://127.0.0.1:7860

🧠 How it works
1.Upload a long video
2.The system transcribes audio → text
3.Detects important segments
4.Extracts clips using MoviePy
5.Returns top short videos

🔮 Future Improvements
🎯 AI viral moment detection (Whisper + GPT)
📱 Auto TikTok/YouTube Shorts formatting (9:16)
🔥 Face/object-based highlight detection
☁️ Cloud deployment (HuggingFace / Render)
🎵 Auto background music addition
🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

👨‍💻 Author
Sneha Mule 
Built with ❤️ using Python & AI

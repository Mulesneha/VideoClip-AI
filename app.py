import gradio as gr
from moviepy.editor import VideoFileClip

# -----------------------------
# Dummy AI functions (replace later)
# -----------------------------
def transcribe_video(video_path):
    return "This is a sample transcript with multiple interesting moments."

def detect_segments(transcript):
    # Fake segments for testing
    return [
        {"start": 0, "end": 5},
        {"start": 5, "end": 10},
        {"start": 10, "end": 15},
    ]

# -----------------------------
# Create short clip
# -----------------------------
def create_short(video_path, segment, index):
    video = VideoFileClip(video_path)

    clip = video.subclip(segment["start"], segment["end"])
    output_path = f"short_{index}.mp4"

    clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None
    )

    video.close()
    clip.close()

    return output_path

# -----------------------------
# Main function
# -----------------------------
def process_video(video_file):
    if video_file is None:
        return []

    # FIX: Gradio may return dict
    video_path = video_file["path"] if isinstance(video_file, dict) else video_file

    try:
        print("Transcribing...")
        transcript = transcribe_video(video_path)

        print("Finding segments...")
        segments = detect_segments(transcript)

        outputs = []

        for i, seg in enumerate(segments[:3]):
            print("Creating clip", i)
            path = create_short(video_path, seg, i)
            outputs.append(path)

        return outputs

    except Exception as e:
        print("ERROR:", e)
        return []

# -----------------------------
# UI
# -----------------------------
with gr.Blocks() as demo:
    gr.Markdown("# 🎬 AI Video Shorts Generator")

    video_input = gr.Video(label="Upload Video")
    btn = gr.Button("Generate Shorts")
    output = gr.Files(label="Short Clips")

    btn.click(process_video, inputs=video_input, outputs=output)

demo.launch()
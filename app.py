import os
import gradio as gr

# ----------------------------------------
# Create Short Video Function
# ----------------------------------------
def create_short(video_path, segment, index):
    from moviepy.editor import VideoFileClip

    video = VideoFileClip(video_path)

    start = segment["start"]
    end = segment["end"]

    clip = video.subclip(start, end)

    output_path = f"short_{index}.mp4"

    final = clip

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
    clip.close()

    return output_path


# ----------------------------------------
# Main Processing Function
# ----------------------------------------
def process_video(video_file):
    if video_file is None:
        return []

    # Gradio gives file path directly (usually)
    video_path = video_file

    print("Transcribing...")
    transcript = transcribe_video(video_path)

    print("Finding best moments...")
    segments = detect_segments(transcript)

    generated_clips = []

    for i, segment in enumerate(segments[:5]):
        print(f"Creating short {i + 1}")

        clip_path = create_short(video_path, segment, i)
        generated_clips.append(clip_path)

    return generated_clips


# ----------------------------------------
# Gradio UI
# ----------------------------------------
with gr.Blocks() as demo:
    gr.Markdown("# AI Video Shorts Generator")
    gr.Markdown("Upload a long video and generate AI-powered short clips.")

    video_input = gr.Video(label="Upload Video")

    generate_btn = gr.Button("Generate Shorts")

    output_files = gr.Files(label="Generated Shorts")

    generate_btn.click(
        fn=process_video,
        inputs=video_input,
        outputs=output_files
    )

demo.launch()
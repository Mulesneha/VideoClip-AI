import os

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
    final.close()

    return output_path


# ----------------------------------------
# Main Processing Function
# ----------------------------------------

def process_video(video_file):
    if video_file is None:
        return []

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

    output_gallery = gr.Files(label="Generated Shorts")

    generate_btn.click(
        fn=process_video,
        inputs=video_input,
        outputs=output_gallery
    )


demo.launch()
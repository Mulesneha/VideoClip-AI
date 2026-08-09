import streamlit as st
from moviepy import VideoFileClip
import os

st.set_page_config(
    page_title="VideoClip AI",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 VideoClip AI")
st.subheader("AI-Powered Video Shorts Generator")

st.write(
    "Upload a video and generate short clips from interesting moments."
)

video_file = st.file_uploader(
    "Upload your video",
    type=["mp4", "mov", "avi", "mkv"]
)

if video_file is not None:

    st.video(video_file)

    if st.button("🚀 Generate Shorts"):

        with st.spinner("Processing video..."):

            input_path = "input_video.mp4"

            with open(input_path, "wb") as f:
                f.write(video_file.getbuffer())

            try:
                video = VideoFileClip(input_path)

                duration = video.duration

                st.success(
                    f"Video uploaded successfully! Duration: {duration:.2f} seconds"
                )

                # Demo segments
                segments = [
                    (0, min(5, duration)),
                    (min(5, duration), min(10, duration)),
                    (min(10, duration), min(15, duration))
                ]

                for i, (start, end) in enumerate(segments):

                    if start >= duration:
                        continue

                    end = min(end, duration)

                    clip = video.subclipped(start, end)

                    output_path = f"short_{i + 1}.mp4"

                    clip.write_videofile(
                        output_path,
                        codec="libx264",
                        audio_codec="aac",
                        logger=None
                    )

                    st.write(f"### 🎞️ Short {i + 1}")

                    with open(output_path, "rb") as file:
                        st.video(file)

                        st.download_button(
                            label=f"⬇️ Download Short {i + 1}",
                            data=file,
                            file_name=output_path,
                            mime="video/mp4",
                            key=f"download_{i}"
                        )

                    clip.close()

                video.close()

            except Exception as e:
                st.error(f"Error: {e}")

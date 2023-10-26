from pytube import YouTube
import os

def download_video_and_audio(url, save_path='/home/meeseeks/Videos'):
    # Create a YouTube object with the provided URL
    yt = YouTube(url)

    # Get the highest resolution video stream
    video_stream = yt.streams.get_highest_resolution()
    # Download the video
    video_stream.download(output_path=save_path)
    print(f"Downloaded video: {yt.title} successfully!")

    # Get the audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    # Define a unique filename for the audio before downloading
    audio_filename_prefix = f"{yt.title}_audio_only"
    audio_filename = audio_stream.download(output_path=save_path, filename_prefix=audio_filename_prefix)
    # Convert the downloaded audio file to mp3
    base_audio_filename = audio_filename.rsplit(".", 1)[0]  # Remove the extension
    mp3_filename = f"{base_audio_filename}.mp3"
    os.rename(audio_filename, mp3_filename)
    print(f"Downloaded audio: {yt.title} successfully!")

if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video you want to download: ")
    download_path = input(f"Enter the path where you want to save the video and audio (or press enter for default path {download_video_and_audio.__defaults__[0]}): ")
    download_video_and_audio(video_url, download_path if download_path else download_video_and_audio.__defaults__[0])

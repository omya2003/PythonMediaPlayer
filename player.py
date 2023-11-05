import tkinter as tk
from tkinter import ttk
import vlc

# Initialize the VLC media player instance
instance = vlc.Instance("--no-xlib")

# Load the video file
media = instance.media_new("Mission_ Impossible Dead Reckoning Part 1 - Airport Nuclear Bomb Clip.mp4")  # Replace with your video file path
player = instance.media_player_new()
player.set_media(media)

# Create a window to display the video
root = tk.Tk()
root.title("Video Player")

# Set the size of the tkinter window (adjust as needed)
root.geometry("1280x720")  # Set the desired width and height

# Create a frame for the video display
video_frame = ttk.Frame(root)
video_frame.pack(fill=tk.BOTH, expand=True)

# Embed the VLC player in the video frame
player.set_hwnd(video_frame.winfo_id())

# Create a separate frame for buttons and controls
button_frame = ttk.Frame(root)
button_frame.pack(fill=tk.X)

# Play Button (using play emoji)
def play_video():
    player.play()
play_button = tk.Button(button_frame, text="▶️", command=play_video, font=("Arial", 18))
play_button.pack(side=tk.LEFT)

# Pause Button (using pause emoji)
def pause_video():
    player.pause()
pause_button = tk.Button(button_frame, text="⏸️", command=pause_video, font=("Arial", 18))
pause_button.pack(side=tk.LEFT)

# Stop Button (using stop emoji)
def stop_video():
    player.stop()
stop_button = tk.Button(button_frame, text="⏹️", command=stop_video, font=("Arial", 18))
stop_button.pack(side=tk.LEFT)


# Volume Slider
volume_scale = ttk.Scale(button_frame, from_=0, to=100, orient="horizontal", length=150)

def set_volume(val):
    volume = round(float(val))
    player.audio_set_volume(volume)

volume_scale.set(50)  # Set the initial volume level (0-100)
volume_scale.config(command=lambda val=volume_scale.get(): set_volume(val))
volume_scale.pack(side=tk.LEFT)

# Exit Button (using exit emoji)
def exit_program():
    player.stop()
    root.destroy()

exit_button = tk.Button(button_frame, text="❌", command=exit_program, font=("Arial", 18))
exit_button.pack(side=tk.LEFT)

# Video Playback Slider
def set_video_position(val):
    position = float(val) / 100
    player.set_position(position)

video_slider = ttk.Scale(button_frame, from_=0, to=100, orient="horizontal", command=set_video_position)
video_slider.pack(side=tk.LEFT, fill="x", expand=True)



root.protocol("WM_DELETE_WINDOW", exit_program)  # This line handles window close event

root.mainloop()

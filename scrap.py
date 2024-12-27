import tkinter as tk
from tkinter import messagebox
import yt_dlp as ytdlp  # Import yt-dlp

# Function to validate YouTube URL
def is_valid_youtube_url(url):
    if url.startswith('https://youtu.be/') or 'youtube.com' in url:
        return True
    return False

# Function to fetch video information using yt-dlp
def fetch_video_info():
    url = url_entry.get()
    if not is_valid_youtube_url(url):
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return
    
    # Display the loading text
    status_label.config(text="Fetching video information...", fg="blue")
    status_label.update_idletasks()  # Ensure the label gets updated immediately
    
    try:
        # Set options for yt-dlp to extract video info
        ydl_opts = {
            'quiet': True,  # Suppresses unnecessary output
            'force_generic_extractor': True,  # Forces generic extractor in case of issues
        }

        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Set download=False to just fetch info
            
            # Setting variables to display the fetched video details
            title_var.set("Title: " + info_dict.get('title', 'N/A'))
            views_var.set("Views: " + str(info_dict.get('view_count', 'N/A')))
            duration_var.set("Duration: " + str(info_dict.get('duration', 'N/A')) + " seconds")
            description_var.set("Description:\n" + (info_dict.get('description', 'No Description')[:500] + '...') if info_dict.get('description') else "Description: None")
            ratings_var.set("Ratings: " + str(info_dict.get('average_rating', 'N/A')) if info_dict.get('average_rating') else "Ratings: None")
        
        # Hide the "Fetching..." status after the information is retrieved
        status_label.config(text="Video information fetched successfully!", fg="green")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch video details. {str(e)}")
        status_label.config(text="Error fetching information.", fg="red")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Info Fetcher")

# Create and place widgets
tk.Label(root, text="Enter YouTube Video URL:").grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, pady=10, padx=10)

fetch_button = tk.Button(root, text="Fetch Info", command=fetch_video_info)
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

# StringVars for displaying fetched information
title_var = tk.StringVar()
views_var = tk.StringVar()
duration_var = tk.StringVar()
description_var = tk.StringVar()
ratings_var = tk.StringVar()

# Labels to display the fetched video details
tk.Label(root, textvariable=title_var, wraplength=600, justify=tk.LEFT).grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=views_var).grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=duration_var).grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=description_var, wraplength=600, justify=tk.LEFT).grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=ratings_var).grid(row=6, column=0, columnspan=2, sticky=tk.W, padx=10)

# Loading/Status message label
status_label = tk.Label(root, text="", fg="blue")
status_label.grid(row=7, column=0, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()

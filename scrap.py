import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def fetch_video_info():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        title_var.set("Title: " + yt.title)
        views_var.set("Views: " + str(yt.views))
        duration_var.set("Duration: " + str(yt.length))
        description_var.set("Description:\n" + yt.description if yt.description else "Description: None")
        ratings_var.set("Ratings: " + str(yt.rating) if yt.rating else "Ratings: None")
    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch video details. " + str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Info Fetcher")

# Create and place widgets
tk.Label(root, text="Enter YouTube Video URL:").grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, pady=10, padx=10)

fetch_button = tk.Button(root, text="Fetch Info", command=fetch_video_info)
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

title_var = tk.StringVar()
views_var = tk.StringVar()
duration_var = tk.StringVar()
description_var = tk.StringVar()
ratings_var = tk.StringVar()

tk.Label(root, textvariable=title_var, wraplength=600, justify=tk.LEFT).grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=views_var).grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=duration_var).grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=description_var, wraplength=600, justify=tk.LEFT).grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Label(root, textvariable=ratings_var).grid(row=6, column=0, columnspan=2, sticky=tk.W, padx=10)

# Start the GUI main loop
root.mainloop()

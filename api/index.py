from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cur_dir = os.getcwd()

@app.post("/api/download")
async def download_video(link: str = Form(...)):
    # This will try to download inside serverless environment
    # may not work for big files or long tasks
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, f"video-{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download started"}

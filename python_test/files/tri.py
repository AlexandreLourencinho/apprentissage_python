from pathlib import Path

dirs = {
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
    ".py": "code",
    ".txt": "documents",
    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".ppt": "documents",
    ".pptx": "documents",
    ".xls": "documents",
    ".xlsx": "documents",
    ".csv": "documents",
    ".mp3": "music",
    ".wav": "music",
    ".mp4": "videos",
    ".mov": "videos",
    ".avi": "videos",
    ".mkv": "videos",
    ".zip": "archives",
    ".tar": "archives",
    ".gz": "archives",
    ".rar": "archives",
    ".7z": "archives",
    ".exe": "autres",
    ".msi": "autres",
    ".dmg": "autres",
    ".java": "code",
    ".class": "code",
    ".jar": "archives",
    ".js": "code",
    ".ts": "code",
    ".json": "code"
}

sort_dir = Path.home() / "Downloads"
files = [f for f in sort_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = sort_dir / dirs.get(f.suffix, "autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

# TODO ok c'est stylé regarder comment créer un programme qui fait ça pour ranger mon bordel sur mon pc de manière auto
# TODO probablement voir pour une interface graphique également
# c'est ça que je veux dans python, youhou !
# ps github copilot qui m'a créé la liste dirs presque tout seul, gg bro
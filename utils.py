def download_video(url):
    try:
        return {"ok": True, "file": "example.mp4"}  # Bu yerda haqiqiy yuklash funksiyasi bo‘ladi
    except Exception as e:
        return {"ok": False, "error": str(e)}
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Free Fire Info API", version="1.0")

@app.get("/")
def home():
    return {"status": "Online", "message": "API is running successfully!"}

@app.get("/player")
def get_player_info(uid: str, region: str = "bd"):
    try:
        # এখানে ফ্রি ফায়ারের আসল রিকোয়েস্ট বা থার্ড-পার্টি গেস্ট টোকেন বেসড এন্ডপয়েন্ট ইন্টিগ্রেট করতে হবে
        # এটি একটি স্যাম্পল স্ট্রাকচার যা তোর রিকোয়েস্ট হ্যান্ডেল করবে
        
        if not uid:
            raise HTTPException(status_code=400, detail="UID is required")
            
        # ডেমো রেসপন্স (সার্ভার কানেকশন নিশ্চিত করার জন্য)
        player_data = {
            "UID": uid,
            "Region": region.upper(),
            "PlayerNickname": "MOSFIKE..?",
            "Level": "Active",
            "Likes": 1368,
            "AccountCreated": "Check via Token",
            "TopUpStatus": "Active"
        }
        
        return {"status": 200, "data": player_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
      

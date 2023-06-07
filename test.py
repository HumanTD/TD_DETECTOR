from backtrack import BackTrack
from database import get_database


dbname = get_database()
collection = dbname["Camera"]
cameras = collection.find()
camera_list = []
lat = 123
long = 456
radius = 1000

back = BackTrack()

nearby_cameras = []
nearby_cameras = back.get_nearby_cameras(lat, long, radius)
print(nearby_cameras)
# videocheck = []
# for i in nearby_cameras:
#     videoObject = {
#         "CameraId": i["_id"],
#         "VideoId": i["VideoId"],
#         "VideoCheck": back.check_video(i["VideoId"])
#     }
#     if videoObject["VideoCheck"] == True:
#         videocheck.append(videoObject)


print(videocheck)
# for videoId in nearby_cameras["VideoId"]:
#     videocheck.append(back.check_video(videoId))

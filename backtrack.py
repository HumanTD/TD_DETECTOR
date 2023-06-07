from database import get_database


class BackTrack:
    def __init__(self) -> None:
        dbname = get_database()
        self.collection = dbname["Camera"]
        self.cameras = self.collection.find()
        self.camera_list = []
        pass

    def get_nearby_cameras(self, lat, long, radius) -> list:
        camera_list = []

        for camera in self.cameras:
            if (int(camera["Latitude"]) - int(lat)) ** 2 + (int(camera["Longitude"]) - int(long)) ** 2 <= radius ** 2:
                camera_list.append(camera)
        return camera_list

    def get_next_camera(self, last_known_camera) -> list:
        camera_list = []
        print(last_known_camera)
        for nearby_camera_id in last_known_camera['NearbyCameras']:
            nearby_camera = self.collection.find_one({"_id": nearby_camera_id})
            camera_list.append(nearby_camera)

        return camera_list

    def check_video(self, video_id) -> bool:
        return True

    def check_nearby_cameras(self, camera_list) -> list:
        videocheck = []

        for i in camera_list:
            videoObject = {
                "CameraId": i["_id"],
                "VideoId": i["VideoId"],
                "VideoCheck": self.check_video(i["VideoId"])
            }
        return videocheck


    def get_all_paths(self, start_camera):
        all_paths = []
        queue = [[start_camera]]
        while queue:
            current_path = queue.pop(0)
            current_camera = current_path[-1]
            all_paths.append(current_path)
            for nearby_camera_id in current_camera['NearbyCameras']:
                new_path = list(current_path)
                nearby_camera = self.collection.find_one({"_id": nearby_camera_id})
                if nearby_camera not in new_path:
                    new_path.append(nearby_camera)
                    queue.append(new_path)
        return all_paths

    def get_path(self, start_camera):
        path = [] # list of cameras
        camera_list = self.camera_list  
        while start_camera['VideoId'] :
            if start_camera["_id"] in path:
                break
            else : 
                path.append(start_camera["_id"])

        
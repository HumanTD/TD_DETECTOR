from database import get_database


class BackTrack:
    def __init__(self):
        dbname = get_database()
        self.collection = dbname["Camera"]
        self.cameras = self.collection.find()
        self.camera_dict = {}  # Dictionary to store cameras by ID
        self.populate_camera_dict()

    def populate_camera_dict(self):
        for camera in self.cameras:
            self.camera_dict[camera["_id"]] = camera

    def check_video(self, video_id):
        # Your video check logic here
        return True

    def find_direction(self, camera1, camera2):
        lat_diff = camera2["Latitude"] - camera1["Latitude"]
        long_diff = camera2["Longitude"] - camera1["Longitude"]

        if lat_diff > 0:
            return "north"
        elif lat_diff < 0:
            return "south"
        elif long_diff > 0:
            return "east"
        elif long_diff < 0:
            return "west"
        else:
            return "unknown"

    def get_path(self, start_camera_id):
        path = []  # List of camera IDs
        visited = set()  # Set to track visited camera IDs
        camera_dict = self.camera_dict

        start_camera = camera_dict[start_camera_id]
        path.append(start_camera_id)

        while start_camera:
            if start_camera_id in visited:
                # Backtrack to the first camera that satisfies the condition
                backtrack_index = len(path) - 2
                while backtrack_index >= 0:
                    backtrack_camera_id = path[backtrack_index]
                    backtrack_camera = camera_dict[backtrack_camera_id]
                    if self.check_video(backtrack_camera["VideoId"]):
                        break
                    backtrack_index -= 1

                # If no previous camera satisfies the condition, break the loop
                if backtrack_index < 0:
                    break

                # Remove the repeated cameras from the path
                path = path[:backtrack_index+1]
                start_camera_id = path[backtrack_index]
                start_camera = camera_dict[start_camera_id]

            visited.add(start_camera_id)

            found_next_camera = False
            next_camera_id = None

            for nearby_camera_id in start_camera.get("NearbyCameras", []):
                nearby_camera = camera_dict[nearby_camera_id]
                direction = self.find_direction(start_camera, nearby_camera)
                if direction != "unknown":
                    if self.check_video(nearby_camera["VideoId"]):
                        next_camera_id = nearby_camera_id
                        break

            if next_camera_id:
                start_camera_id = next_camera_id
                start_camera = camera_dict[start_camera_id]
                path.append(start_camera_id)
                found_next_camera = True

            if not found_next_camera:
                # Backtrack to the previous camera and move to the next possible CCTV
                if len(path) >= 2:
                    path.pop()
                    start_camera_id = path[-1]
                    start_camera = camera_dict[start_camera_id]
                else:
                    break

        return path


def find_cctv_name(camera_id):
    # Function to find the CCTV name based on the camera ID
    # Implement your logic here
    pass


def main():
    # Create an instance of the BackTrack class
    backtracker = BackTrack()

    # Obtain the start camera ID (assuming you have its information)
    start_camera_id = "1"  # Replace with the actual ID of the start camera

    # Get the path based on the start camera ID
    path = backtracker.get_path(start_camera_id)

    # Print the resulting path with actual CCTV names
    print("Path:")
    for camera_id in path:
        cctv_name = find_cctv_name(camera_id)
        print(f"CCTV ID: {camera_id}, CCTV Name: {cctv_name}")

    # Check if the last camera in the path satisfies the condition
    last_camera_id = path[-1]
    if backtracker.check_video(backtracker.camera_dict[last_camera_id]["VideoId"]):
        print("Person found in the last camera.")
    else:
        print("Person not found in the last camera.")


if __name__ == "__main__":
    main()

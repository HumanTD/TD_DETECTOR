# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

from backtrack import BackTrack
# creating a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        data = request.get_json()
        lat = data['latitude']
        long = data['longitude']
        RADIUS = 100000
        backtrack = BackTrack()
        pathway = []
        near_by_cameras = backtrack.get_nearby_cameras(lat, long, RADIUS)

        check_nearby_cameras = backtrack.check_nearby_cameras(near_by_cameras)
        # while len(check_nearby_cameras) > 0:
        #     if che
        #     pathway.append(check_nearby_cameras[0])

        #     print(check_nearby_cameras[0])
        #     # check_nearby_cameras = backtrack.check_nearby_cameras(
        #     #    videoObject check_nearby_cameras[0])
        #     break
        for i in range(len(check_nearby_cameras)):
            if check_nearby_cameras[i]["VideoCheck"] == True:
                pathway.append(check_nearby_cameras[i])
                break
            else:
                continue
        print(pathway)
        return ({
            "nearby_cameras": True,
        })


@app.route('/hello', methods=['GET', 'POST'])
def check():
    if (request.method == 'POST'):
        data = request.get_json()
        lat = data['latitude']
        long = data['longitude']
        RADIUS = 10
        backtrack = BackTrack()
        first_camera = backtrack.get_nearby_cameras(lat, long, RADIUS)[0]
        pathway = backtrack.get_all_paths(first_camera)
        print(pathway)
        return ({
            "nearby_cameras": f"{pathway}",
        })


# driver function
if __name__ == '__main__':

    app.run(debug=True)

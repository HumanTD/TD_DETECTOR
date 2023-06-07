from database import get_database
dbname = get_database()
collection_name = dbname["Camera"]

item_1 = {
    "_id": 1,
    "Latitude": 123,
    "Longitude": 456,
    "VideoId": 123123123,
    "NearbyCameras": [1, 2, 3, 4]
}

item_2 = {
    "_id": 2,
    "Latitude": 123,
    "Longitude": 238,
    "VideoId": 213124,
    "NearbyCameras": [1, 4]
}
item_3 = {
    "_id": 3,
    "Latitude": 304,
    "Longitude": 456,
    "VideoId": 2109321983,
    "NearbyCameras": [3, 4]
}
item_4 = {
    "_id": 4,
    "Latitude": 82913981,
    "Longitude": 456,
    "NearbyCameras": [1]
}
collection_name.insert_many([item_1, item_2, item_3, item_4])

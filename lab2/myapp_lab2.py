from flask import Flask, jsonify

all_records = [
    {
    "name" : "Radiohead",
    "albums" : [
            {
                "title":"The King of Limbs",
                "songs":[
                    "..."
                    ],
                    "description":"..."
                },
                {
                    "title":"OK Computer",
                    "songs":[],
                    "description":"..."
                }
            ]
    },
    {
    "name":"Portishead",
    "albums":[
            {
                "title":"Dummy",
                "songs":[],
                "description":"..."
    },
    {
                "title":"Third",
                "songs":[],
                "description":"..."
            }
        ]
    }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "<h1>Hello, World!</h1>"

@app.route('/records/', methods=['GET'])
def get_records():
        return jsonify(all_records)

@app.route('/records/all_bands/', methods=['GET'])
def get_bands():
        response = [item['name'] for item in all_records]
        return jsonify(response)

@app.route('/records/albums_by_band/<bandname>/', methods=['GET'])
def get_album_by_band(bandname):
        response={bandname:'Not Found!'}
        for item in all_records:
                if item["name"]==bandname:
                        response = [x["title"] for x in item["albums"]]
                        break
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

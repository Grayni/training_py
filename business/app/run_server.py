# USAGE
# Start the server:
# 	python run_server.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
# Submita a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd

# import cloudpickle
import flask

dill._dill._reverse_typemap['ClassType'] = type

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

X_test = pd.read_csv("data_split/X_test.csv")

def load_model(model_path):
    # load the pre-trained model
    global model
    with open(model_path, 'rb') as f:
        model = dill.load(f)


@app.route("/", methods=["GET"])
def general():
    return "Welcome to fraudlent prediction process"


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":

        request_json = flask.request.get_json()
        df = pd.DataFrame(request_json, index=[0])

        predictions = model.predict_proba(df)

        data["predictions"] = predictions[:, 1][0]

        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    modelpath = "./model/cardio.dill"
    load_model(modelpath)
    app.run()

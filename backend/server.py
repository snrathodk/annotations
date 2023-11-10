from flask import Flask, Response, jsonify, request
# Import flask and datetime module for showing date and time
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/data')
def get_time():

	# Returning an api for showing in reactjs
	return {
		'Name':"geek", 
		"Age":"22",
		"Date":x, 
		"programming":"python"
		}

@app.route("/api_endpoint", methods=["POST"])
def function_for_api():
    img = request.files['file']
    print(img.filename)
    return Response(status=200)

# Running app
if __name__ == '__main__':
	app.run(debug=True, port=5001)


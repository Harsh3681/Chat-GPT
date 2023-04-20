# deploy it on the "render"
# link = https://mychat-2htl.onrender.com/

from flask import Flask, request, jsonify, render_template
import openai
import os
from flask_cors import CORS

# Set up the Flask app
app = Flask(__name__)
cors = CORS(app)

openai.api_key = "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" 


@app.route('/', methods=['GET'])

def index():
    # Render the "index.html" template as the response
    return render_template('index.html')

# Define a route for the API endpoint
@app.route("/openai", methods=["POST"])
def openai_endpoint():
    # Get the request data
    data = request.get_json()

    # Get the prompt from the request data
    prompt = str(data)

    # Set up the OpenAI API parameters
    params = {
        "engine": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1
    }

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(**params)

    # Get the response text from the API response
    print(response)
    response_text = response.choices[0].text.strip() # remove the leading and trailing spaces

    # Return the response as JSON
    return jsonify({"response": response_text})

# Run the app
if __name__ == "__main__":
    app.run(debug=True) 




# http://127.0.0.1:5000/



# the above code is explain is as follow :

# 1. import the flask module for the "web app development" and the following modules : 
# 2. import the openai module for the ai chatbot development 
# 3. import the os module for the "environment variables" 
# 4. import the flask_cors module for the "cross origin resource sharing" that is used to allow the api to be accessed by the web app   
# 5. set up the flask app 
# 6. set up the cors 
# 7. set up the openai api key
# 8. define the index route
# 9. define the openai route
# 10. get the request data
# 11. get the prompt from the request data
# 12. set up the openai api parameters
# 13. call the openai api to generate a response 
# 14. get the response text from the api response
# 15. return the response as json
# 16. run the app

# how the above program work is as follow :

# 1. the user will go to the index route
# 2. the user will enter the prompt
# 3. the user will click the submit button
# 4. the user will go to the openai route
# 5. the user will get the request data
# 6. the user will get the prompt from the request data
# 7. the user will set up the openai api parameters
# 8. the user will call the openai api to generate a response
# 9. the user will get the response text from the api response
# 10. the user will return the response as json
# 11. the user will run the app

# is we have used node.js in this code ? 







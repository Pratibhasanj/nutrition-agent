import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model
from prompts import build_nutrition_prompt

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
REGION = os.getenv("WATSONX_REGION")

model = Model(
    model_id="granite-13b-instruct",  # You can use other Granite models too
    params={"decoding_method": "greedy", "max_new_tokens": 300},
    credentials={
        "url": f"https://{REGION}.ml.cloud.ibm.com",
        "apikey": API_KEY,
    },
    project_id=PROJECT_ID
)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("question", "")

    prompt = build_nutrition_prompt(user_input)
    response = model.generate(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

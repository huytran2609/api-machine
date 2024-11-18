from flask import Flask, request, jsonify, send_file
import uuid
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import requests
import os
from dotenv import load_dotenv
import glob
from flask_cors import CORS
import asyncio
import subprocess
import threading
import logging
from utils.log import thread_log
import json
# from tools.chatbot import init_chatbot

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)
app.static_folder = "public"

# model, kdtree, answers = init_chatbot()

# chatbot_store = {"model": model, "kdtree": kdtree, "answers": answers}


@app.route("/recommend", methods=["POST"])
def post_recommend():
    from tools.recommend import handle_recomment

    body = request.get_json()  # Get the JSON data from the request
    skills = body.get("skills", [])

    result = handle_recomment(skills)
    return jsonify(json.loads((result))), 200


@app.route("/", methods=["GET"])
def get_default():
    return jsonify("hello"), 200


# @app.route("/chat", methods=["GET"])
# def chat():
#     from tools.chatbot import chatbot
#     stored_model = chatbot_store["model"]
#     stored_kdtree = chatbot_store["kdtree"]
#     stored_answers = chatbot_store["answers"]

#     question = request.args.get("question")
#     messages = chatbot(stored_model, stored_kdtree, stored_answers, question)
#     print(messages)
#     return jsonify(messages)


if __name__ == "__main__":
    app.run()

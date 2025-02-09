from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 后端 API 地址
API_URL = "http://127.0.0.1:8000/analyze_video"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """前端提交视频 URL，调用 FastAPI 并返回结果"""
    video_url = request.form.get("video_url")
    response = requests.post(API_URL, json={"video_url": video_url})
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"status": "error", "message": "分析失败"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    return {"visits": r.incr("visits")}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

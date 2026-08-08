from app import app
from waitress import serve

if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 4500
    print(f"App running at {HOST}:{PORT}")
    serve(app, host=HOST, port=PORT, threads=6)
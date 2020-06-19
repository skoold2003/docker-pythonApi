from pdap import create_app

app = create_app("development")
# app = create_app("development-docker")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

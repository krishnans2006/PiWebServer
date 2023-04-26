from flask import Flask

app = Flask(__name__)

@app.route("/temp")
def temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = int(file.read().strip())
    return str(temp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

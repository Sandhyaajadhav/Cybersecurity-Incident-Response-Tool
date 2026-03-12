from flask import Flask, render_template
import attack_simulator
import detection_engine
import response_module

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulate")
def simulate():

    attack = attack_simulator.simulate_attack()

    detection = detection_engine.detect_threat(attack)

    response = response_module.response_action(attack)

    return render_template(
        "dashboard.html",
        attack=attack,
        detection=detection,
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)
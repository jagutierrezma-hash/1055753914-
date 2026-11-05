from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/par-impar/<int:valor>")
def par_impar(valor):
    mensaje = "el numero es par" if valor % 2 == 0 else "el numero es impar"
    return jsonify({"numero": valor, "mensaje": mensaje})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

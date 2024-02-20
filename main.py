from flask import Flask, request, jsonify
from sqlite4 import SQLite4
from popular import readData
import sys
database = readData()
database_name = "alunos.db"
engine = SQLite4("alunos.db")
engine.connect()
try:
  if sys.argv[1] == "first":
    engine.delete("alunos", "1=1")
    engine.create_table("alunos", {"matricula": "INTEGER", "nome": "TEXT", "saldo": "INTEGER"})
    for data in database:
      dataDict = {"matricula": data[0], "nome": data[1], "saldo": data[2]}
      engine.insert("alunos", dataDict)
except:
  pass


app = Flask(__name__)

@app.route("/api/qrcode", methods=["POST"])
def receive_qrcode():
  data = request.get_json()
  qrcode_data = data["qrcode"]
  print(f"QRCode data: {qrcode_data} : quantidade de pessoas: {data['quantidade']}")

  aluno = engine.select("alunos", columns=["matricula , nome, saldo"], condition=f"matricula = {qrcode_data}")
  aluno = aluno[0]
  if aluno[2] < 1:
    print(f"Saldo insuficiente, aluno: {aluno[1]}, saldo atual: {aluno[2]}")
    print("faça uma recarga")
    return jsonify({"success": False}), 499
  else:
    print(f"Matricula: {aluno[0]} , {aluno[1]}, tem {aluno[2]} fichas. Retirando uma ficha...")
    engine.update("alunos", {"saldo": aluno[2] - 1}, f"matricula = {qrcode_data}")
    upd_alun = engine.select("alunos", columns=["matricula , nome, saldo"], condition=f"matricula = {qrcode_data}")
    upd_alun = upd_alun[0]
    print(f"Saldo atualizado, aluno: {upd_alun[1]}, saldo atual: {upd_alun[2]}")
    return jsonify({"success": True})

@app.route("/saldo", methods=["GET"])
def get_alunos():
  alunos = engine.select("alunos")
  return jsonify(alunos)

@app.route("/recarga/<int:matricula>", methods=["GET"])
def recarga_aluno(matricula):
  aluno = engine.select("alunos", columns=["matricula , nome, saldo"], condition=f"matricula = {matricula}")
  engine.update("alunos", {"saldo": aluno[0][2] + 10}, f"matricula = {matricula}")
  return jsonify({"success": True})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, use_reloader=True)

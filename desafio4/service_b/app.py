from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

SERVICE_A_URL = "http://service_a:8001"


@app.get("/usuarios-combinado")
def getCombinedUsuarios():
    try:
        response = requests.get(f"{SERVICE_A_URL}/usuarios")
        usuarios = response.json()

        formatted_usuarios = []

        for usuario in usuarios:
            status = "ativo" if usuario["active"] else "inativo"
            start_date = datetime.strptime(usuario["start_date"], "%Y-%m-%d")
            days_since = (datetime.now() - start_date).days

            formatted_usuarios.append({
                "id": usuario["id"],
                "nome": usuario["name"],
                "status": status,
                "data_inicio": usuario["start_date"],
                "dias_desde_inicio": days_since,
                "mensagem": f"Usuário {usuario['name']} {status} desde {usuario['start_date']} ({days_since} dias)"
            })

        return jsonify({
            "total": len(formatted_usuarios),
            "usuarios": formatted_usuarios
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.get("/usuarios-detalhado/<int:usuario_id>")
def getUsuarioDetailed(usuario_id):
    try:
        response = requests.get(f"{SERVICE_A_URL}/usuarios/{usuario_id}")
        usuario = response.json()

        if "error" in usuario:
            return jsonify(usuario), 404

        status = "ativo" if usuario["active"] else "inativo"
        start_date = datetime.strptime(usuario["start_date"], "%Y-%m-%d")
        days_since = (datetime.now() - start_date).days

        return jsonify({
            "id": usuario["id"],
            "nome": usuario["name"],
            "status": status,
            "data_inicio": usuario["start_date"],
            "dias_desde_inicio": days_since,
            "detalhes": f"Usuário {usuario['name']} está {status} há {days_since} dias"
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.get("/health")
def health_check():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)

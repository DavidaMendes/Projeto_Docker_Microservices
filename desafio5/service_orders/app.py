from flask import Flask, jsonify

app = Flask(__name__)

pedidos_db = [
    {"id": 1, "usuario_id": 1, "produto": "Notebook", "valor": 2500.00, "status": "entregue"},
    {"id": 2, "usuario_id": 1, "produto": "Mouse", "valor": 50.00, "status": "pendente"},
    {"id": 3, "usuario_id": 2, "produto": "Teclado", "valor": 150.00, "status": "entregue"},
    {"id": 4, "usuario_id": 3, "produto": "Monitor", "valor": 800.00, "status": "processando"},
]

@app.get("/health")
def healthCheck():
    return jsonify({"status": "healthy", "component": "service_orders"})

@app.get("/pedidos")
def getAllPedidos():
    return jsonify(pedidos_db)

@app.get("/pedidos/<int:pedido_id>")
def getPedido(pedido_id):
    for pedido in pedidos_db:
        if pedido["id"] == pedido_id:
            return jsonify(pedido)
    return jsonify({"error": "Pedido não encontrado"}), 404

@app.get("/pedidos/usuario/<int:usuario_id>")
def getPedidosUsuario(usuario_id):
    pedidos_usuario = [pedido for pedido in pedidos_db if pedido["usuario_id"] == usuario_id]
    return jsonify(pedidos_usuario)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)
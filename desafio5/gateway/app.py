from fastapi import FastAPI, HTTPException
import httpx
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SERVICE_USERS_URL = "http://service_users:8001"
SERVICE_ORDERS_URL = "http://service_orders:8002"

@app.get("/health")
def healthCheck():
    return {"status": "healthy", "component": "gateway"}

@app.get("/users")
def getAllUsers():
    try:
        response = httpx.get(f"{SERVICE_USERS_URL}/usuarios", timeout=5.0)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Erro ao buscar usuários: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao serviço de usuários: {str(e)}")

@app.get("/users/{user_id}")
def getUser(user_id: int):
    try:
        response = httpx.get(f"{SERVICE_USERS_URL}/usuarios/{user_id}", timeout=5.0)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        raise HTTPException(status_code=500, detail="Erro ao buscar usuário")
    except Exception as e:
        logger.error(f"Erro ao buscar usuário {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao serviço de usuários: {str(e)}")

@app.get("/orders")
def getAllOrders():
    try:
        response = httpx.get(f"{SERVICE_ORDERS_URL}/pedidos", timeout=5.0)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Erro ao buscar pedidos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao serviço de pedidos: {str(e)}")

@app.get("/orders/{order_id}")
def getOrder(order_id: int):
    try:
        response = httpx.get(f"{SERVICE_ORDERS_URL}/pedidos/{order_id}", timeout=5.0)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        raise HTTPException(status_code=500, detail="Erro ao buscar pedido")
    except Exception as e:
        logger.error(f"Erro ao buscar pedido {order_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao serviço de pedidos: {str(e)}")

@app.get("/users/{user_id}/orders")
def getUserOrders(user_id: int):
    try:
        user_response = httpx.get(f"{SERVICE_USERS_URL}/usuarios/{user_id}", timeout=5.0)
        user_response.raise_for_status()
        user = user_response.json()
        
        orders_response = httpx.get(f"{SERVICE_ORDERS_URL}/pedidos/usuario/{user_id}", timeout=5.0)
        orders_response.raise_for_status()
        orders = orders_response.json()
        
        return {
            "usuario": user,
            "pedidos": orders
        }
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        raise HTTPException(status_code=500, detail="Erro ao buscar dados")
    except Exception as e:
        logger.error(f"Erro ao buscar pedidos do usuário {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao conectar aos serviços: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
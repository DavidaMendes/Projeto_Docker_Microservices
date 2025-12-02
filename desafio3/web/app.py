from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        host="db",
        database="appdb",
        user="admin",
        password="senha"
    )

cache = redis.Redis(host="cache", port=6379)

@app.get("/db")
def test_db():
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        conn.close()
        return {"db_status": "connected", "result": result}
    except Exception as e:
        return {"db_status": "error", "error": str(e)}

@app.get("/cache/set")
def cache_set():
    cache.set("mensagem", "Teste")
    return {"cache": "value_set"}

@app.get("/cache/get")
def cache_get():
    value = cache.get("mensagem")
    return {"cache_value": value.decode() if value else None}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

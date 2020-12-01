# este modulo se puede usar para hacer debug
import uvicorn

if __name__ == "__main__":
    uvicorn.run("config.api:app", host="0.0.0.0", port=8002)

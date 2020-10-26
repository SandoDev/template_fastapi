# este modulo se puede usar para hacer debug
import uvicorn
from app.api.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

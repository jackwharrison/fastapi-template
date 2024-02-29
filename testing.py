import uvicorn
from typing import Union
from fastapi import Depends, FastAPI, Request, HTTPException, Header
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import os
import logging
import sys
from dotenv import load_dotenv
import random
# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("azure").setLevel(logging.WARNING)
logging.getLogger("requests_oauthlib").setLevel(logging.WARNING)

# Load environment variables
load_dotenv()

# Load PORT from environment variables or use default 8000
port = int(os.getenv("PORT", 8000))

# Initialize FastAPI
app = FastAPI(
    title="fastapi-template",
    description="Template repo for FastAPI.",
    version="0.0.1",
    license_info={
        "name": "AGPL-3.0 license",
        "url": "https://www.gnu.org/licenses/agpl-3.0.en.html",
    },
)
key_query_scheme = APIKeyHeader(name="key")

# Function to perform some action
def some_function():
    """Some function that does something."""
    pass

# Dependency to get required headers
def required_headers(
        username: str = Header(),
        password: str = Header()):
    """Headers required to use the API."""
    return username, password



names = ["Matthew", "Mark", "Luke", "John"]


# Demo API endpoint
@app.get("/demo")
async def demo_api():
    """Demo API endpoint."""
    random_name = random.choice(names)
    random_number = random.randint(1, 100) 
    return {"message": "This API will write the age of when you will die.", 
            "This person,": random_name,
            ", will die, at the following age": random_number}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)

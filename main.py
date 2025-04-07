from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# === MODELO DE ENTRADA ===
class CallRequest(BaseModel):
    phone_number: str

# === ENDPOINT POST ===
@app.post("/make-call")
def make_call(request: CallRequest):
    url = "https://api.bland.ai/v1/calls"

    headers = {
        "Authorization": "Bearer org_08ad39a77760d9fd370b1ddc24131a1bfc9c73867ad91984aca5e85d539a2395bffa0eb8a092c99bbf1269",
        "Content-Type": "application/json",
    }

    payload = {
        "phone_number": request.phone_number,
        "pathway_id": "801e637d-89ef-4efa-91c1-92c3886bd715",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "response": response.json()
        }

    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

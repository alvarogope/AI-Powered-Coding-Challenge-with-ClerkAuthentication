from fastapi import HTTPException
from clerk_backend_api import Clerk, AuthenticateRequestOptions
import os
from dotenv import load_dotenv

_backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(_backend_dir, ".env"))
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

def authenticate_and_get_user_details(request):
    request_state = clerk_sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=["http://localhost:5173", "http://localhost:5174"]
        )
    )
    if not request_state.is_signed_in:
        raise HTTPException(status_code=401, detail="Unauthorized")

    userid = request_state.payload.get("sub")
    return {"userid": userid}

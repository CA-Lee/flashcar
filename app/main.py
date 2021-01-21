from fastapi import FastAPI, Request, Header, Response
from starlette import status

from app.event_handler import handler

router = FastAPI()


@router.post("/webhook")
async def handle_webhook_events(
    request_body: Request, X_Line_Signature: str = Header(None)
) -> Response:
    """
    Handle all webhook events
    """

    try:

        body = await request_body.body()
        handler.handle(body.decode(), X_Line_Signature)

    except Exception as e:
        print(e)
    finally:
        return Response(status_code=status.HTTP_200_OK)

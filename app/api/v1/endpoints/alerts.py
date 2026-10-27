from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.notification_service import notification_manager

router = APIRouter()

@router.websocket("/ws/notifications")
async def websocket_notifications(websocket: WebSocket):
    await notification_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Mantiene vivo el canal
    except WebSocketDisconnect:
        notification_manager.disconnect(websocket)
from aiohttp import web

clients = set()


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    clients.add(ws)
    print("클라이언트 연결")

    join_msg = "새 사용자가 입장하였습니다."
    for client in clients:
        if client != ws:
            await client.send_str(join_msg)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            print(msg.data)

            for client in clients:
                if client != ws:
                    await client.send_str(msg.data)

        elif msg.type == web.WSMsgType.ERROR:
            print("WebSocket 연결 오류: ", ws.exception())

    notice = "사용자가 퇴장하였습니다."
    for client in clients : 
        if client != ws :
            await client.send_str(notice)
            
    clients.remove(ws)
    print("클라이언트 연결 해제")
    return ws


async def index(request):
    return web.FileResponse('index.html')


app = web.Application()
app.router.add_get('/', index)
app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8000)

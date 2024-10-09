import asyncio
import sys
import time
import json
from fastapi import FastAPI, Request, Response
from loguru import logger
from film.router import router as router_films
from event.base_consumer import Consumer
from starlette.middleware.cors import CORSMiddleware
from config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.consumer = Consumer()


app = App()
app.include_router(router_films)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS.split(";"),
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


logger.remove()
logger.add(sys.stdout, format="{time:YYYY-MM-DDTHH:mm:ss.SSSZ} - {level} - {message} - {module} - {function} - {file} - {name}", level=settings.LOG_LEVEL)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    body = await request.body()
    body_json = None
    if body:
        body_text = body.decode('utf-8')
        try:
            body_json = json.loads(body_text)
        except json.JSONDecodeError:
            body_json = body_text
        request._body = body

    async def receive_body():
        return {'type': 'http.request', 'body': body}

    request = Request(request.scope, receive=receive_body)

    response = await call_next(request)

    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk

    response = Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )

    process_time = time.time() - start_time

    status_code = response.status_code
    url = str(request.url)
    ip_address = request.client.host
    method = request.method

    log_message = (
        f"\n|| Status_code: {status_code}"
        f"\n|| URL: {url}"
        f"\n|| IP: {ip_address}"
        f"\n|| Method: {method}"
        f"\n|| Body: {body_json}"
    )

    if status_code == 200:
        logger.info(log_message)
    else:
        logger.error(log_message + f"\n|| Query_params: {dict(request.query_params)}"
                     + f"\n|| Response: {response_body.decode('utf-8')}"
                     + f"\n|| Process_time: {round(process_time, 2)}")

    return response

@app.on_event("startup")
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.consumer.consume(loop))
    await task

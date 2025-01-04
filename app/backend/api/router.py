from fastapi import APIRouter, Depends, HTTPException, status, Query
#from loguru import logger
from fastapi.responses import JSONResponse
from fastapi.requests import Request

router = APIRouter(prefix='/api', tags=['API'])

@router.get('/url')
async def external_url(request: Request):
    return str(request.url)



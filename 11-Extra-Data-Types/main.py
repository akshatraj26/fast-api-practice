from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
import uuid
from fastapi import FastAPI, Body

app = FastAPI()


@app.put('/item/{item_id}')
async def read_items(item_id: UUID,
                     start_datetime: Annotated[datetime | None,  Body()] = None,
                     end_datetime: Annotated[datetime | None, Body()] = None,
                     repeat_at: Annotated[time | None, Body()] = None,
                     process_after: Annotated[timedelta | None, Body()] = None):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {"item_id": item_id,
            'start_datetime': start_datetime,
            'end_datetine': end_datetime,
            'repeat_at': repeat_at,
            'process_after': process_after,
            'start_process': start_process,
            'duration': duration}
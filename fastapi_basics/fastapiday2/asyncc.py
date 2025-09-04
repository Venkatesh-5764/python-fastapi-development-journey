from fastapi import FastAPI
import asyncio
from datetime import datetime

venkk = FastAPI()

@venkk.get("/time")
async def time_task():
    messages = []
    for i in range(3):  # run 3 times
        now = datetime.now().strftime("%H:%M:%S")
        msg = f"Hello! Current time is {now}"
        print(msg)   # server console output
        messages.append(msg)
        await asyncio.sleep(3)  # wait 3 seconds (non-blocking)
    return {"messages": messages}

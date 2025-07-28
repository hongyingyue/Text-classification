from typing import Any, Dict, List, Optional, Union

import datetime
import json
import re
import uuid
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
import logging

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from logging.handlers import TimedRotatingFileHandler

from pydantic import BaseModel
from util import calc_accuracy4math, calc_cloud_score, format_reward_deepseek

logger = logging.getLogger(__name__)


file_handler = TimedRotatingFileHandler(
    "data/logs/text_classifiction.log",
    when="midnight",
    interval=1,
    backupCount=5,
)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BaseRequest(BaseModel):
    data_source: Any
    solution_str: str
    ground_truth: Union[dict, list, str]
    extra_info: Union[dict, list, str]


@app.post("/get_classifiction")
async def get_reward(request: Request):
    json_data = await request.json()
    # print(json_data)

    groud_truth: str = json_data.get("ground_truth", "")
    pred_answer = json_data.get("response_str", "")

    if isinstance(pred_answer, list):
        pred_answer = pred_answer[0]


    score["score"] = sum(
        score.values()
    )

    cur_date = datetime.datetime.now()

    temp_data = {
        "cur_date": cur_date.strftime("%Y-%m-%d %X"),
        "input_data": json_data,
        "score": score,
    }
    logger.info(json.dumps(temp_data, ensure_ascii=False))

    return score


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6009)

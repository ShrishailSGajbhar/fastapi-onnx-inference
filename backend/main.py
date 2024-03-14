from fastapi import FastAPI, Response
from pydantic import BaseModel

import torch
import numpy as np
from transformers import RobertaTokenizer
import onnxruntime
from fastapi.middleware.cors import CORSMiddleware


tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")


class Body(BaseModel):
    phrase: str

app = FastAPI()

# Allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allow these HTTP methods
    allow_headers=["*"],  # Allow all headers
)



@app.get('/')
def root():
    return Response("<h1>A self-documenting API to interact with an ONNX model</h1>")


def to_numpy(tensor):
    if tensor.requires_grad:
        return tensor.detach().cpu().numpy()
    return tensor.cpu().numpy()


@app.post('/predict')
def predict(body: Body):
    input_ids = torch.tensor(
        tokenizer.encode(body.phrase, add_special_tokens=True)
    ).unsqueeze(
        0
    )

    inputs = {session.get_inputs()[0].name: to_numpy(input_ids)}
    out = session.run(None, inputs)

    result = np.argmax(out)
    if bool(result)==True:
        return {'sentiment': "positive"}
    else:
        return {"sentiment": "negative"}

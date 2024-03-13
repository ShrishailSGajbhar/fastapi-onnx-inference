## Reproducing the FastAPI-ONNX Inference For Sentiment Analysis

### How to run
Prerequisites:
- Docker
- Binary file for the task in onnx format. Download it from this [link](https://github.com/kundanapillari/models/tree/master/text/machine_comprehension/roberta/model) 

1. Create a docker image using command `docker build -t fastapi-onnx-sentiment .`
2. Run the container using `docker run -d -p 8000:8000 fastapi-onnx-sentiment`
3. 
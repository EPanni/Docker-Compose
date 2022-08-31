FROM python:3.9

RUN python -m pip install --upgrade pip

WORKDIR /backend

COPY . /backend

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /backend/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

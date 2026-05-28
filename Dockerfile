FROM docker.arvancloud.ir/python:3.11-slim

WORKDIR /app

ENV PIP_INDEX_URL=https://pypi.devneeds.ir/simple/
ENV PIP_TRUSTED_HOST=pypi.devneeds.ir

COPY pyproject.toml requirements.txt ./
COPY src/ ./src/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir .

CMD ["airbnb-ops", "run"]
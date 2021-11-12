FROM python:3.9-alpine

COPY requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt


COPY . .

CMD python3 -m pytest homework5/tests/test_auth_page.py --executor 0.0.0.0:4444
FROM python:3.8-alpine

WORKDIR /yada
RUN pip install -r flask gunicorn

COPY app /yada/

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "application:app"]

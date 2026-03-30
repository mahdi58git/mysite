FROM python:3.12-slim
WORKDIR /mysite
ENV PYTHONDONTWRITEBYTECODE=1ENV PYTHONUNBUFFERED=1
COPY . .
RUN  pip install --no-cache-dir -i https://mirror-pypi.runflare.com/simple -r requirements.txt
RUN adduser --disabled-password --gecos "" mahdi && chown -R mahdi:mahdi /mysite
USER mahdi
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
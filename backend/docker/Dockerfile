FROM python:3.10
WORKDIR /DRFpackt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./DRFpackt .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
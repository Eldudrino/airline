FROM python:3
COPY . C:/Users/Arman HajiAzizi/Desktop/lecture8
WORKDIR C:/Users/Arman HajiAzizi/Desktop/lecture8
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0.8000"]
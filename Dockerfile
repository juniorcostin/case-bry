FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN  pip install --upgrade pip

RUN pip install numpy
RUN pip install streamlit-option-menu
RUN pip install streamlit
RUN pip install boto3



EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py"]
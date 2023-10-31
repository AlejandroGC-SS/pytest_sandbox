FROM python:3.11.6-bullseye
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash"]
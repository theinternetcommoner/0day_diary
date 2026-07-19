<img width="1365" height="612" alt="Screenshot_2" src="https://github.com/user-attachments/assets/b580dfd4-de18-4bd8-978a-1b536df2ea33" />

# Zer0 Day Diary
No fluff. just you thoughts

## Stack
Python 3.11 or higher  
Flask (API)  
Waitress WSGI (Server)  
HTML & Bootstrap (Frontend)  
SQLite (Database)  

## Installation and setup (For host PC - Windows)

Clone the repository, extract and go to the directory and use the following commands:

Create virtual environment
```
python -m venv <yourvenv>
```

Activate virtual environment
```cmd
.\<yourenv>\Scripts\activate
```
or
```cmd
./<yourenv>/Scripts/activate
```

Install dependencied using the requirements.txt file
```cmd
pip install -r requirements.txt
```

Run the app
```cmd
python app.py
```

## Running with Docker

To build the image uding the Dockerfile
```cmd
docker build -t <yourpreferedimagename> .
```

Edit the compose.yml file and add your directory (for persistence)
```yml
services:
  app:
    container_name: <containername>
    image: <imagename>
    ports:
      - 4500:4500 # host_port:container_port
    volumes:
      # - source(host):target(container)
      - type: bind
        source: '<hostdirectory>'
        target: /0day_diary/data
    restart: always
```

To run the container
```cmd
docker compose up -d
```
To stop the container
```cmd
docker compose down
```

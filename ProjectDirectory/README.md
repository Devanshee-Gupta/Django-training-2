# Commands to execute

docker build -t devansheegupta/pollproject:latest .

docker run --name polls -p 8000:8000 -it devansheegupta/pollproject:latest
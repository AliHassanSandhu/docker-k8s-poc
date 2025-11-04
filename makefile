APP_NAME=docker-k8s-poc
TAG=latest

build:
	docker build -t $(APP_NAME):$(TAG) .

run:
	docker run -p 8000:8000 $(APP_NAME):$(TAG)

compose-up:
	docker-compose up --build

k8s-deploy:
	kubectl apply -f k8s/

test:
	pytest

clean:
	docker system prune -f

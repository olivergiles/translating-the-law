PROJECT_ID=translating-the-law
DOCKER_IMAGE_NAME=uksc-question-app

build_container:
	@docker build -t uksc-question-app .

build_google_container:
	@docker build -t eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME} .

push_google_container:
	@docker push eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME}

deploy_google_container:
	@gcloud run deploy --image eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME} --platform managed --region europe-west1 --memory 8Gi --cpu 2

docker_run:
	@docker run -e PORT=8001 -p 8001:8001 ${DOCKER_IMAGE_NAME}

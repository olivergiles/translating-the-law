PROJECT_ID=translating-the-law
DOCKER_IMAGE_NAME=uskc-summarizer-app

tests:
	@python tests/test_summ

build_container:
	@docker build -t ${DOCKER_IMAGE_NAME} .

build_google_container:
	@docker build -t eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME} .

push_google_container:
	@docker push eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME}

deploy_google_container:
	@gcloud run deploy --image eu.gcr.io/${PROJECT_ID}/${DOCKER_IMAGE_NAME} --platform managed --region europe-west1 --memory 8Gi --cpu 2

docker_run:
	@docker run -e PORT=8000 -p 8000:8000 ${DOCKER_IMAGE_NAME}

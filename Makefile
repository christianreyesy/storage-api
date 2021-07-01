.PHONY: push, pull

DOCKER_IMAGE_NAME := storage-api

# This value is the URI for the bucket or
# bucket with path corresponding to the storage you
# want to sync.
BUCKET_URI=gs://xyz-ekiim-api-storage

# This value is the local path for the directory
# where you are storing the copy of the bucket
# you are using for this proyect.
LOCAL_API_STORAGE=../xyz-ekiim-api-storage

pull:
	mkdir -p $(LOCAL_API_STORAGE)
	gsutil rsync -R $(BUCKET_URI) $(LOCAL_API_STORAGE)

push:
	echo "Pushing"

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run -p 8080:8080 --env-file .env $(DOCKER_IMAGE_NAME):latest

clean:
	rm -rf storage migrations database.db

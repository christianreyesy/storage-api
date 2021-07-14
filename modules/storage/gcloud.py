from os import environ
from pathlib import Path
from io import BytesIO
from google.cloud import storage

try:
    bucket_name = environ["GCLOUD_BUCKET"]
except KeyError:
    raise Exception("No gcloud bucket set")


def get_blob(target):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    return bucket.blob(target)


def get_file_to_store(collection, filename):
    target = str(Path(collection) / filename)
    blob = get_blob(target)
    if blob.exists():
        raise Exception("File already exists")
    return blob


def store_bytes(collection, filename, byte):
    target = get_file_to_store(collection, filename)
    target.upload_from_file(BytesIO(byte))


def store_string(collection, filename, text):
    target = get_file_to_store(collection, filename)
    target.upload_from_string(text)


def query_storage(path=""):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    iterator = bucket.list_blobs(
        prefix=path,
        delimiter="/",
        include_trailing_delimiter=True
    )
    blobs = list(iterator)
    dirs = [i[:-1] for i in iterator.prefixes]
    if len(dirs) == 0 and len(blobs) == 1 and blobs[0].name == path:
        blob = blobs[0]
        return dict(
            path=blob.name,
            type="file",
            metadata=dict(
                mime=blob.content_type,
                size=blob.size,
            )
        )
    else:
        print(dirs)
        return dict(
            path=path,
            type="directory",
            content=[*list(dirs), *[b.name for b in blobs]]
        )
    return {}


def get_storage_file(path=""):
    target = path
    blob = get_blob(target)
    if not blob.exists():
        raise Exception("Does not exists")
    return blob.content_type, blob.download_as_bytes()

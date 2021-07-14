from os import environ
STORAGE_METHOD = environ["STORAGE_METHOD"]
if STORAGE_METHOD == 'LOCAL':
    print("Using local storage")
    from modules.storage.filesystem import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
elif STORAGE_METHOD == 'GCLOUD':
    print("Using gcloud storage")
    from modules.storage.gcloud import (
        store_bytes,
        store_string,
        query_storage,
        get_storage_file
    )
else:
    raise Exception("Storage method not set")

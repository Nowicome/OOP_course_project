from Google import Create_Service
from googleapiclient.http import MediaFileUpload


client_secret_file = "credentials.json"
api_name = "drive"
api_version = "v3"
scopes = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(client_secret_file, api_name, api_version, scopes)


def create_folder(folder_name="new folder", parents=None):
    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    }
    if parents:
        file_metadata["parents"] = parents
    service.files().create(body=file_metadata).execute()
    return None


link = "https://sun9-80.userapi.com/impg/A1SYOgxHYozW9RJb9nz_" \
        "hm5YMDlzHYW9-jWFsg/SdrAdwLYi-A.jpg?" \
        "size=2560x1631&quality=95&sign=2c36245802cc6223a3a14d69acb53f5e&type=album"
# folder_id = ""
file_name = "new.jpg"
mime_type = "image/jpeg"
file_path = file_name
file_metadata = {
    "name": file_name,
    # "parents": [folder_id]
}

media = MediaFileUpload(file_path, mimetype=mime_type)
service.files().create(
    body=file_metadata,
    media_body=media,
    fields="id"
).execute()

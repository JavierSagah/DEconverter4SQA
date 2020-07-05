import requests
from tests.requests_helper import *

# action types include :
# token - to create a token
# import - to get the url to upload into

# this is the root url
url = "https://stage-wave.beaconama.net"
version = "v3"
token = ""
up_url = ""
file_url = ""
import_id = ""


# this method creates a token
def create_token(user, passw):
    post_url = "/token/" + version + "/get-token"
    payload = "{\n\"username\": \"" + user + "\",\n\"password\": \"" + passw + "\"\n}"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url + post_url, headers=headers, data=payload)
    pretty_print_response(response)

    response_body = response.json()

    global token
    token = response_body["access_token"]

    return response


# this method gets the url to upload into
def upload_url(import_type, uuid, filename, effective_time):
    put_url = "/import/" + version + "/" + uuid

    payload = "{\n\"filename\": \"" + filename + "\",\n\"effective_time\": \"" + effective_time + "\",\n\"import_type\": \"" + import_type + "\"\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("PUT", url + put_url, headers=headers, data = payload)

    pretty_print_request(response.request)

    pretty_print_response(response)

    response_body = response.json()

    global up_url
    up_url = response_body["upload_url"]
    global import_id
    import_id = response_body["import_id"]

    return response


# this method uploads the file into the url
def upload_file(filename):
    file_path = 'test_input/' + filename
    print("Uploading File: " + file_path)

    payload = {}
    file = open(file_path, 'rb')
    files = [
        ('filename', file)
    ]
    headers = {}

    response = requests.request("PUT", up_url, headers=headers, data = payload, files = files)
    file.close()

    # print(response.json())
    return response


# main method to de2
def de2_upload_de_file(user, passw, uuid, import_type, filename):
    create_token(user, passw)
    r2 = upload_url(import_type, uuid, filename, '')
    upload_file(filename)
    return r2

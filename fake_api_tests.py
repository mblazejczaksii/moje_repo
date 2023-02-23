# fake api tests related with 'Jenkins course for automation testers'
# Maciej Błażejczak MBQA

import asserts
import requests


class FakeApi:
    def __init__(self, protocol, address, port, resource, current_resource=None):
        self.protocol = protocol
        self.address = address
        self.port = port
        self.resource = resource
        self.current_resource = current_resource

    def __str__(self):
        return (f"New FakeApi created with parameters:\n"
                f"protocol: {self.protocol}\n"
                f"address: {self.address}\n"
                f"port: {self.port}\n"
                f"resource: {self.resource}\n"
                f"current resource: {self.current_resource}\n")

    def create_url(self):
        url = str(self.protocol + '://' + self.address + ':' + self.port + '/' + self.resource)
        return url

    def create_current_resource_url(self):
        url = self.create_url()
        return str(url + '/' + str(self.current_resource))


def send_get_request_to_endpoint(target_endpoint):
    re = requests
    response = re.get(url=target_endpoint)
    asserts.assert_equal(response.status_code, 200, f"Response code is {response.status_code} instead of 200")


def send_post_request_to_endpoint(target_endpoint):
    re = requests
    dict_body = {"body": "updated", "username": "mblazejczak", "postId": "1"}
    response = re.post(url=target_endpoint, data=dict_body)
    asserts.assert_equal(response.status_code, 201, f"Response code is {response.status_code} instead of 201")


def send_patch_request_to_endpoint(target_endpoint):
    re = requests
    dict_body = {"body": "patched"}
    response = re.patch(url=target_endpoint, data=dict_body)
    asserts.assert_equal(response.status_code, 200, f"Response code is {response.status_code} instead of 200")


endpoint_instance = FakeApi(protocol='http', address='localhost', port='3000', resource='comments')
current_endpoint_instance = FakeApi(protocol='http', address='localhost', port='3000', resource='comments',
                                    current_resource=2)
endpoint_url = endpoint_instance.create_url()
current_endpoint_url = current_endpoint_instance.create_current_resource_url()


# test1 - send get to endpoint - response 200 OK
def test_get_method():
    send_get_request_to_endpoint(target_endpoint=endpoint_url)


# test2 - send get to endpoint - response 201 OK
def test_post_method():
    send_post_request_to_endpoint(target_endpoint=endpoint_url)


# test3 - send get to endpoint - response 200 OK
def test_get_method_current_url():
    send_get_request_to_endpoint(target_endpoint=current_endpoint_url)


# test4 - send get to endpoint - response 200 OK
def test_patch_method():
    send_patch_request_to_endpoint(target_endpoint=current_endpoint_url)

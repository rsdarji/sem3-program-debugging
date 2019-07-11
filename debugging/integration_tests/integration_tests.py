import server
import urllib.request
import urllib.parse

# use server.start_server() to start the server
# use server.stop_server() to stop the server


def get_request(base_url, query):
    """
    Make a request at the given base url (string) using the query arguments (dict)
    """
    query_string = urllib.parse.urlencode(query)
    url = '{}?{}'.format(base_url, query_string)
    content = urllib.request.urlopen(url).read().decode()
    return content


def test_encrypt_endpoint():
    ...


def test_decrypt_endpoint():
    ...


def test_encrypt_and_decrypt():
    ...


def test_encrypt_decrypt_with_random_key():
    ...


if __name__ == "__main__":
    server.start_server()

    test_encrypt_endpoint()
    test_decrypt_endpoint()
    test_encrypt_and_decrypt()
    test_encrypt_decrypt_with_random_key()

    server.stop_server()
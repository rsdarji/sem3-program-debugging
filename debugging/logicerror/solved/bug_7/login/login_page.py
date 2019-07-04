import sqlite3
import http.server
import socketserver
import urllib.parse
import urllib.response

# Connect to our database
conn = sqlite3.connect('users.db')
c = conn.cursor()


def fetch_user_password(username):
    """Recover the password of the user"""
    user_password = c.execute("SELECT (password) FROM users WHERE username = ?", [username]).fetchone()
    return user_password


def validate_credentials(username, password):
    """Validate whether a username exists and has provided the correct password"""
    if password == fetch_user_password(username):
        return True
    else:
        return False


def login_response(query):
    """Determines the response to a user which has provided their username and password"""
    if validate_credentials(query['uname'], query['psw']):
        return "Welcome {}! You are now connected.".format(query['uname'])
    else:
        return "Connection error..."


class ServerHandler(http.server.SimpleHTTPRequestHandler):
    """Server handler class which handles the /login endpoint"""

    def do_GET(self):
        request = urllib.parse.urlparse(self.path)
        path = request.path

        if path == "/login":
            query = dict(urllib.parse.parse_qsl(request.query))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(login_response(query).encode())
        else:
            return super().do_GET()


if __name__ == "__main__":
    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS users"
              "(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)")

    # Create admin user if not exists
    admin_user = c.execute("SELECT * FROM users WHERE username='admin'").fetchone()
    if not admin_user:
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")

    conn.commit()

    # Start the server
    PORT = 8000
    httpd = socketserver.TCPServer(("", PORT), ServerHandler)
    print("[SERVER UP] open browser at 'localhost:{}'".format(PORT))
    httpd.serve_forever()

from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>LAPTOP CONFIGURATION</title>
    </head>
    <body>
        <h2>POOJA SHREE K</h2>
        <h2>REFERENCE NO :26018233</h2>
        <table border="1" cellspacing="5
        ">
<tr bgcolor="lightblue">
    <th>S.NO</th>
<th> Device name</th>
<th>Description</th>
<th>Physical address</th>
</tr>
<tr>
    <td>1</td>
    <td>Local area connection*1</td>
    <td>
        Microsoft Wi-Fi Direct Virtual Adapter
    </td><td>b8:f7:75:af:95:75
</td>
</tr>
<tr>
    <td>2</td>
<td>Local Area Connection* 2</td>
<td>Microsoft Wi-Fi Direct Virtual Adapter #2</td>
<td>ba:f7:75:af:95:74</td>
</tr>
<tr>
    <td>3</td>
    <td>Wi-Fi</td>
    <td>Intel(R) Wi-Fi 6</td>
    <td>b8:f7:75:af:95:74</td>
</tr>
<tr>
    <td>4</td>
    <td>Ethernet</td>
    <td>Realtek PCIe GbE Family Controller</td>
    <td>34:ia:4d:7c:80:c7</td>

</tr>
<tr>
    <td>5</td>
<td>
    Bluetooth Network connection
</td>
<td>
Bluetooth Device (Personal Area Network)
</td>
<td>
    b8:f7:75:af:95:78
</td></tr>

</table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
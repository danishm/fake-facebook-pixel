Fake Facebook Pixel
===

A simple project to serve as an endpoint for Facebook advertising pixel pings for development and debugging callouts made to `https://www.facebook.com/tr/?id=*******&ev=PageView`.

I created this to test and debug Facebook pixel integration without actually hitting Facebook.

How To Use
---

### Generate a Self Signed SSL Certificate

Since the endpoint has to be served from `https`, you will need to generate a self signed ssl certificate with the name `www.facebook.com` and "Always Trust" it locally. You will still see the browser warning that the site is "Not Secure", but it will work.

The following instructions are based on macOS Sierra

1. Open the "Keychain Access" application
2. Keychain Access > Certificate Assistant > Create a Certificate...
3. Assign Name as "www.facebook.com", Identity Type as "Self Signed Root", Certificate Type as "SSL Server"
4. Click "Create", "Continue" and "Done" as required
5. Find the newly created certificate in Keychain Access
6. Double Click and select "Always Trust" under Trust > When using this certificate. Clost window
7. Right Click on the certificate and select "Export ......"
8. Save the .p12 file in the same folder as `server.py`
9. Convert it to the .pem format using the command `openssl pkcs12 -in www.facebook.com.p12 -out www.facebook.com.pem -nodes`

### Modify You Hosts File

`vim /private/etc/hosts`

Add `www.facebook.com` as an alias for `127.0.0.1`

`127.0.0.1		localhost www.facebook.com`

The reason why this works out is because the actual Facebook tag that implements the `fbq` function is loaded from `connect.facebook.net`, which is not in the hosts file. Hence, the plumbing loades succesfully. 

The `https://www.facebook.com/tr/` endpoint is used for pinging the pixel, which we are intercepting and simply logging!

### Make Sure Port `80` is Open

On macOS Sierra, I had to make sure

  * Firewall was turned off
  * The default `https` service was stopped `sudo apachectl stop`

### Launch Server

`sudo python server.py`

*sudo is required to serve on port `80`*

### Start Debugging!

Lauch the page you want to test debug and as it loades and pings the Facebook pixel, you will see the query and parameter details on the STDOUT from `server.py`


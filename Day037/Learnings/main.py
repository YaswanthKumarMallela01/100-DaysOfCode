import requests

"""
Method 	            Purpose	                                    CRUD Operation	             Idempotent
GET	      Retrieves data from the server.	                         Read	                     Yes

POST	 Sends data to the server to create a new resource.	        Create	                      No

PUT	      Replaces or update an existing resource entirely 
           (or creates it if it does not exist).	                Update	                      Yes
           
DELETE	Removes the specified resource from the server.	            Delete	                      Yes
"""

"""
HTTP headers are key-value pairs of metadata sent with HTTP requests and responses, 
providing essential context like content type, caching rules, authorization, and more, 
helping clients and servers communicate efficiently and securely.
"""

import xmlrpclib
import struct, os
import webbrowser
import sys
import subprocess

def HashFile(name): 
      try: 
                 
                longlong = 'q'
                bytesize = struct.calcsize(longlong) 
                    
                f = open(name, "rb") 
                    
                filesize = os.path.getsize(name) 
                hash = filesize 

                 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlong, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF
                         
    
                f.seek(max(0,filesize-65536),0) 
                for x in range(65536/bytesize): 
                        buffer = f.read(bytesize) 
                        (l_value,)= struct.unpack(longlong, buffer)  
                        hash += l_value 
                        hash = hash & 0xFFFFFFFFFFFFFFFF 
                 
                f.close() 
                returnedhash =  "%016x" % hash 
                return returnedhash 
    
      except(IOError): 
                return "IOError"
            

server_url = 'http://api.opensubtitles.org/xml-rpc';
server = xmlrpclib.Server(server_url);


info = server.LogIn("", "", "eng", "OS Test User Agent");
token = info['token']

Size = os.path.getsize(sys.argv[1])
Hash = HashFile(sys.argv[1])
Language = "eng"

array = [{'sublanguageid': Language, 'moviehash':Hash,'moviebytesize':str(Size)}]


data = server.SearchSubtitles(token, array)
d = data['data']
d = d[0]
link = d['ZipDownloadLink']


subprocess.Popen(r'"' + os.environ["PROGRAMFILES"] + '\Internet Explorer\IEXPLORE.EXE"' + link)
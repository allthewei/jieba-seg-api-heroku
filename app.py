from flask import Flask
from flask import request
import jieba, json
# import importlib  
# import sys  

# importlib.reload(sys) 
     
app = Flask(__name__)

@app.route("/seg", methods=['POST', 'GET'])
def jieba_seg():
    if not request.args.get('q'):
        return packJsonReturn(-1, 'no seg text')
    
    # text = 'text'.encode('utf-8')
    segs = jieba.lcut(request.args.get('q'))
    if not segs:
        return packJsonReturn(-2, 'no seg result')
        
    return packJsonReturn(0, 'ok', segs)


def packJsonReturn(resCode=0, resMsg='ok', resData=None):
    return json.dumps({'resCode':resCode, 'resMsg':resMsg, 'resData':resData}, 
                      ensure_ascii=False).encode('utf-8')
    
if __name__ == "__main__":
    jieba.initialize()
    app.run()
from flask import Flask, render_template, Response
import io
import time
app = Flask(__name__)

FRAME_RATE = 60 #60 Frames per second

def gen():
    #returned a generator
    while True:
      time.sleep(1/FRAME_RATE)
      for i in images_bytes:
          yield (b'--jpgboundary'
          b'Content-type: image/jpeg\r\n\r\n' + 
          i + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/source.mjpg')
def feed_stream():
    #Response is a object
    #Streaming Contents
    #http://flask.pocoo.org/docs/0.12/patterns/streaming/
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=--jpgboundary') 

if __name__ == '__main__':

  #read out .jpeg files in binary format
  file_list = ['./images/{}.jpeg'.format(x) for x in range(1,10)]
  images_bytes = map(lambda x: open(x,"rb").read(),file_list)

  print "run"
  app.run(host='127.0.0.1', port=8000, debug=True)


 
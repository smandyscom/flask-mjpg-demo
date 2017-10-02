from flask import Flask, render_template, Response
import io,cv2
import random
import time
app = Flask(__name__)

#stream like
#output = io.BytesIO() 

def gen():
    #this object returned a generator
    while True:
      for i in images_bytes:
          yield (b'--jpgboundary'
          b'Content-type: image/jpeg\r\n\r\n' + 
          i + b'\r\n')

def gen_random():
  #why generator effected only?
  while True:
    time.sleep(0.04)
    yield (b'--jpgboundary'
          b'Content-type: image/jpeg\r\n\r\n' + 
          images_bytes[random.randint(0,len(images_bytes)-1)] + b'\r\n') 

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

@app.route('/source.mjpg')
def feed_stream():
    print("Response")
    #Response is a object
    #may detect generator then decide what's end of response context
    #streaming
    #only one stream available
    return Response(gen_random(),mimetype='multipart/x-mixed-replace; boundary=--jpgboundary') 

@app.route('/source2.mjpg')
def feed_stream_2():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=--jpgboundary') 


if __name__ == '__main__':

  #read out .jpeg files in binary format
  file_list = ['./images/{}.jpeg'.format(x) for x in range(1,10)]
  images_bytes = map(lambda x: open(x,"rb").read(),file_list)

  print "run"
  app.run(host='127.0.0.1', port=8000, debug=True)


 
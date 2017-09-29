from flask import Flask, render_template, Response
import io,cv2
app = Flask(__name__)

#stream like
#output = io.BytesIO() 

def gen():
    #this object returned a generator
    while True:
      for i in images_bytes:
          yield (b'--jpgboundary'
          b'Content-type: image/jpeg\r\n\r\n' + i + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/source.mjpg')
def feed_stream():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=--jpgboundary') 


if __name__ == '__main__':

  file_list = ['./images/{}.jpeg'.format(x) for x in range(1,10)]
  #images = map(lambda x: cv2.imread(x),file_list)
  images_bytes = map(lambda x: open(x,"rb").read(),file_list)

  app.run(host='127.0.0.1', port=8000, debug=True)
 
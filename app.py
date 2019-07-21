from sys import stdout

import logging
import cv2
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from drumset_flask_api.camera import Camera
from drumset_flask_api.utils import base64_to_pil_image, pil_image_to_base64
from drumset_flask_api.test import DrumSet
from drumset_flask_api.makeup_artist import Makeup_artist
# from camera import Camera
# from utils import base64_to_pil_image, pil_image_to_base64
# from test import DrumSet
# from makeup_artist import Makeup_artist

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
# app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app, engineio_logger=True, logger=True)
# print('Test make up', Makeup_artist())
camera = Camera(Makeup_artist())


src = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"></script>
<script>
const socket = io();
socket.on('connect', function(){
  console.log('Connected');
  setTimeout(function() {socket.emit('msg', 2);}, 1000);
});
</script>
"""

@socketio.on('input image', namespace='/test')
def test_message(input):
    input = input.split(",")[1]
    camera.enqueue_input(input)
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")


@app.route('/test')
def test():
    """Video streaming home page."""
    return src


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""

    app.logger.info("starting to generate frames!")
    while True:
        # frame = camera.get_frame() #pil_image_to_base64(camera.get_frame())
        # # processed_frmae = DrumSet.getFrame(frame)
        # # yield (b'--frame\r\n'
        # #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        success, frame = camera.get_frame()   # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    socketio.run(app)



# from flask import Flask, render_template, Response
# import cv2
# from drumset_flask_api.camera import Camera
# from drumset_flask_api.makeup_artist import Makeup_artist
# from flask_socketio import SocketIO
# from drumset_flask_api.test import DrumSet
#
# app = Flask(__name__)
# camera = Camera(Makeup_artist())
# # camera = cv2.VideoCapture(0)  # use 0 for web camera
# #  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
#
# def gen_frames():  # generate frame by frame from camera
#     while True:
#         # Capture frame-by-frame
#         # success, frame = camera.read()  # read the camera frame
#         # print("frame1 ::", type(frame))
#         success, frame = camera.get_frame()
#         # processed_frame = DrumSet.getFrame( frame)
#         # print("frame2 ::", type(processed_frame))
#         if not success:
#             break
#         else:
#             # processed_frame = DrumSet.getFrame(frame)
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
#
#
# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen_frames(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



# from sys import stdout
# from makeup_artist import Makeup_artist
# import logging
# from flask import Flask, render_template, Response
# from flask_socketio import SocketIO
# from camera import Camera
# from utils import base64_to_pil_image, pil_image_to_base64
#
#
# app = Flask(__name__)
# app.logger.addHandler(logging.StreamHandler(stdout))
# app.config['SECRET_KEY'] = 'secret!'
# app.config['DEBUG'] = True
# socketio = SocketIO(app)
# camera = Camera(Makeup_artist())
#
#
# @socketio.on('input image', namespace='/test')
# def test_message(input):
#     input = input.split(",")[1]
#     camera.enqueue_input(input)
#     #camera.enqueue_input(base64_to_pil_image(input))
#
#
# @socketio.on('connect', namespace='/test')
# def test_connect():
#     app.logger.info("client connected")
#
#
# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')
#
#
# def gen():
#     """Video streaming generator function."""
#
#     app.logger.info("starting to generate frames!")
#     while True:
#         frame = camera.get_frame()
#         print(frame)#pil_image_to_base64(camera.get_frame())
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
#
# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# if __name__ == '__main__':
#     socketio.run(app)

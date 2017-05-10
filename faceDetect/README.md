# FacePlusPlus Python SDK

This is the Face++ python SDK suite. Note that python2.7 is required.

## 1. cmdtool.py
This is an interactive command line tool which could be used to experiment
with Face++ APIs. It is recommended to have ipython installed so that you can
have tab-completion and some other nice features.

First please put your API key/secret in apikey.cfg. Then you can start the program
and you will drop into a python shell, where you can write something like:

    api.detect(image_file = File(r'<path to the image file>'))

Note that `api` here is a global variable.

## 2. call.py
This is a comprehensive demo for Face++ APIs. See the comments in the source
code for details.

## 3. facepp.py

This is the underlying API implementation.

# FaceDetect

Note that opencv for python is required. I use steps as below :

    sudo apt-get install build-essential
    sudo apt-get update
    sudo apt-get upgrade
    sudo rpi-update
    sudo reboot
    sudo apt-get install libopencv-dev
    sudo apt-get install python-opencv
    sudo apt-get install python-numpy libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev libdc1394-22-dev
    
Now your environment is OK.

## 1. capture_test.py
This is a sample to read a frame of usb-camera.

## 2. detect_test.py
This is a sample to check faces in pictures.

## 3. search.py

This is a sample to use FacePlusPlus Python SDK like `call.py`, actually it is.
But because of the network(`CONCURRENCY_LIMIT_EXCEEDED`) and some strange error in `api.search`(`IndexError: list index out of range`), 
I changed `facepp.py` as below :

    except urllib2.HTTPError as e:
        print '***network limited!'
        continue
        raise APIError(e.code, url, e.read())
        
and where we use `api.search`, can modify like :
    
    try:
        search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id='test')
    except:
        print '***picture is not good!'
        continue

## 4. faceDetect.py

The code to capture usb-camera, detect faces and search the face in faceset.
In order to ensure real-time, I used a thread to capture usb-camera. 

# Use Other Apps

I provide a way to use other apps in FacePlusPlus as below:
1. change the link address, such as detectsceneandobject(`api_server_china = 'https://api-cn.faceplusplus.com/imagepp/beta/'`)
2. you should modify `facepp.py`:
```python
server = 'https://api-cn.faceplusplus.com/imagepp/beta/'
```    
```python
_APIS = [
    '/detect',
    '/compare',
    '/search',
    '/faceset/create',
    '/faceset/addface',
    '/faceset/removeface',
    '/faceset/update',
    '/faceset/getdetail',
    '/faceset/delete',
    '/faceset/getfacesets',
    '/face/analyze',
    '/face/getdetail',
    '/face/setuserid',
	'/detectsceneandobject'
]
```
3. use api like:
```python
api.detectsceneandobject(image_file=File('./thingset/lab.png'))
```

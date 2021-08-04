import ctypes
import numpy as np

uEyeDll = ctypes.cdll.LoadLibrary("C:\\Windows\\System32\\uEye_api_64.dll") #include full path or copy dll into same folder as .py script


#connect camera
cam = ctypes.c_uint32(0)
hWnd = ctypes.c_voidp()
msg=uEyeDll.is_InitCamera(ctypes.byref(cam),hWnd)
ErrChk=uEyeDll.is_EnableAutoExit (cam, ctypes.c_uint(1))
if ~ErrChk:
    print (' Camera Connected')
IS_CM_SENSOR_RAW8  =ctypes.c_int(11)
nRet = uEyeDll.is_SetColorMode(cam,IS_CM_SENSOR_RAW8)
IS_SET_TRIGGER_SOFTWARE = ctypes.c_uint(0x1000)
nRet = uEyeDll.is_SetExternalTrigger(cam, IS_SET_TRIGGER_SOFTWARE)


#allocate memory
width_py = 1600
height_py = 1200
pixels_py =8

width = ctypes.c_int(width_py) #convert python values into c++ integers
height = ctypes.c_int(height_py) 
bitspixel=ctypes.c_int(pixels_py)
pcImgMem = ctypes.c_char_p() #create placeholder for image memory
pid=ctypes.c_int()

ErrChk=uEyeDll.is_AllocImageMem(cam, width, height,  bitspixel, ctypes.byref(pcImgMem), ctypes.byref(pid))
if ~ErrChk:
    print (' Success')
else:
    print (' Memory allocation failed, no camera with value' +str(cam.value))


# Get image data    
uEyeDll.is_SetImageMem(cam, pcImgMem, pid)
ImageData = np.ones((height_py,width_py),dtype=np.uint8)
print(ImageData)
# #put these lines inside a while loop to return continous images to the array "ImageData"  
# uEyeDll.is_FreezeVideo (cam, ctypes.c_int(0x0000))  #IS_DONT_WAIT  = 0x0000, or IS_GET_LIVE = 0x8000
# uEyeDll.is_CopyImageMem (cam, pcImgMem, pid, ImageData.ctypes.data) 
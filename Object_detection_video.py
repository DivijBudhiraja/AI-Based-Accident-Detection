
import os
import cv2
import numpy as np
import tensorflow as tf

import sys


sys.path.append("..")


from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
Region=input("Enter the accident prone region(H/M/L):");


MODEL_NAME = 'inference_graph'
VIDEO_NAME = r'C:/Users/djbud/Desktop/Accident-detection-system-main/acci.mp4'


CWD_PATH = os.getcwd()


PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')


PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')


PATH_TO_VIDEO = os.path.join(CWD_PATH,VIDEO_NAME)


NUM_CLASSES = 6


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef() 
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.compat.v1.Session(graph=detection_graph)


image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')


detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')


detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')


num_detections = detection_graph.get_tensor_by_name('num_detections:0')


video = cv2.VideoCapture(PATH_TO_VIDEO)


while(video.isOpened()):

    
    ret, frame = video.read()
    frame_expanded = np.expand_dims(frame, axis=0)

    #frame delays-part3
    
    

    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    
    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.80)
    
    cv2.imshow('Object detector', frame)

    #video.set(cv2.CAP_PROP_POS_MSEC,5) 
    if cv2.waitKey(1) == ord('q'):
        break


#Frame delay-part3
def getFrame(sec): 
   video.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
   hasFrames,image = video.read() 
   if hasFrames: 
       cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file 
   return hasFrames

if Region=="H":
    frameRate=50;
elif Region=="M":
    frameRate=100;
elif Region=="L":
    frameRate=150;

sec = 0 
success = getFrame(sec) 
while success: 
   sec = sec + frameRate 
   sec = round(sec, 2) 
   success = getFrame(sec)


video.release()
cv2.destroyAllWindows()

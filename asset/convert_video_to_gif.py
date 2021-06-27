from moviepy.editor import *

clip=(VideoFileClip(r"pred_complex_yolo_v4.avi"))
        # .resize(0.45))
clip.write_gif("pred_complex_yolo_v4.gif")
# clip = (VideoFileClip("frozen_trailer.mp4")
#         .subclip((1,22.65),(1,23.2))
#         .resize(0.3))
# clip.write_gif("Pred_street.gif")
print("Conversion completed")
"""

import imageio
import os

def convertVideoToGifFile(inputFile, outputFile=None):	
    if not outputFile:
        outputFile = os.path.splitext(inputFile)[0] + ".gif"
		
    print("Converting {0} to {1}".format(inputFile, outputFile))

    reader = imageio.get_reader(inputFile)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputFile, fps=fps)
	
    for i,im in enumerate(reader):
        writer.append_data(im)

    writer.close()
	
    print("\r\nConversion done.")

# Convert Input Files
# convertVideoToGifFile("sample_960x540.avi")
convertVideoToGifFile("Pred_street.mp4", "Pred_street.gif")
"""
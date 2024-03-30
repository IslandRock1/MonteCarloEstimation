import cv2
import os

def make(antall):
    frameSize = (1920, 1080)
    name = 1
    while True:
        path = f"videos\{name}.avi"
        if not os.path.exists(path):
            break
        name += 1

    out = cv2.VideoWriter(f'videos\{name}.avi', cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)
    for i in range(1, antall, 1):
        if i % 50 == 0:
            print(i)
        
        q = cv2.imread(f"images\{i}.png") # Used to be jpeg..
        out.write(q)
    
    out.release()
    
def delete():
    i = 0
    while True:
        if i % 100 == 0:
            print(i)
        
        try:
            os.remove(f"images\Frame{i}.jpeg")
        except Exception:
            break

        i += 1

make(6000)
# delete()
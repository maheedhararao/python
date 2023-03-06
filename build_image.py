import os, time

images_before = os.popen("sudo docker images").read().strip().split("\n")[1:]
print(images_before)
os.popen("sudo docker build -t ubuntu:v1 /home/remlab/demo")
time.sleep(5)
images_after = os.popen("sudo docker images").read().strip().split('\n')[1:]
print(images_after)
if images_after <= images_before:
    raise Exception('Image creation is unsuccessful')

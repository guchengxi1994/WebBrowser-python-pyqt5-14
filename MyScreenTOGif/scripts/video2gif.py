'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-08 10:21:41
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-08 11:31:42
'''
import cv2
import os
import imageio
from PIL import Image


def compressImg(imgName):
    im = Image.open(imgName)
    im.convert('RGB')
    
    im.thumbnail((int(im.shape[0]*0.25),int(im.shape[1]*0.25)))
    return im


def extract_image_from_video(video_path_name=None, img_dir='img/', cap_fps=1):
    '''
    从视频中提取图片
    :param video_path_name: 视频文件全路径
    :param img_dir: 截图存放文件夹路径
    :param cap_fps: 每秒截图数量
    :return:
    '''
    # 创建文件夹用于保存从video中提取的图像
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    else:
        for file_name in os.listdir(img_dir):
            os.remove(img_dir + file_name)
 
    cap = cv2.VideoCapture(video_path_name)  # 打开视频文件
    # 视频文件的一些信息（name，fps，size）
    video_name = ''.join(video_path_name.split(os.sep)[-1].split('.')[:-1])
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Video info : ', {'name': video_name, 'fps': fps, 'size': size})
 
    temp = fps // cap_fps  # 根据每秒视频提取图片数计算何时保存视频文件
    frame_nb = 1  # 当前视频帧数
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # 以下被注释语句用于显示视频
            # cv2.imshow('frame', frame)
            if frame_nb % temp == 0:
                # 保存视频当前帧， 文件名应按字符大小升序保存
                print(img_dir + video_name + '%3d.png' % frame_nb)
                
                cv2.imwrite(img_dir + video_name + '%3d.png' % frame_nb, frame)
        else:
            break
        frame_nb += 1
 
    cap.release()
    cv2.destroyAllWindows()


def make_gif(gif_name='new.gif', duration=0.1,img_dir = "img/"):
    '''
    通过截图得到 *.gif文件
    :param gif_name: 存放gif文件全路径
    :param duration: gif中每一张图片（每一帧）持续时间
    :return:
    '''
    image_list = [img_dir + img_name for img_name in os.listdir(img_dir)]
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
 
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)



if __name__ == '__main__':
    extract_image_from_video("D:\\testALg\\WebBrowser-python-pyqt5-14\\MyScreenTOGif\\scripts\\2020-05-08 10-20-12.avi")
    make_gif()
from PIL import Image, ImageDraw, ImageFont
import os



interval=17
width = 60
height = 30
#四种颜色
tr1=[(255, 135, 0),(255,110,0),(255,74,0),(255,58,0),(255,45,0),(255,37,0),(255,22,0),(230,0,0),(202,0,11),(159,2,54),(111,22,113),(81,42,160),(80,88,209),(80,135,252),(80,175,255),(80,196,255),(80,227,255),(80,253,255)]
trblue1=[(80,211,243),(86,213,244),(95,216,246),(100,218,248),(110,222,250),(120,227,252),(130,229,253),(140,233,255),(152,237,255),(160,239,255),(171,242,255),(181,248,255),(191,252,255),(203,254,255),(211,255,255),(217,255,255),(225,255,255),(230,255,255)]
tr2=[(255,16,0),(255,69,0),(255,145,0),(255,180,0),(255,207,0),(255,227,0),(241,245,0),(194,253,0),(157,255,12),(103,255,54),(41,255,110),(2,255,153),(0,245,197),(0,225,235),(0,185,255),(0,140,255),(0,78,255),(0,26,255)]
trblue2  =[(0,54,228),(9,61,229),(20,70,230),(27,75,231),(40,85,233),(54,96,235),(65,105,236),(78,116,238),(95,129,240),(105,137,241),(118,147,242),(131,157,244),(145,168,246),(158,178,247),(169,187,249),(177,194,250),(187,202,251),(194,207,252)]

color_data=[tr1,tr2,trblue1,trblue2]
color_names=['tr1','tr2','trblue1','trblue2']


if not os.path.exists('picture'):
    os.mkdir('picture')

# 生成验证码和图片
print('1、tr1    2、tr2   3、trblue1   4、trblue2')
index=int(input('输入序号：'))-1
color_bar=color_data[index]
color_name=color_names[index]
min_speed=input('输入最小风速：')
max_speed=input('输入最大风速：')
begin=int(min_speed)
end=int(max_speed)

for i in range(interval+1):

    image = Image.new('RGB', (width, height), color_bar[i])
    # 创建Font对象
    font = ImageFont.truetype('arial.ttf', 18)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    if i==0:
        img_str='<'+str(begin)
    elif i==interval:
        img_str='>'+str(end)
    else:
        img_str=round((begin+(end-begin)/interval*i),2)

    tmp = str(img_str)
    draw.text((14 , 5), tmp, font=font, fill=(0,0,0))
    image.save('picture/code' + str(i) + '.png', 'png')
    print('正在打印第{}张图片'.format(str(i)))
print('结束')


# 参数初始化
# 每行每列显示图片数量
line_max = 1
row_max = interval+1
all_path = []
num = 0
pic_max = line_max * row_max
dirName = os.getcwd()

all_picture=[dirName+'/'+'picture/code{}.png'.format(i) for i in range(interval+1)]
toImage = Image.new('RGBA', (width * line_max, height * row_max))

for j in range(0, row_max):
    pic_fole_head = Image.open(all_picture[num])
    # tmppic = pic_fole_head.resize((width, height))
    loc = ( 0,int(j * height))
    print("第" + str(num) + "存放位置" + str(loc))
    toImage.paste(pic_fole_head, loc)
    num = num + 1
    if num >= len(all_picture):
        print("break")
        break

print(toImage.size)
toImage.save(dirName+'/picture/{}_{}_{}.png'.format(color_name,str(min_speed),str(max_speed)))
import math, copy

img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]

def up(img):
    img_next = copy.deepcopy(img[1:])
    img_next.append(len(img[0])*[0])
    return img_next

def down(img):
    img_next = copy.deepcopy(img[:-1])
    img_next.insert(0, len(img[0])*[0])
    return img_next

def left(img):
    img_next = len(img)*[[]]
    for i in range(len(img_next)):
        img_next[i] = img[i][1:] + [0]
    return img_next

def right(img):
    img_next = len(img)*[[]]
    for i in range(len(img_next)):
        img_next[i] = [0] + img[i][:-1]
    return img_next

translated_images = [[]]

def generate_translated_images(img):
    if img not in translated_images[0]:
        translated_images[0] += [img]

        for i in range(4):
            if i == 0:
                generate_translated_images(up(img))
            elif i == 1:
                generate_translated_images(down(img))
            elif i == 2:
                generate_translated_images(right(img))
            elif i == 3:
                generate_translated_images(left(img))

generate_translated_images(img1)
#print(translated_images)

def count_overlapping(image1, image2):
    overlapped_cnt = 0
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            if image1[i][j]==1 and image1[i][j] == image2[i][j]:
                overlapped_cnt += 1
    return overlapped_cnt

max_cnt = 0
for image in translated_images[0]:
    max_cnt = max(max_cnt, count_overlapping(image, img2))

print(max_cnt)

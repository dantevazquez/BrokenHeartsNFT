from PIL import Image
import random

NUM_NFTS = 5
NUM_ATTRIBUTES = 0

def createImage(crown, heart, leftHand, rightHand, shoes, name):
 
    merge1 = Image.alpha_composite(crown, heart)
    merge2 = Image.alpha_composite(merge1, leftHand)
    merge3 = Image.alpha_composite(merge2, rightHand)
    finalMerge = Image.alpha_composite(merge3, shoes)
    finalMerge.save("broken_heart_" + name + ".png")

def getRandomCrown(crown):
    return crown[random.randint(0, NUM_ATTRIBUTES)]

def getRandomHeart(heart):
    return heart[random.randint(0, NUM_ATTRIBUTES)]

def getRandomLeftHand(leftHand):
    return leftHand[random.randint(0, NUM_ATTRIBUTES)]

def getRandomRightHand(rightHand):
    return rightHand[random.randint(0, NUM_ATTRIBUTES)]

def getRandomShoes(shoes):
    return shoes[random.randint(0, NUM_ATTRIBUTES)]

#crowns
crown = [
    Image.open(r"./attributes/crowns/crown_1.png")
    # crown[1] = Image.open(r"./attributes/crowns/crown_2.png")
    # crown[2] = Image.open(r"./attributes/crowns/crown_3.png")
    # crown[3] = Image.open(r"./attributes/crowns/crown_4.png")
    # crown[4] = Image.open(r"./attributes/crowns/crown_5.png")
    # crown[5] = Image.open(r"./attributes/crowns/crown_6.png")
    # crown[6] = Image.open(r"./attributes/crowns/crown_7.png")
    # crown[7] = Image.open(r"./attributes/crowns/crown_8.png")
    # crown[8] = Image.open(r"./attributes/crowns/crown_9.png")
    # crown[9] = Image.open(r"./attributes/crowns/crown_10.png")
]


#hearts
heart = [
    Image.open(r"./attributes/hearts/heart_1.png")
    # heart[1] = Image.open(r"./attributes/hearts/heart_2.png")
    # heart[2] = Image.open(r"./attributes/hearts/heart_3.png")
    # heart[3] = Image.open(r"./attributes/hearts/heart_4.png")
    # heart[4] = Image.open(r"./attributes/hearts/heart_5.png")
    # heart[5] = Image.open(r"./attributes/hearts/heart_6.png")
    # heart[6] = Image.open(r"./attributes/hearts/heart_7.png")
    # heart[7] = Image.open(r"./attributes/hearts/heart_8.png")
    # heart[8] = Image.open(r"./attributes/hearts/heart_9.png")
    # heart[9] = Image.open(r"./attributes/hearts/heart_10.png")
]


#left hands
leftHand = [
    Image.open(r"./attributes/left_hands/left_hand_1.png")
    # leftHand[1] = Image.open(r"./attributes/left_hands/left_hand_2.png")
    # leftHand[2] = Image.open(r"./attributes/left_hands/left_hand_3.png")
    # leftHand[3] = Image.open(r"./attributes/left_hands/left_hand_4.png")
    # leftHand[4] = Image.open(r"./attributes/left_hands/left_hand_5.png")
    # leftHand[5] = Image.open(r"./attributes/left_hands/left_hand_6.png")
    # leftHand[6] = Image.open(r"./attributes/left_hands/left_hand_7.png")
    # leftHand[7] = Image.open(r"./attributes/left_hands/left_hand_8.png")
    # leftHand[8] = Image.open(r"./attributes/left_hands/left_hand_9.png")
    # leftHand[9] = Image.open(r"./attributes/left_hands/left_hand_10.png")
]


#right hands
rightHand = [
    Image.open(r"./attributes/right_hands/right_hand_1.png")
    # rightHand[1] = Image.open(r"./attributes/right_hands/right_hand_2.png")
    # rightHand[2] = Image.open(r"./attributes/right_hands/right_hand_3.png")
    # rightHand[3] = Image.open(r"./attributes/right_hands/right_hand_4.png")
    # rightHand[4] = Image.open(r"./attributes/right_hands/right_hand_5.png")
    # rightHand[5] = Image.open(r"./attributes/right_hands/right_hand_6.png")
    # rightHand[6] = Image.open(r"./attributes/right_hands/right_hand_7.png")
    # rightHand[7] = Image.open(r"./attributes/right_hands/right_hand_8.png")
    # rightHand[8] = Image.open(r"./attributes/right_hands/right_hand_9.png")
    # rightHand[9] = Image.open(r"./attributes/right_hands/right_hand_10.png")
]


#shoes
shoes = [
    Image.open(r"./attributes/shoes/shoes_1.png")
    # shoes[1] = Image.open(r"./attributes/shoes/shoes_2.png")
    # shoes[2] = Image.open(r"./attributes/shoes/shoes_3.png")
    # shoes[3] = Image.open(r"./attributes/shoes/shoes_4.png")
    # shoes[4] = Image.open(r"./attributes/shoes/shoes_5.png")
    # shoes[5] = Image.open(r"./attributes/shoes/shoes_6.png")
    # shoes[6] = Image.open(r"./attributes/shoes/shoes_7.png")
    # shoes[7] = Image.open(r"./attributes/shoes/shoes_8.png")
    # shoes[8] = Image.open(r"./attributes/shoes/shoes_9.png")
    # shoes[9] = Image.open(r"./attributes/shoes/shoes_10.png")
]

for x in range(NUM_NFTS):
    createImage(getRandomCrown(crown), getRandomHeart(heart), getRandomLeftHand(leftHand), getRandomRightHand(rightHand), getRandomShoes(shoes), str(x))


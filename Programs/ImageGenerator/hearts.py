#NFT GENERATOR FOR CLOUDKENT
#MADE BY DANTE VAZQUEZ

from PIL import Image
import random
import os

#Total number of png's you wanna create
NUM_NFTS = 1

#Number of images you have for each attribute
NUM_CROWNS = 1
NUM_HEARTS = 1
NUM_LEFT_HANDS = 1
NUM_RIGHT_HANDS = 1
NUM_SHOES = 1

#Directories for the attributes
CROWNS_DIR = "./attributes/crowns"
HEARTS_DIR = "./attributes/hearts"
LEFT_HANDS_DIR = "./attributes/left_hands"
RIGHT_HANDS_DIR = "./attributes/right_hands"
SHOES_DIR = "./attributes/shoes"

def createImage(crown, heart, leftHand, rightHand, shoes, name):
 
    merge1 = Image.alpha_composite(crown, heart)
    merge2 = Image.alpha_composite(merge1, leftHand)
    merge3 = Image.alpha_composite(merge2, rightHand)
    finalMerge = Image.alpha_composite(merge3, shoes)
    finalMerge.save("broken_heart_" + name + ".png")

def getRandomCrown(crown):
    return crown[random.randint(0, NUM_CROWNS - 1)]

def getRandomHeart(heart):
    return heart[random.randint(0, NUM_HEARTS - 1)]

def getRandomLeftHand(leftHand):
    return leftHand[random.randint(0, NUM_LEFT_HANDS - 1)]

def getRandomRightHand(rightHand):
    return rightHand[random.randint(0, NUM_RIGHT_HANDS - 1)]

def getRandomShoes(shoes):
    return shoes[random.randint(0, NUM_SHOES - 1)]

#load crowns
crown = []
for images in os.listdir(CROWNS_DIR):
    crown.append(Image.open(CROWNS_DIR + "/" + images))

#load hearts
heart = []
for images in os.listdir(HEARTS_DIR):
    heart.append(Image.open(HEARTS_DIR + "/" + images))

#load left hands
leftHand = []
for images in os.listdir(LEFT_HANDS_DIR):
    leftHand.append(Image.open(LEFT_HANDS_DIR + "/" + images))

#load right hands
rightHand = []
for images in os.listdir(RIGHT_HANDS_DIR):
    rightHand.append(Image.open(RIGHT_HANDS_DIR + "/" + images))

#load shoes
shoes = []
for images in os.listdir(SHOES_DIR):
    shoes.append(Image.open(SHOES_DIR + "/" + images))

#main loop to create NFTS
for x in range(NUM_NFTS):
    createImage(getRandomCrown(crown), getRandomHeart(heart), getRandomLeftHand(leftHand), 
    getRandomRightHand(rightHand), getRandomShoes(shoes), str(x + 1))
    
    print("NFT CREATED: " + str(x + 1))

if NUM_NFTS == 1:
    print("Succesfully created " + str(NUM_NFTS) + " NFT")

else:
    print("Succesfully created " + str(NUM_NFTS) + " NFTs")

#EOP
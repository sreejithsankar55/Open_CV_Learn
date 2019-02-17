import cv2

def main():

    imgpath = "/home/sreejith/Pictures/sreejith2.png"
    img = cv2.imread(imgpath,0)

    outpath = "/home/sreejith/Desktop/sreejith2.jpg"
    
    cv2.imshow('Lena',img)
    cv2.imwrite(outpath,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

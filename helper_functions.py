
import numpy as np

from skimage import transform
from skimage.util.shape import view_as_blocks


def tran(t):
    T={'B':0,'b':1,'K':2,'k':3,'Q':4,'q':5,'R':6,'r':7,'P':8,'p':9,'N':10,'n':11,'F':12}
    return T[t]

def tran_t(t):
    T={0:'B',1:'b',2:'K',3:'k',4:'Q',5:'q',6:'R',7:'r',8:'P',9:'p',10:'N',11:'n'}
    return T[t]

SQUARE_SIZE = 40
downsample_size = SQUARE_SIZE * 8
square_size = SQUARE_SIZE

def split_chessboard_into_64_images(image):
    # img_read = cv2.imread(f"../input/chess-positions/dataset/{mode}/{image}",cv2.IMREAD_GRAYSCALE)
    img_read = transform.resize(image, (downsample_size, downsample_size), mode='constant')
    tiles = view_as_blocks(img_read, block_shape=(square_size, square_size))
    tiles =  tiles.reshape(64, square_size, square_size)
    return tiles.tolist()

def fen_from_onehot(one_hot):
    output = ''
    for j in range(8):
        for i in range(8):
            if(one_hot[j][i] == 12):
                output += ' '
            else:
                output += tran_t(one_hot[j][i])
        if(j != 7):
            output += '-'

    for i in range(8, 0, -1):
        output = output.replace(' ' * i, str(i))

    return output


if __name__ == "__main__":
    print('Hello')
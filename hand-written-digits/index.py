labelsPath = "./t10k-labels.idx1-ubyte"
imgPath = "./t10k-images.idx3-ubyte"

def toInt(_byte):
    return int.from_bytes(_byte, "big")

labelsf = open(labelsPath, "rb")
magicNumber= toInt(labelsf.read(4))
labelCount = toInt(labelsf.read(4))

imgsf = open(imgPath, "rb")
magicNumber2 = toInt(imgsf.read(4))
imgCount = toInt(imgsf.read(4))
imgRows = toInt(imgsf.read(4))
imgCollums = toInt(imgsf.read(4))


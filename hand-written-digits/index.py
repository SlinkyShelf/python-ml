labelsPath = "./t10k-labels.idx1-ubyte"
imgPath = "./t10k-images.idx3-ubyte"

def toInt(_byte):
    return int.from_bytes(_byte, "big")

labelsf = open(labelsPath, "rb")
magicNumber= toInt(labelsf.read(4))
labelCount = toInt(labelsf.read(4))
# for i in range(100):
#     print(toInt(labelsf.read(1)))

imgsf = open(imgPath, "rb")
magicNumber2 = toInt(imgsf.read(4))
imgCount = toInt(imgsf.read(4))
imgRows = toInt(imgsf.read(4))
imgCollums = toInt(imgsf.read(4))


# for i in range(imgRows):
#     row = ""
#     for j in range(imgCollums):
#         if toInt(imgsf.read(1)) < 128:
#             row += "█"
#         else:  
#             row += " "
#     print(row)

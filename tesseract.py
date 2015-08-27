import tesseract

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(tesseract.PSM_AUTO)

mImgFile = "eurotext.jpg"
mBuffer=open(mImgFile,"rb").read()
result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
print "result(ProcessPagesBuffer)=",result
intPtr=api.AllWordConfidences()
print str(intPtr)
pyPtrRaw=tesseract.cdata(intPtr,300)
print len(pyPtrRaw),len(mBuffer)
pyPtr=[ord(data) for i,data in enumerate(pyPtrRaw)]
print pyPtr
tesseract.delete_intp(intPtr) 

from datetime import datetime

class store:
   def __init__(self, delta):
      self.delta = delta
      self.dataDict = {}
      self.ordList = []
 
   def store(self, data, info):
      ob2store = [data,info]
      if data in self.dataDict:
         try:
            self.ordList.remove(self.dataDict[data])
         except ValueError:
            pass
      self.dataDict[data] = ob2store
      self.ordList.append(ob2store)

   def flush(self):
      self.ordList = []
      self.dataDict = {}

   def getIndex(self, pivot):
      endIndex = len(self.ordList)
      if endIndex == 0:
         return 0
      (d0,i0) = self.ordList[0]
      (dE,iE) = self.ordList[-1]
      if i0 > pivot:
         return 0
      if iE < pivot:
         return endIndex

      return self.getIndexRec(pivot, 0, endIndex)      

   def getIndexRec(self, pivot, startIndex, endIndex):
      if startIndex == endIndex:
         return startIndex

      median = (endIndex-startIndex)/2 +startIndex
      (data, info) = self.ordList[median]

      if info > pivot:
         return self.getIndexRec( pivot, startIndex, max(0,median-1) )
      if info < pivot:
         return self.getIndexRec( pivot, min(median+1,endIndex), endIndex )

      return median

   def getData(self, ref):
      self.ordList = self.ordList[self.getIndex(ref-self.delta):]
      if len(self.ordList) == 0:
         self.dataDict = {}
      return [ x for (x,y) in self.ordList ]


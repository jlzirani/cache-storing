from store import store


def store_test():
   s = store(2)
   s.store('a',0)
   assert s.getData(0) == ['a']   
   s.store('b',1)
   assert s.getData(0) == ['a','b']   
   s.store('c',2)
   s.store('d',3)
   assert s.getData(1) == ['a','b','c','d']   
   assert s.getData(2) == ['a','b','c','d']   
   assert s.getData(3) == ['b','c','d']   
   assert s.getData(4) == ['c','d']   
   s.store('a', 4)
   assert s.getData(5) == ['d','a']   
   assert s.getData(6) == ['a']
   assert s.getData(7) == []

def store_order():
   s = store(2)
   s.store('a',0)
   s.store('b',1)
   s.store('c',2)
   s.store('d',3)
   assert s.getData(0) == ['a','b','c','d']   
   s.store('a',4)
   assert s.getData(0) == ['b','c','d','a']   

def store_flush():
   s = store(1)
   s.store('a', 0)
   assert s.getData(0) == ['a']
   s.flush()
   assert s.getData(0) == []

if __name__=='__main__':
   store_test()
   store_flush()
   store_order()

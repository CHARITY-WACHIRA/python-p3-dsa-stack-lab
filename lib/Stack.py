class Stack:

    def __init__(self, items= [], limit = 100):
        self.list=items.copy()
        self.limit=limit

    def isEmpty(self):
        pass

    def push(self, item):
       if self.size()==self.limit:
           return
       self.list.append(item)

    def pop(self):
        if self.is_empty():
            return None
        
        return self.list.pop()
        

    def peek(self):
        if not self.is_empty():
            return self.list(-1)
        else: 
            return None
    
    def size(self):
        return len (self.list)

    def full(self):
        return len(self.list)==0

    def search(self, target):
        for i in range(len(self.list)-1,-1,-1):
            if self.list[i]== target:
                return len(self.list)-1 -i
            return -1

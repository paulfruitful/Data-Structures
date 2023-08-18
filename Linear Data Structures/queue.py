class Queue:
   def __init__(self):
     self.queue= []
 
   def enqueue(self,value):
      self.queue.append(value)

   def dequeue(self):
      self.queue.pop(0)
  
     




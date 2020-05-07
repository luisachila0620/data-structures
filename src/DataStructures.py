class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        self.__queue.append(item)
        pass
    def dequeue(self):
         self.__queue.pop(0)
        
    def get_queue(self):
        return self._queue
    def size(self):
        pass
class Foo:
    def __init__(self):
        self.isFirstFinished = False
        self.isSecondFinished = False
        self.lock = threading.Condition()
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        self.lock.acquire()
        printFirst()
        self.isFirstFinished = True
        self.lock.notifyAll()
        self.lock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock.acquire()
        while not self.isFirstFinished:
            self.lock.wait()
        printSecond()
        self.isSecondFinished = True
        self.lock.notifyAll()
        self.lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.lock.acquire()
        while not self.isSecondFinished:
            self.lock.wait()
        printThird()
        self.lock.release()

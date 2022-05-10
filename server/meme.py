import time

class Meme():

    __instances__ = 0

    def __init__(self) -> None:
        
        self.date_created = time.time()
        self.num_likes = 0
        self.num_views = 0
        self.bidding_price = 0
        self.uuid = self.__class__.__instances__ 

        self.__class__.__instances__ += 1


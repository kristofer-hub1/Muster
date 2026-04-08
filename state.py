class CombinationLock:
    def __init__(self, combination):
        self.combination = combination         
        self.entered = []              
        self.status = 'LOCKED'
        

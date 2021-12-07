class tile:
    # Constructors
    def __init__(self, isMine):
        self.isMine = isMine
        self.active = True
        self.value = 0
    
    # Tile-specific functions
    def excavate(self):
        self.active = False
    
    # Getters and Setters
    def set_value(self, value): self.value = value
    def get_value(self): return self.value
    def getIsMine(self): return self.isMine

    # Redifining existing functions
    def __str__(self):
        if self.active:
            return "_"
        else:
            if self.isMine:
                return "*"
            else:
                return "{}".format(self.value)

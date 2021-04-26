class NoMentions(Exception):
    """
    Exception raised when command needs mentions but no mentions are given.
    
    :params:
        message:str -- custom message
    """
    def __init__(self, message:str=None):
        self.message = message if isinstance(message, str) else "Message does not contain any mentions"
        super().__init__(self.message)
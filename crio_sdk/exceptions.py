class CrioAPIError(Exception):
    """Raises error message for API failures"""
    def __init__(self, message:str, status_code:int=None, response_body:dict=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        
    def __repr__(self):
        return f"CrioAPIError (status_code={self.status_code}, message={super().__str__()!r})"
        

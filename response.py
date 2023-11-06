class PokemonResponse(object):
    def __init__(self, status: str, message: str, data: any) -> None:
        self.status = status
        self.message = message
        self.data = data
        
    @staticmethod
    def getSuccessMessage(message: str, data: any = []):
        return PokemonResponse('ok', message, data)
    
    @staticmethod
    def getErrorMessage(message: str, details: any = []):
        return PokemonResponse('error', message, details)
    
    def to_dict(self) -> dict:
        return {
            'status': self.status,
            'message': self.message,
            'data': self.data
        }
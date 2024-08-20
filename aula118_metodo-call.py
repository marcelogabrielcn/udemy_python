class CallMe: 
    def __init__(self, phone) -> None:
        self.phone = phone

    
    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
    

call01 = CallMe('11928843728')
call01('Marcelo')

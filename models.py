from datetime import date

class Lead:
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = date.today().isoformat()

    def model_lead(self):
        ''' cria um lead como dicionario simples '''
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }
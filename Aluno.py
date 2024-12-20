class Aluno:
    
    def __init__(self, documento):
        documento = str(documento)
        if self.validar_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF é inválido")
        
    def __str__(self):
        return self.format_cpf()
    
    def validar_cpf(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
        

    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return(
            "{}.{}.{}-{}".format(
                fatia_um,
                fatia_dois,
                fatia_tres,
                fatia_quatro
                )    
            )
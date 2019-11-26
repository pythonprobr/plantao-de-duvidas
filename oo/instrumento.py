# class Instrumento{
#     private som
#
#     public String get_som(){
#         return this.som
#     }
#
#     public String set_som(String som){
#         if (som != null){
#             this.som= som
#         }
#     }
# }
#
# new Instrumento()
# instrumento.set_som('Blem')

class Instrumento:
    def __init__(self):
        self._som = 'Blem'

    @property
    def som(self):
        return self._som

    @som.setter
    def som(self, valor):
        if valor is not None:
            self._som = valor


violao = Instrumento()
violao.som = None
print(violao.__dict__)
print(violao.som)
violao.som = 'Vrum'
print(violao.som)
print(violao._som)

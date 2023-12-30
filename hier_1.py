class College:
    def __init__(self,name):
        self.name=name
class branch(College):
    def __init__(self,principal,hod):
        super().__init__(name)
        self.principal=principal
        self.hod=hod
class dep(branch):
    def __init__(self,bc,fee):
        super().__init__(name,principal,hod,)
        self.bc=bc
        self.fee=fee
obj=dep('ganapathi','mca',4500)

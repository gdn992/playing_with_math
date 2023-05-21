class HeaderButtonComponent:
    component: any
    name: str

    def __init__(self, component: any, name: str):
        super().__init__()
        self.component = component
        self.name = name

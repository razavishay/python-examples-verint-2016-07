class Widget (object):
    def __init__(self, val = ""):
        self.name = val
        self.depends = []

    def add_dependency(self, *dependencies):
        for dependency in dependencies:
            self.depends.append(dependency)

    def build(self):
        if self.depends != []:
            for widget in self.depends:
                print widget.name
                

luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()

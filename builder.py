class CodeBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append((name, value))
        return self 

    def __str__(self):
        indent = "  "
        lines = []

        lines.append(f"class {self.class_name}:")
        lines.append("")

        lines.append(f"{indent}def __init__(self):")

        if not self.fields:
            lines.append(f"{indent*2}pass")
        else:
            for name, value in self.fields:
                lines.append(f"{indent*2}self.{name} = {value}")

        return "\n".join(lines)



cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
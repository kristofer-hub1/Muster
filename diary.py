class Diary:
    def __init__(self):
        self.entries = []      # nimekiri sissekannetest
        self.counter = 0       # loendur

    def add_entry(self, text):
        self.counter += 1
        entry = f"{self.counter}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
        else:
            print("Vale indeks!")

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for entry in self.entries:
                f.write(entry + "\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.entries = [line.strip() for line in f]
        self.counter = len(self.entries)

    def print_statistics(self):
        count = len(self.entries)
        if count == 0:
            avg = 0
        else:
            total_chars = sum(len(entry) for entry in self.entries)
            avg = total_chars / count

        print("Sissekannete arv:", count)
        print("Keskmine tähemärkide arv:", avg)

    def __str__(self):
        return "\n".join(self.entries)


# Näidiskasutus
d = Diary()
d.add_entry("Täna oli ilus ilm.")
d.add_entry("Õppisin programmeerimist.")
d.save("diary.txt")

d.print_statistics()
print(d)
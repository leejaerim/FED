from saver.saver import Saver
class Savers:
    savers = []

    def add(self, saver:Saver):
        self.savers.append(saver)

    def save(self):
        for saver in self.savers:
            saver.save()

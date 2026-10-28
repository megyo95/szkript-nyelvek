
import os


class MDZene:
    def __init__(self, fajl_utvonal):
        self.fajl_utvonal = fajl_utvonal
        self.cim = md_fajlnev(fajl_utvonal)

    def adatok(self):
        return self.cim


def md_fajlnev(fajl_utvonal):
    return os.path.splitext(os.path.basename(fajl_utvonal))[0]
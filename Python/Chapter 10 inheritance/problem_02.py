class Animals:
    pass

class pets(Animals):
    pass


class Dogs(pets):

    @staticmethod
    def show():
        print(f"The Behaviour of Dog is BOW BOW !!!")


d = Dogs()
d.show()

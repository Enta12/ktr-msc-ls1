from worker_information import Worker_information

class Buisness_cards(Worker_information):
    def __init__(self, name):
        super().__init__(name)

    def equals(self, card):
        if self.get_name() != card.get_name():
            print(self.get_name() + " self name")
            print(card.get_name()+ " card name")
            return False;
        if self.get_email() != card.get_email():
            print(self.get_email() + " self name")
            print(card.get_email() + " card name")
            return False;
        if self.get_phone_number() != card.get_phone_number():
            return False;
        if self.get_compagny_name() != card.get_compagny_name():
            return False;
        return True
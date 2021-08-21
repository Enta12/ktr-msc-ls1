from worker_information import Worker_information

class Profile(Worker_information):
    def __init__(self, name, password):
        super().__init__(name)
        self.password = password
        self.share_profiles = []

    def get_password(self):
        return self.password

    def add_share_profile(self, profile_shared):
        self.share_profiles.append(profile_shared)
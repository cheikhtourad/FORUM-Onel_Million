from models import Member


class MemberStore:
    members = []

    def get_all(self):
        return self.members

    def add(self, member):
        self.members.append(member)

    def get_by_id(self, id):
        for x in self.members:
            if id == x.id:
                return x
        return False

    def update(self, member):
        if self.entity_exists(member):
            member.name = input('\nEnter title to update\n')
            member.age = input('\nEnter age to update\n')
            return True
        return "the member don't exist"

    def deleted(self, id):
        for x in self.members:
            if id == x.id:
                self.members.remove(x)
                return self.members
        return False

    def entity_exists(self, member):
        for x in self.members:
            if member == x:
                return True
        return False



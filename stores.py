from models import Member


class MemberStore:
    members = []

    def get_all(self):
        return self.members

    def add(self, member):
        all_members = self.get_all()
        all_members.append(member)

    def get_by_id(self, id):
        all_members = self.get_all()
        for x in all_members:
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
        all_members = self.get_all()
        for x in all_members:
            if id == x.id:
                all_members.remove(x)
                return all_members
        return False

    def entity_exists(self, member):
        all_members = self.get_all()
        for x in all_members:
            if member == x:
                return True
        return False



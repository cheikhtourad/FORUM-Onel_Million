from ctypes import c_bool


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


class PostStore:
    posts = []

    def get_all(self):
        return self.posts

    def add(self, post):
        all_postes = self.get_all()
        all_postes.append(post)

    def get_by_id(self, id):
        all_postes = self.get_all()
        for x in all_postes:
            if id == x.id:
                return x
        return False

    def update(self, post):
        if self.entity_exists(post):
            post.title = input('\nEnter title to update\n')
            post.content = input('\nEnter content to update\n')
            return True
        return "the post don't exist"

    def deleted(self, id):
        all_postes = self.get_all()
        for x in all_postes:
            if id == x.id:
                all_postes.remove(x)
                return all_postes
        return False

    def entity_exists(self, post):
        all_postes = self.get_all()
        for x in all_postes:
            if post == x:
                return True
        return False
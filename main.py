from models import Member
from stores import MemberStore


member1 = Member(1, "tourad", 15)
member2 = Member(2, "Mohamedou", 20)
member3 = Member(3, "cheikh", 25)

# Store of members
member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)
member_store.add(member3)

#list = member_store.get_all()
print(" ")
print("***members get_All***")
for me in member_store.get_all():
    print(me)

print(" ")
print("****get_by_id member1*****")
print(member_store.get_by_id(1))

print(" ")
print("update member1")
member_store.update(member1)
print(member1)
print(member1.age)

print(" ")
print("***members get_All***")
for me in member_store.get_all():
    print(me)

print(" ")
print("delted member1")
member_store.deleted(1)
for me in member_store.get_all():
    print(me)


print(" ")
print("entity_exists member1 ?")
print(member_store.entity_exists(member1))


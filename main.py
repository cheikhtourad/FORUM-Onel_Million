from models import Member, Post
from stores import MemberStore, PostStore


member1 = Member(1, "tourad", 15)
member2 = Member(2, "Mohamedou", 20)
member3 = Member(3, "cheikh", 25)

post1 = Post(1, "Post1", "Content1")
post2 = Post(2, "Post2", "Content2")
post3 = Post(3, "Post3", "Content3")

# Store of members
member_store = MemberStore()
post_sotre = PostStore()

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


post_sotre.add(post1)
post_sotre.add(post2)
post_sotre.add(post3)


#list = member_store.get_all()
print(" ")
print("***post get_All***")
for me in post_sotre.get_all():
    print(me)

print(" ")
print("****get_by_id post1*****")
print(post_sotre.get_by_id(1))

print(" ")
print("update post1")
post_sotre.update(post1)
print(post1)
print(post1.content)

print(" ")
print("***posts get_All***")
for me in post_sotre.get_all():
    print(me)

print(" ")
print("delted post1")
post_sotre.deleted(1)
for me in post_sotre.get_all():
    print(me)


print(" ")
print("entity_exists post1 ?")
print(post_sotre.entity_exists(member1))



#!/usr/bin/python3
import sys

__import__('sys').path.append('.')


def main():
    import uuid
    from models import storage
    from models.place import Place

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new User --")
    my_user = Place()
    my_user.name = "Betty"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = Place()
    my_user2.name = "puta"
    my_user2
    my_user2.save()
    print(my_user2)


main()
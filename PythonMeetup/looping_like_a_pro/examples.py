#
# # Example #1
# import random
#
# dead = False
#
#
# while not dead:
#     print('<3 <3 <3 Keep coding <3 <3 <3')
#     dead = random.random() < 0.4
#
#
# #Example # 2
# list = [1, 2, 3]
# for num in list:
#     print(num)
#
#
# #Example # 3
# prog_langauges = ['Swift', 'Python', 'Objective-c']
#
# for prog_lang in prog_langauges:
#      print(prog_lang)
#
# #Example # 4
#
# for index, prog_langs in enumerate(prog_langauges):
#               print("{} : {}".format(index, prog_langs))
#
#
# #Exapmple 5
# for x,y in [(1,2), (3,4)] :
#     print(x, y)
#
# #Example of enumerate()
#
# foods = ['milk', 'bread', 'eggs']
#
# for index, food in enumerate(foods):
#     print('{} : {}'.format((index + 1), food))
#
# # Example of sorted()
# foods = ['milk', 'bread', 'eggs']
#
# for sorted_food in sorted(foods):
#     print(sorted_food)
#
# #Example of range()
#
# for index in range(5):
#     print(index)
#
# #Example of reversed()
# foods = ['milk', 'bread', 'eggs']
#
# for reversed_food in reversed(foods):
#     print(reversed_food)
#
#
# #Example of zip()
# foods = ['milk', 'bread', 'eggs']
# people = ['Osama', 'Hamza', 'Raza']
#
# for person, food in zip(people, foods):
#     print('{} likes {}'.format(person, food))
#
# #Example of Genrators
#
# class Person:
#     def __init__(self, name, is_anit_social, is_bad_guy):
#         self.name = name
#         self.is_anti_social = is_anit_social
#         self.is_bad_guy = is_bad_guy
#
#     def greeting(self, person):
#         print('{} says Hello {}'.format( self.name, person.name))
#
#
# people_of_gulshan = [Person('Sharjeel', True, False), Person('Omar', False, True), Person('Subhan', False, False)]
# people_of_buffer_zone = [Person('Osama', True, True), Person('Hamza', False, True), Person('Raza', False, True)]
#
# for person_of_gulshan in people_of_gulshan:
#     for person_of_buffer_zone in people_of_buffer_zone:
#             person_of_gulshan.greeting(person_of_buffer_zone)
#
#
#
# for person_of_gulshan in people_of_gulshan:
#     for person_of_buffer_zone in people_of_buffer_zone:
#         if person_of_buffer_zone.is_anti_social == False:
#             person_of_gulshan.greeting(person_of_buffer_zone)
#
#
# for person_of_gulshan in people_of_gulshan:
#     if person_of_gulshan.is_bad_guy == False:
#         for person_of_buffer_zone in people_of_buffer_zone:
#             if person_of_buffer_zone.is_anti_social == False:
#                 person_of_gulshan.greeting(person_of_buffer_zone)
#
#
# for person_of_gulshan in people_of_gulshan:
#     if person_of_gulshan.is_bad_guy == False:
#         for person_of_buffer_zone in people_of_buffer_zone:
#             if person_of_buffer_zone.is_anti_social == False:
#                 if person_of_buffer_zone.is_bad_guy:
#                     break
#                 person_of_gulshan.greeting(person_of_buffer_zone)
#
# def greeting_group():
#     for person_of_gulshan in people_of_gulshan:
#         if person_of_gulshan.is_bad_guy is False:
#             for person_of_buffer_zone in people_of_buffer_zone:
#                 if person_of_buffer_zone.is_anti_social is False:
#                     yield person_of_gulshan, person_of_buffer_zone
#
#
# for person_of_gulshan, person_of_buffer_zone in greeting_group():
#     person_of_gulshan.greeting(person_of_buffer_zone)
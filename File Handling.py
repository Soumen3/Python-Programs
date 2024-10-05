#             # write a file
# f=open('test.txt','w')
# f.write('If you are the smartest person in the room then you are in the wrong room')
# f.close()


#             # more appreciate way to write a file
# with open('text.txt','w') as f:                                 # in this way you do not need to close the file. the file will close autometically 
#     f.write('You are the genius')


# def writing(filename, text):
#     with open(filename, 'w') as f:
#         f.write(text)

# writing('text.txt','I am Soumen')




#                 # Append file
# def append(filename, text):
#     with open(filename, 'a') as f:
#         f.write(text)

# append('text.txt','\nI am a developer')




#                 #read file
# def reading(filename):
#     try:
#         f=open(filename,'r')
#         print(f.read())
#     except FileNotFoundError:
#         print('File does not exist')
#     finally:
#         f.close()

# reading('text.txt')






# #               serching word in file
# def search(filename,word):
#     try:
#         f=open(filename,'r')
#         for line in f.readlines():
#             if word in line:
#                 f.close()
#                 return 1
#         else:
#             f.close()
#             return 0
#     except FileNotFoundError:
#         print('File not Found')

# s=search('text.txt','Soumen')
# if s==1:
#     print('The word is found')
# else:
#     print('The word is not found')




# #           serching word with position in file
# def searching(filename,word):
#     try:
#         f=open(filename,'r')
#         line_count=0
#         for line in f.readlines():
#             line_count+=1
#             strlist=line.split(' ')
#             word_count=0
#             for w in strlist:
#                 word_count+=1
#                 if w==word:
#                     f.close()
#                     return (line_count, word_count)
#         else:
#             f.close()
#             return None
#     except FileNotFoundError:
#         print('File not found')

# position=searching('text.txt', 'developer')
# print(f'The position of the latter is {position[0]} No. line and {position[1]} No. word')








# #                   modify a word in file
# def modify(filename,word,new):
#     t=searching(filename, word)
#     if t!=None:
#         mylist=[]
#         try:
#             f=open(filename,'r')
#             for line in f.readlines():
#                 line=line.replace(word,new)
#                 mylist.append(line)
#             f.close()
#             f=open(filename,'w')
#             f.write(''.join(mylist))
#             f.close()
#         except Exception:
#             print('file not found')
#     else:
#         print('The word does not exists')

# modify('text.txt','developer','Engineer')








# #                   delete a word in file
# def delete(filename,word):
#     t=searching(filename, word)
#     if t!=None:
#         mylist=[]
#         try:
#             f=open(filename,'r')
#             for line in f.readlines():
#                 line=line.replace(word,'')
#                 mylist.append(line)
#             f.close()
#             f=open(filename,'w')
#             f.write(''.join(mylist))
#             f.close()
#         except Exception:
#             print('file not found')
#     else:
#         print('The word does not exists')

# delete('text.txt','am')
# print('The string deleted')
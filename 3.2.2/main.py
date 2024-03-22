

from Post import Post

all_posts_archive = []

# your code here

post1 = Post("Marie", " This is my first post!")
post2 = Post("Marie", " This is my second")
post3 = Post("Marie", " This is my third")

user_input = input(""" What would you like to do?
          "add" - Add a post to the archive
          "remove" - Remove a post from the archive
          "change user" - Change the user name associated with any future posts
          "print" - Display the current up to date list of all posts
          "quit" - End the program

          """)


username = input("Enter the username")

user_input = input("Enter the options below new - add a post to the archive")
while user_input != "quit":
    if user_input == "add":
        message = input("what data would you like to post")
        all_posts_archive.append(Post.get_user_name(), message)
    elif user_input == "remove":
        index = input("what is the index of the message to be removed")
        del all_posts_archive[int(index)]
    elif user_input == "change user":
        username = input("what is you new username")

    elif user_input == "print":
        for post in all_posts_archive:
            print("post")

        else:
            print("please enter a valid option")

            user_input = input(""" What would you like to do?
            "add" - Add a post to the archive
            "remove" - Remove a post from the archive
            "change user" - Change the user name associated with any future posts
            "print" - Display the current up to date list of all posts
            "quit" - End the program

            """)
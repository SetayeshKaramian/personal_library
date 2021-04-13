# Book class is parent of all other classes.
class Book:
    def __init__(self, title, author, publish_year, pages, language, price, counter="pages", read_state=0,
                 act_percent=0):

        self.title = title
        self.creator = author
        self.publish_year = publish_year
        # number of pages or time. based on what media we have.
        self.universe = pages
        # act_percent stores the output of progress def.
        self.act_percent = act_percent
        self.language = language
        self.price = price
        # counter has a default value which shows if we should count based on hours or pages.
        self.counter = counter
        # number of pages or time user have finished for each object till now.
        self.read_state = read_state

    def __str__(self):
        return f"your book infos:\ntitle: {self.title}\nauthor: {self.creator}\npublish_year: {self.publish_year}\
        \npages: {self.universe}\nlanguage: {self.language}\nprice: {self.price}"

    #  get pages that user accomplished and add it to what we had before. update read_state and print out the results.
    #  also if user give a number more than the whole pages of the book it will print out warning.
    def read(self):
        read_now = float(input(f"enter {self.counter} to add: "))
        while self.universe - self.read_state + read_now < 0:
            print("you are adding more than limit. you can't pour water in a glass more then its volume.")
            read_now = float(input(f"Please enter right {self.counter} to add, or 0 for quiet: "))
        self.read_state += read_now
        left = self.universe - self.read_state
        print(f"You have complete {read_now} more {self.counter} from {self.title}\
        \n There are {left}more {self.counter}left.\n")

    # get progress and if p == F just return the progress and if P == T print the statement.
    def progress(self, p):
        self.act_percent = self.read_state / self.universe * 100
        if p == True:
            print(f"you have completed {self.act_percent} % of {self.title}")
        else:
            return self.act_percent

    def get_status(self):
        if self.act_percent == 0:
            print(f"no {self.counter} has been completed.")
        elif self.act_percent == 100:
            print("finished")
        else:
            print("reading/listening")

    # return name of the class
    def whoami(self):
        return type(self).__name__


class Magazine(Book):
    def __int__(self, title, author, publish_year, pages, language, price, issue, counter="pages", act_percent=0):
        super().__init__(title, author, publish_year, pages, language, price, counter, act_percent)
        self.issue = issue

    def __str__(self):
        return f"your magazine infos:\ntitle: {self.title}\nauthor: {self.creator}\npublish_year: {self.publish_year}\
        \npages= {self.universe}\nlanguage:{self.language}\nprice: {self.price}\n issue:{self.issue}"


# just like it's parent Book.
class PodcastEpisode(Book):
    def __init__(self, title, speaker, publish_year, time, language, price, counter="hours", read_state=0,
                 act_percent=0):
        super().__init__(title, speaker, publish_year, time, language, price,
                         counter, read_state, act_percent)

    def __str__(self):
        return f"your podcast episode infos:\ntitle: {self.title}\nspeaker: {self.creator}\
        \npublish_year: {self.publish_year}\ntime= {self.universe}\nlanguage:{self.language}\nprice: {self.price}"


class AudioBook(Book):
    def __init__(self, title, author, speaker, publish_year, pages, time, language,
                 podcast_language, price, read_state=0, counter="pages", act_percent=0):
        super(Book, self).__init__(title, author, publish_year, time, language, price, read_state,
                                   counter, act_percent)
        self.speaker = speaker
        self.pages = pages
        self.podcast_language = podcast_language

    def __str__(self):
        return f"your AudioBook infos:\ntitle: {self.title}\nauthor: {self.creator}speaker: {self.speaker}\
        \npublish_year: {self.publish_year}\npages: {self.pages} \ntime= {self.universe}\nbook_language:{self.language}\n\
         podcast_language:{self.podcast_language}\nprice: {self.price}"


# making objects
def get_data(media):
    if media == Book:
        data = input("please enter: title, author, publish_year, pages, language, price: ").split(",")
    elif media == Magazine:
        data = input("please enter: title, author, publish_year, pages, language, price, issue: ").split(",")
    elif media == PodcastEpisode:
        data = input("please enter: title, speaker , publish_year, time, language, price: ").split(",")
    else:
        data = input("please enter: title, author, speaker, publish_year, pages, time,"
                     " language, podcast language, price: ").split(",")

    data = [float(x) if x.strip().isdigit() else x.strip() for x in data]
    print(media(*data))
    return media(*data)


# Menu of medias. Handing wrong inputs. creating list of medias.
def add_media(number_media, library):
    number = input("enter number of medias: ")
    while number.isdigit() != True or '.' in number:
        print("!Please enter valid input!\n")
        number = input("enter number of medias: ")
    number = int(number)
    lst_media = [Book, Magazine, PodcastEpisode, AudioBook]
    for i in range(0, number):
        type_media = input("please choose your media: 0.Book, 1.Magazine, 2.Podcast episode, 3.Audio book:  ")
        while type_media not in ["0", "1", "2", "3"]:
            print("!Please enter valid input!")
            type_media = input("please choose your media: 0.Book, 1.Magazine, 2.Podcast episode, 3.Audio book:  ")
        type_media = int(type_media)
        media = lst_media[type_media]
        library.append(get_data(media))
    number_media += number
    return number_media, library


# sort all obj by progress
def sorted_progress(library):
    sorted_lib = sorted(library, key=lambda media: media.act_percent)
    for i in range(len(sorted_lib)):
        print(f"class: {sorted_lib[i].whoami()},        title: {sorted_lib[i].title},"
              f"        progress: {sorted_lib[i].progress(False)}\n")


# finding obj in library based on their title.
def item_finder(library):
    a = 0
    while a != 1:
        name = input("Please enter the title of your media: ")
        for item in library:
            if item.title == name:
                a += 1
                return item
        if a == 0:
            print("media not found!")


option = 0
number_media = 0
library = []
print("WELCOME TO YOUR VIRTUAL LIBRARY!\n\n".center(120))
# Home menu. Handling wrong inputs.
while option != 7:

    option = input("please choose your command:\n0.add media, 1.keep track, 2.get progress, 3.get status,"
                   " 4.print all sorted by progress, 5.print all sorted by name, 6.print all, 7.quite: ")

    if option.isdigit() != True:
        print("!Please enter valid input!\n")

    else:
        # add media.
        option = int(option)
        if option == 0:
            a = add_media(number_media, library)
            number_media = a[0]
            library = a[1]

        # read or listen.
        elif option == 1:
            item_finder(library).read()

        # get progress.
        elif option == 2:
            item_finder(library).progress(True)

        # get status
        elif option == 3:
            item_finder(library.progress(False))
            item_finder(library).get_status()

        # print all sorted by progress
        elif option == 4:
            sorted_progress(library)

        # print all sorted by name
        elif option == 5:
            sorted_name = sorted(library, key=lambda media: media.act_percent)
            [print(i, "\n") for i in library]

        # print all
        elif option == 6:
            [print(i, "\n") for i in library]

        # quit
        elif option == 7:
            print("So many books, so little time! <<Frank Zappa>>\nSEE YOU LATER! ".center(120))

        # invalid int input
        else:
            print("!Please enter valid input!\n")

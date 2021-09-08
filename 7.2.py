#Exercise 1

def main():
    user_input = ""
    while user_input != 'STOP':
        user_input = input("Type any word: ")
        generate_word = user_input.lower()
        print(generate_word)

main()

#Exercise 2

salaries1 = {'Jake': '$100K', 'Anand': '$120K'}
print("Jake's salary {Jake} and Anand's salary is {Anand}".format(**salaries1))

#Exercise 3

my_list = (4, 30, 2017, 2, 27)
print("{}, {}, {}, {}, {}".format(my_list[3], my_list[4], my_list[2], my_list[0], my_list[1]))


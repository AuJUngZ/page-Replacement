import random


def generateRefString(number_of_page):
    list_page = []
    for i in range(number_of_page):
        list_page.append(random.randint(0, 7))

    with open(f"ref_string_{number_of_page}.txt", "w") as file:
        file.write(",".join(map(str, list_page)))


if __name__ == '__main__':
    generateRefString(30)

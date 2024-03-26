def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(colored(255, 0, 0, 'Hello, World'))

def colored_name(name ,text):
    if name == "red":
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 0, 0, text)
    if name == "red":
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, text)


def hello(name): 
    print(f"{(colored(255, 0, 0, name))}님 안녕하세요.")

hello("홍길동")
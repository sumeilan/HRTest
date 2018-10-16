global val  # 在使用前初次声明
val = ''  # 给全局变量赋值


def save_token(token):
    global val  # 再次声明，表示在这里使用的是全局变量，而不是局部变量
    val = token  # 这样的话全局变量也会为5
    print(val)

def get_token():
    global val
    print(val)


if __name__ == "__main__":
    save_token(55)
    get_token()
def create_test_lunas_file():
    code = """#Luna Script

int main()
    {
    put.console >> "Hello World/n" >>
    put.console >> "Good Bye World/n" >>

    X = Hello World
    Y = Hello World
    A = Good Bye World

        FLOAT = A
    }
    """

    with open("test.lunas", "w") as file:
        file.write(code)

# Call the function to create the file
create_test_lunas_file()

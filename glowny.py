def save_to_file(content, file_path='example.txt'):
    with open(file_path, 'w') as file:
        file.write(content)
    print("Text saved to '{}' successfully!".format(file_path))

if __name__ == "__main__":
    user_input = input("Wprowadź tekst do zapisania do pliku: ")
    custom_file_path = input("Podaj nazwę pliku (jeśli inna niż 'example.txt'): ")

    if custom_file_path:
        save_to_file(user_input, custom_file_path)
    else:
        save_to_file(user_input)
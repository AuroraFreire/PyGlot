import json

def main():
    def load_data():
        with open("data/translated_data.json", "r") as data:
            translated_data = json.load(data)
            return translated_data


    def get_file_path():
        file_path = input("Enter the path for your file: ")
        with open(file_path, "r") as file:
            python_file = file.read()

    data = load_data()
    get_file_path()

if __name__ == "__main__":
    main()

while True:
    try:
        print("Введите слово: ")
        fileName: str = input()
        if len(fileName) >= 3:
            if fileName.isalpha():
                newfile = open(fileName + ".txt", "a")
                newfile.close()
            else:
                print("Слово должно состоять только из букв")
        else:
            print("Слово должно быть от трёх букв")
    except ValueError:
        print("Ошибка: неверный тип данных")
    except Exception as e:
        print(e)

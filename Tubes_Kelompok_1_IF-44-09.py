import time
import os

clear = lambda: os.system('cls')

# Kami mendefinisikan kartu jack, queen, king, ace sebagai berikut
'''
Jack    = 11
Queen   = 12
King    = 13
Ace     = 14
'''

# List dari masing masing kartu
diamondTupleCard = ( ["D", 2], ["D", 3], ["D", 4], ["D", 5], ["D", 6], ["D", 7], ["D", 8], ["D", 9], ["D", 10], ["D", 11], ["D", 12], ["D", 13], ["D", 14])
cloverTupleCard  = ( ["C", 2], ["C", 3], ["C", 4], ["C", 5], ["C", 6], ["C", 7], ["C", 8], ["C", 9], ["C", 10], ["C", 11], ["C", 12], ["C", 13], ["C", 14])
heartTupleCard   = ( ["H", 2], ["H", 3], ["H", 4], ["H", 5], ["H", 6], ["H", 7], ["H", 8], ["H", 9], ["H", 10], ["H", 11], ["H", 12], ["H", 13], ["H", 14])
spadeTupleCard   = ( ["S", 2], ["S", 3], ["S", 4], ["S", 5], ["S", 6], ["S", 7], ["S", 8], ["S", 9], ["S", 10], ["S", 11], ["S", 12], ["S", 13], ["S", 14])

# Kombinasi kartu yang dianggap sebagai royal flush
royalCardList = [10, 11, 12, 13, 14]

# Deck kartu yang telah disatukan
tupleCard = diamondTupleCard + cloverTupleCard + heartTupleCard + spadeTupleCard

# Mencari kartu royal flush dimana jenis kartu telah ditentukan dengan metode divide and conquer dengan algoritma binary search
def binarySearch(check, tupleCard):
    finalHand = []
    onHand = list(tupleCard)
    current = []
    countI = 0

    left = 0
    right = len(tupleCard)
    mid = int((right + left) / 2)

    start = time.time()
    time.sleep(1)
 
    # Mencari lambang kartu yang sesuai dengan metode divide and conquer
    if check == "H" or check == "S":
        time.sleep(0.07)
        left = mid

        if check == "H":
            mid = int((right + left) / 2)
            right = mid

        elif check == "S":
            mid = int((right + left) / 2)
            left = mid

    elif check == "D" or check == "C":
        right = mid
    
        if check == "D":
            mid = int((right + left) / 2)
            right = mid

        elif check == "C":
            mid = int((right + left) / 2)
            left = mid

    i = left
    while i != right:
        current.append(onHand[i])
        i += 1

    left = 0
    right = len(current) - 1
    mid = 0

    # Mencari pasangan kartu royal flush dengan metode divide and conquer
    while len(finalHand) != len(royalCardList):
        time.sleep(0.15)
        for i in range(len(royalCardList)):
            time.sleep(0.15)
            mid = (right + left) // 2

            # Jika royalCardList[i] > current[mid][1] maka bagian kiri akan diabaikan
            if royalCardList[i] > current[mid][1]:
                left = mid + 1
                mid = (right + left) // 2
                while royalCardList[i] > current[mid][1]:
                    time.sleep(0.15)
                    left = mid + 1
                    mid = (right + left) // 2 
    
            # Jika royalCardList[i] < current[mid][1] maka bagian kanan akan diabaikan
            if royalCardList[i] < current[mid][1]:
                right = mid - 1
                mid = (right + left) // 2 + 1
                while royalCardList[i] < current[mid][1]:
                    time.sleep(0.15)
                    left = mid - 1
                    mid = (right + left) // 2 + 1
    
            # # Jika royalCardList[i] = current[mid][1] maka akan dimasukkan ke finalHand
            if current[mid][1] == royalCardList[i]:
                finalHand.append(current[mid])
                current.remove(current[mid])

                left = 0
                right = len(current) - 1
                mid = 0

    end = time.time()

    checkTime = ((end - start) - 1 - 0.1)

    print("\nFinal hand : ")

    # Menampilkan seluruh kartu yang ada di finalHand
    while countI != len(finalHand):
        time.sleep(0.1)
        print(finalHand[countI])
        countI += 1

    print(f"\nRuntime of Divide and Conquer is {checkTime}")


# Mencari kartu royal flush dimana jenis kartu telah ditentukan dengan metode bruteforce dengan algoritma sequential search
def bruteForce(check, tupleCard):
    finalHand = []
    exist = []
    count = 0
    countI = 0
    test = 0

    start = time.time()
    time.sleep(1)
    # Looping sebanyak panjang deck kartu
    for i in range(len(tupleCard)):
        time.sleep(0.2)

        print(" __________")
        print(f"|{tupleCard[i][1]}")
        print(f"|{tupleCard[i][0]}         |")
        print("|          |")
        print("|          |")
        print(f"|        {tupleCard[i][1]}")
        print(f"|        {tupleCard[i][0]} |")
        print(" -----------")

        # Apabila ada kartu yang dicari maka akan ditambahkan ke finalHand
        if tupleCard[i][0] == check and (tupleCard[i][1] == 10 or tupleCard[i][1] == 11 or tupleCard[i][1] == 12 or tupleCard[i][1] == 13 or tupleCard[i][1] == 14):
            finalHand.append(tupleCard[i])
            exist.append(1)
        else:
            pass  

        if len(exist) == 5:
            for j in range(len(exist)):
                if exist[j] == 1:
                    count += 1
                    if count == 5:
                        test += 1
        if test == 1:
            break
        else:
            pass 

    end = time.time()

    checkTime = ((end - start) - 1 - 0.1)

    print("\nFinal hand : ")

    # Menampilkan seluruh kartu yang ada di finalHand
    while countI != len(finalHand):
        time.sleep(0.1)
        print(finalHand[countI])
        countI += 1

    print(f"\nRuntime of Brute Force is {checkTime}")

# Fungsi untuk mengecek input user dan akan mengubahnya menjadi satu huruf
def checkInput(x):
    if inputCard == "diamond":
        x = "D"
    elif inputCard == "clover":
        x = "C"
    elif inputCard == "heart":
        x = "H"
    elif inputCard == "spade":
        x = "S"
    return x

# Fungsi main
if __name__ == "__main__":
    menu = ""
    inputJenis = ""

    while menu != "n":
        print("______________________________________")
        print("                 MUBES")
        print("--------------------------------------")

        print("Diamond | Clover | Heart | Spade\n")

        inputCard = input("Masukkan Jenis Kartu : ").lower()

        # Looping dibawah untuk mengecek apakah input yang dimasukkan oleh user itu valid atau tidak, jika tidak maka akan minta input ulang
        while inputCard != "diamond" and inputCard != "clover" and inputCard != "heart" and inputCard != "spade":
            clear()
            print("Salah Gan, Coba input lagi!")
            print("______________________________________")
            print("                 MUBES")
            print("--------------------------------------")

            print("Diamond | Clover | Heart | Spade\n")

            inputCard = input("Masukkan Jenis Kartu : ").lower()

        check = checkInput(inputCard)

        print("______________________________________")
        print("Pilih Jenis Search")
        print("1 : Bruteforce Search")
        print("2 : Binary Search")
        print("--------------------------------------")

        inputJenis = input("Masukkan Jenis Searching : ")

        # Looping dibawah guna mengecek apakah input yang dimasukkan oleh user valid atau tidak, jika tidak maka sistem akan meminta user input ulang
        while inputJenis != "1" or inputJenis != "2":
            if inputJenis == "1" or inputJenis == "2":
                break
            else:
                clear()
                print("Salah Gan, Coba input lagi!")

                print("______________________________________")
                print("Pilih Jenis Search")
                print("1 : Bruteforce Search")
                print("2 : Binary Search")
                print("--------------------------------------")

                inputJenis = input("Masukkan Jenis Searching : ")

        # Kondisi untuk memanggil fungsi terkait
        if inputJenis == "1":
            bruteForce(check, tupleCard)
        elif inputJenis == "2":
            binarySearch(check, tupleCard)

        # Input untuk meminta user akankah user mengulang sistem kembali atau tidak.
        menu = input("Mulai dari awal lagi? (Y/N) : ").lower()

        clear()

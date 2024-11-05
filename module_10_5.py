import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден. Проверьте путь и имя файла.")

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./data/file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное выполнение: {end_time - start_time:.6f} секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение: {end_time - start_time:.6f} секунд")
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")
def save_file(write_file, unique_list):
    with open(write_file, 'w', encoding='UTF-8') as f:
        f.write(f'Всего уникальных слов: {len(unique_list)}\n===========================')
        for word in unique_list:
            f.write(f'{word}\n')
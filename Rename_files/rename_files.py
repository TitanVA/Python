import os


DIRECTORY = r"D:\Projects\For_education\Photos"


def get_valid_name(name, num):
    name = f"IMG_{num}" + name[-4:]
    name = name.replace("RINA", "")
    if not name.startswith("T_"):
        name = "T_" + name + ".jpg"
    return name


def rename_file(root, name, num):
    valid_name = get_valid_name(name, num)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old_file, new_file)


def rename_files(find_directory):
    num = 0
    for root, dirs, files in os.walk(find_directory):
        for name in files:
            rename_file(root, name, num)
            num += 1


if __name__ == '__main__':
    rename_files(DIRECTORY)

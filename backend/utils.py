import os
import random
import string

limit = (1000 * 1000) * 2  # 2MB


def gen_alphabet():
    """
    Generate alphabetic string
    """
    length = random.randint(10, 24)
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def gen_alphanumeric():
    """
    Generate alphanumeric string
    """
    length = random.randint(10, 24)
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(length)
    )


def gen_integers():
    """
    Generate integers
    """
    length = random.randint(2, 15)
    return "".join(random.choice(string.digits) for i in range(length))


def gen_real_numbers():
    """
    Generate real numbers
    """
    length = random.randint(2, 5)
    return round(random.uniform(-50000, 50000), length)


def type_count(_string):
    """
    Get 4 type count
    """
    alpha_count = 0
    num_count = 0
    alpha_num_count = 0
    real_num_count = 0
    for s in _string.split(", "):
        s = str(s)
        if s.isalnum():
            if s.isalpha():
                alpha_count += 1
            elif s.isnumeric():
                num_count += 1
            else:
                alpha_num_count += 1
        else:
            real_num_count += 1
    return {
        "report": {
            "alpha_count": alpha_count,
            "num_count": num_count,
            "alpha_num_count": alpha_num_count,
            "real_num_count": real_num_count - 1,
        }
    }


def get_path_upload():
    """
    Get path upload
    """
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r"uploads")
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    return final_directory


def generate_file(_id):
    """
    Generate file
    """
    count = 0
    path = get_path_upload()
    filename = f"{path}/{_id}.txt"
    try:
        with open(filename, "w") as f:
            while count < limit:
                my_list = [
                    gen_alphabet(),
                    gen_alphanumeric(),
                    gen_integers(),
                    gen_real_numbers(),
                ]
                generated_string = random.choice(my_list)
                count += len(str(generated_string)) + 2
                f.write(str(generated_string) + ", ")
        return generate_report(_id)
    except Exception as e:
        print(e)
        if os.path.exists(filename):
            os.remove(filename)


def generate_report(_id):
    """
    Generate report from file
    """
    path = get_path_upload()
    filename = f"{path}/{_id}.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            return type_count(f.read())
    else:
        return None


def read_file(_id):
    """
    Read file data for download
    """
    path = get_path_upload()
    filename = f"{path}/{_id}.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    else:
        return None

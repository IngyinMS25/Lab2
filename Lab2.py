def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 67, 32)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))
    return float_list

def calc_average_temperature(num_list):
    return sum(num_list) / len(num_list)

def calc_min_max_temperature(num_list):
    return [min(num_list), max(num_list)]

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average_temperature(num_list)
    print("Average temperature :" + str(average))

    min_max = calc_min_max_temperature(num_list)
    print("Minimum temperature :" + str(min_max[0]))
    print("Maximum temperature :" + str(min_max[1]))

if __name__ == "__main__":
    main()
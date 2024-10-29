###########################################################
#  Social Media Analysis Project
#
#  Algorithm
#    prompt for file names for names, X's friends, and Facebook's friends
#    open and read the given files, handling any file errors
#    loop to display a menu with multiple choices:
#       1. Calculate and display the max number of friend intersections between X and Facebook
#       2. Calculate and display the percentage of people with no shared friends between X and Facebook
#       3. Allow for individual information lookup to display friends in X and Facebook
#       4. Calculate and display the percentage of people with more friends in X compared to Facebook
#       5. Calculate and display the number of triangle friendships in X
#       6. Calculate and display the number of triangle friendships on Facebook
#       7. Calculate and display the number of triangle friendships in X and Facebook combined
#    prompt for a choice and process the selected option until the user decides to exit
#    display a closing message upon exit
###########################################################
import csv
import sys


def input(prompt=None):
    """
        DO NOT MODIFY: Uncomment this function when submitting to Codio
        or when using the run_file.py to test your code.
        This function is needed for testing in Codio to echo the input to the output
        Function to get user input from the standard input (stdin) with an optional prompt.
        Args:
            prompt (str, optional): A prompt to display before waiting for input. Defaults to None.
        Returns:
            str: The user input received from stdin.
    """

    if prompt:
        print(prompt, end="")
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip("\n")
    print(aaa_str)
    return aaa_str


choices = '''
  Menu :
     1: Max number of friends intersection between X and Facebook among all
     2: Percentage of people with no shared friends between X and Facebook
     3: Individual information
     4: Percentage of people with  more friends in X compared to Facebook
     5: The number of  triangle friendships in X
     6: The number of  triangle friendships on Facebook
     7: The number of  triangle friendships in X and Facebook together
       Enter any other key(s) to exit

  '''


def open_file(prompt):
    """
    Open the file and return the file name, simple error message if the file does not exist.
    :param prompt:
    :return: opened file
    """
    while True:
        file_name_1 = input(prompt)
        try:  # Try to open the file
            file_name = open(file_name_1, "r")
            return file_name
        except FileNotFoundError: # If the file does not exist, print an error message
            print("Error. File does not exist\n")


def read_file(file_name):
    """
    Read the file and return a list of the file content, its elements are from the names file only.
    :param file_name:
    :return: list of data from the file
    """
    file_name_list = []
    csv_reader = csv.reader(file_name)
    for line in csv_reader:
        lines = ','.join(line)  # Convert the list of elements to a string
        file_name_list.append(lines)
    return file_name_list


def read_txt_file(file, file_content):
    """
    Read the file and return a list of the file content, its elements are from the facebook and x files.
    :param file:
    :param file_content:
    :return: list of lists of the data from the file
    """
    file_list = []
    if file_content:
        for line in file:
            try:
                line = line.strip().split(",") # line in the file is made into a list of elements separated by a comma
                if len(line) > 1: # If the length of the line is greater than 1
                    del line[-1]   # Remove the last element in the list, as there would be a white space at the end
                file_list.append(line)
            except ValueError:
                file_list.append(line)
        return file_list
    else:
        for line in file:
            try:
                line = line.strip().split(",")  # line in the file is made into a list of elements separated by a comma
                if len(line) > 1:
                    del line[-1]  # Remove the last element in the list, as there would be a white space at the end
                elif len(line) == 1 and line[0] == "":  # If the only element is whitespace, then we empty the list
                    del line[-1]
                file_list.append(line)
            except ValueError:
                file_list.append(line)
        return file_list


def assign_id(file_list):
    """
    Assign an id to each element in the list using the index of the element.
    :param file_list:
    :return: All the names with their corresponding id
    """
    id_dict = {}
    for i in range(len(file_list)):  # Iterate through the elements in the list
        id_dict[i] = file_list[i]  # Assign an id to each element
    return id_dict


def convert_id(file_name_twitter, id_dict):
    """
    Convert the id in the twitter list which comes from the read_text_file function to the corresponding
    name using the id_dict which is returned from the assign_id function.
    :param file_name_twitter:
    :param id_dict:
    :return: converted id
    """
    converted_id = []
    for line in file_name_twitter: # Iterate through the twitter list
        if len(line) >= 1 and line[0] != "":
            for i in range(len(line)):  # Iterate through the elements in the list
                line[i] = id_dict[int(line[i])]
            converted_id.append(line)
        else:  # If the line is empty, remove the last element
            del line[-1]
            converted_id.append(line)
    return converted_id


def nested_dictionary(names, facebook, x_file):
    """
    Create a nested dictionary with the names in the names file as the key and the values are the
    X and Facebook friends.
    :param names:
    :param facebook:
    :param x_file:
    :return: nested dictionary
    """
    names_list = read_file(names)  # Read the names file content
    facebook_list = read_txt_file(facebook, False)  # Read the facebook file content
    x_list = read_txt_file(x_file, True)  # Read the x file content
    id_dict = assign_id(names_list)  # Assign an id to each name in the names file
    # Convert the id in the x_list to the corresponding name
    x = convert_id(x_list, id_dict)
    nested_dict = {}
    for i in range(len(names_list)):
        nested_dict[names_list[i]] = {"X": x[i],
                                      "Facebook": facebook_list[i]}
    # names.close()
    facebook.close()
    x_file.close()
    return nested_dict


def maximum_number_interaction(nested_dict):
    """
    Find the maximum number of friends intersection between X and Facebook using sets and set methods.
    :param nested_dict:
    :return: maximum number of friends intersection
    """
    max_intersection = 0
    for i, j in enumerate(nested_dict.keys()):  # Enumerate the keys of the nested dictionary
        # Check if the intersection of X and Facebook is greater than the current max intersection
        intersection = len(set(nested_dict[j]["X"]).intersection(set(nested_dict[j]["Facebook"])))
        if intersection > max_intersection:
            max_intersection = intersection
    return max_intersection


def percentage_no_shared_friends(nested_dict):
    """
    Find the percentage of people with no shared friends between X and Facebook using sets and set methods.
    :param nested_dict:
    :return: percentage of people with no shared friends
    """
    no_shared_friends = 0
    for j in nested_dict.keys():
        # Check if the intersection of X and Facebook is 0
        intersection = len(set(nested_dict[j]["X"]).intersection(set(nested_dict[j]["Facebook"])))
        if intersection == 0:
            no_shared_friends += 1
    return int((no_shared_friends/len(nested_dict)) * 100)


def access_friends(nested_dict):
    """
    Access the friends of a person using the name of the person.
    :param nested_dict:
    :return: access the friends of a person in X and Facebook
    """
    while True:
        try:
            name = input("Enter a person's name ~: ")
            if name in nested_dict.keys():
                print("-" * 14 + "\nFriends in X\n" + "*" * 14)
                for i in sorted(x for x in nested_dict[name]["X"]):  # Sort the friends in X for an alphabetical order
                    print(i)
                print("-" * 20 + "\nFriends in Facebook\n" + "*" * 20)
                for facebook in sorted(j for j in nested_dict[name]["Facebook"]): # Sort the friends in Facebook for an alphabetical order
                    print(facebook)
                break
            else:
                print("Invalid name or does not exist")
        except ValueError:
            print("Invalid name or does not exist")


def percentage_more_friends_x_facebook(nested_dict):
    """
    Find the percentage of people with more friends in X compared to Facebook.
    :param nested_dict:
    :return: percentage value as an int
    """
    more_friends = 0
    for j in nested_dict.keys():
        if len(nested_dict[j]["X"]) > len(nested_dict[j]["Facebook"]): # Check if X has more friends than Facebook
            more_friends += 1
        # Check if X has friends but Facebook does not
        elif len(nested_dict[j]["X"]) > 0 and len(nested_dict[j]["Facebook"]) == 0:
            more_friends += 1
        # Check if X has no friends but Facebook does
        elif len(nested_dict[j]["X"]) == 0 and len(nested_dict[j]["Facebook"]) == 0:
            pass
        # Check if X has no friends but Facebook does
        elif len(nested_dict[j]["X"]) == 0 and len(nested_dict[j]["Facebook"]) > 0:
            pass
    return int((more_friends/len(nested_dict)) * 100)


def triangle_friendship_x(nested_dict):
    """
    Find the number of triangle friendships in X,where a triangle friendship is when person i is
    friends with person j.
    :param nested_dict:
    :return: number of triangle friendships
    """
    triangle_friendship = 0
    for j in nested_dict.keys():
        x_friends = nested_dict[j]["X"]
        for i in range(len(x_friends)):
            for k in range(i + 1, len(x_friends)):  # Avoid repeating pairs
                # Condition to check if i is friend is also a friend of k in X
                if x_friends[k] in nested_dict[x_friends[i]]["X"]:
                    # Ensure j is the "smallest" to count the triangle only once
                    if j < x_friends[i] and j < x_friends[k]:
                        triangle_friendship += 1
    return triangle_friendship


def triangle_friendship_facebook(nested_dict):
    """
    Find the number of triangle friendships in Facebook, where a triangle friendship is when person i is
    friends with person j.
    :param nested_dict:
    :return: number of triangle friendships
    """
    triangle_friendship = 0
    for j in nested_dict.keys():  # Iterate through the keys of the nested dictionary
        x_friends = nested_dict[j]["Facebook"]
        for i in range(len(x_friends)):  # Iterate through the friends of j in Facebook
            for k in range(i + 1, len(x_friends)):  # Avoid repeating pairs
                # Condition to check if i is friend is also a friend of k in Facebook
                if x_friends[k] in nested_dict[x_friends[i]]["Facebook"]:
                    # Ensure j is the "smallest" to count the triangle only once
                    if j < x_friends[i] and j < x_friends[k]:
                        triangle_friendship += 1
    return triangle_friendship


def triangle_friendship_merged(nested_dict):
    """
    Find the number of triangle friendships in X merged with Facebook, where a triangle friendship is when person i is
    friends with person j.
    :param nested_dict:
    :return: number of triangle friendships
    """
    triangle_friendship = 0
    for j in nested_dict.keys():
        # Get the union of X's friends and Facebook's friends for person j
        merged_friends = set(nested_dict[j]["X"]) | set(nested_dict[j]["Facebook"])
        merged_friends_list = list(merged_friends)  # Convert to list for indexing

        for i in range(len(merged_friends_list)):
            for k in range(i + 1, len(merged_friends_list)):  # Avoid repeating pairs
                # Check if i's friend is also a friend of k in the merged list
                if merged_friends_list[k] in nested_dict[merged_friends_list[i]]["X"] or merged_friends_list[k] in nested_dict[merged_friends_list[i]]["Facebook"]:
                    if j < merged_friends_list[i] and j < merged_friends_list[k]:
                        triangle_friendship += 1
    return triangle_friendship


def main():
    names_file = open_file("Enter a names file ~:")
    print()
    x_file = open_file("Enter the twitter id file ~:")
    print()
    facebook_file = open_file("Enter the facebook id file ~:")
    print()
    while True:
        print(choices)
        choice = input("Input a choice ~:")
        if choice == "1":
            nested_dict_in_1 = nested_dictionary(names_file, facebook_file, x_file)
            max_intersection = maximum_number_interaction(nested_dict_in_1)
            print("The Max number intersection of friends between X and Facebook is: {}".format(max_intersection))
        elif choice == "2":
            nested_dict_in_2 = nested_dictionary(names_file, facebook_file, x_file)
            no_shared_friends = percentage_no_shared_friends(nested_dict_in_2)
            print("{}% of people have no friends in common on X and Facebook".format(no_shared_friends))
        elif choice == "3":
            nested_dict_in_3 = nested_dictionary(names_file, facebook_file, x_file)
            access_friends(nested_dict_in_3)
        elif choice == "4":
            nested_dict_in_4 = nested_dictionary(names_file, facebook_file, x_file)
            more_friends = percentage_more_friends_x_facebook(nested_dict_in_4)
            print("{}% of people have more friends in X compared to Facebook".format(more_friends))
        elif choice == "5":
            nested_dict_in_5 = nested_dictionary(names_file, facebook_file, x_file)
            triangle_friendship = triangle_friendship_x(nested_dict_in_5)
            print("The number of triangle friendships in X is: {}".format(triangle_friendship))
        elif choice == "6":
            nested_dict_in_6 = nested_dictionary(names_file, facebook_file, x_file)
            triangle_friendship = triangle_friendship_facebook(nested_dict_in_6)
            print("The number of triangle friendships in Facebook is: {}".format(triangle_friendship))
        elif choice == "7":
            nested_dict_in_7 = nested_dictionary(names_file, facebook_file, x_file)
            triangle_friendship = triangle_friendship_merged(nested_dict_in_7)
            print("The number of triangle friendships in X merged with Facebook is:  {}".format(triangle_friendship))
        else:
            print("Thank you")
            break
if __name__ == "__main__":
    main()

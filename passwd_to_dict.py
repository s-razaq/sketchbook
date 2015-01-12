__author__ = 'Saqib Razaq'

"""
Create a dictionary based on /etc/passwd, in which the dict's keys are usernames and the values are the
numeric IDs of those users. Then iterate through this dict, displaying one username and user
ID on each line in alphabetical order.
"""


def main():
    passwd_dict = dict()
    with open('/etc/passwd') as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith("#"):
                line = line.split(":")
                passwd_dict[line[0]] = line[2]

    # sort dict by keys
    for key in sorted(passwd_dict):
        print "username: {} \t id: {}".format(key, passwd_dict[key])


if __name__ == '__main__':
    main()
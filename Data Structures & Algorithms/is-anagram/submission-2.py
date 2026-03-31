class Solution:
    def isAnagram(self, s : str, t : str) -> bool:
        def check(string):
            my_dict = {}
            for i in range(len(string)):
                if string[i] in my_dict.keys():
                    my_dict[string[i]] += 1
                else:
                    my_dict[string[i]] = 1
                    print(string[i])
                    print(count)
            return my_dict
        print(check(s))
        print(check(t))
        if check(s) == check(t):
            return True
        else:
            return False
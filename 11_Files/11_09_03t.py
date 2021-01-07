import test
from task_11_09_03 import min_list

class TestMin():
    def empty_test_min(alist):
        alist = []
        return(test.assertEqual(None, min_list(alist)))

    def zero_test_min(alist):
        alist = [0]
        return(test.assertEqual(0, min_list(alist)))

    def normal_test_min(alist):
        alist = [3,1,2]
        return(test.assertEqual(1, min_list(alist)))

t = TestMin()
print(t.empty_test_min()) # Fixed IndexError
print(t.zero_test_min())
print(t.normal_test_min())

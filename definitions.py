import os

#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.getcwd().replace("\\","/")
TEST_RESOURCES_FOLDER = ROOT_DIR + '/tests/test_resources'
print(TEST_RESOURCES_FOLDER)

if __name__ == '__main__':
    print(ROOT_DIR)

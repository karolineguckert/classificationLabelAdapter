import os
import cv2

class LabelAdapter:

    def __init__(self):
        self.ROOT_PATH = './images'

    def create_a_copy_of_classification_with_different_type(self, folder):
        labels_list = os.listdir('{}/{}/labels'.format(self.ROOT_PATH, folder))

        for file_name in labels_list:
            label_path = '{}/{}/labels/{}'.format(self.ROOT_PATH, folder, file_name)
            content = self.__get_label_lines(label_path)

            if len(content) != 0:
                lines_divided = content[0].split(" ")
                label_type = lines_divided[0]

                if label_type != 3:
                    self.open_image(folder, file_name)
                    answer = self.get_answer(file_name)
                    cv2.destroyAllWindows()

                    new_line = self.create_a_copy_of_classification(lines_divided, answer)
                    new_content = "{}{}".format(content[0], new_line)
                    self.__write_to_file(label_path, new_content)

    def create_a_copy_of_classification(self, lines_divided, answer):
        lines_divided[0] = str(answer)
        changed_line = " ".join(lines_divided)
        return changed_line

    def get_answer(self, file_name):
        has_a_correct_answer = False

        while not has_a_correct_answer:
            print("\n -------------------------\n")
            print("\nFile name: {}".format(file_name))
            print("0 - Arbusto grande")
            print("1 - Arbusto pequeno")
            print("4 - Folhas estreitas")
            print("5 - Folhas largas")
            answer = input("Which is this classification? -> ")

            if int(answer) in (4, 5, 0, 1):
                return answer

    def open_image(self, folder, file):
        image_file_name = file.replace(".txt", ".jpg")
        image_path = '{}/{}/images/{}'.format(self.ROOT_PATH, folder, image_file_name)

        image = cv2.imread(image_path)
        cv2.imshow(file, image)
        cv2.waitKey(4)

    # Assistant method to write values in the file with classifications
    #
    # label_path is the path of the label
    # content is the values to be written in the file classifications
    def __write_to_file(self, label_path, content):
        file = open(label_path, "w+")
        file.write(content)

    # Assistant method to get all lines from file with classifications
    #
    # label_path is the path of the label
    def __get_label_lines(self, label_path):
        file = open(label_path, "r")
        content = file.readlines()

        file.close()

        return content

import os
import shutil

class SeparateByType:

    def __init__(self):
        self.ROOT_PATH = './images'
        self.BROADLEAF = './broadleaf'

    def move_labels_of_broadleaf(self):
        labels_list = os.listdir('{}/labels'.format(self.ROOT_PATH))

        for file_name in labels_list:
            label_path = '{}/labels/{}'.format(self.ROOT_PATH, file_name)
            content = self.__get_label_lines(label_path)

            if len(content) != 0:
                lines_divided = content[0].split(" ")
                label_type = lines_divided[0]
                print(label_type, file_name)

                if int(label_type) == 5:
                    new_path_of_label = '{}/labels/{}'.format(self.BROADLEAF, file_name)
                    shutil.move(label_path, new_path_of_label)

    def move_images_of_broadleaf(self):
        labels_list = os.listdir('{}/labels'.format(self.BROADLEAF))

        for file_name in labels_list:
            image_name = file_name.replace(".txt",".jpg")
            image_path = '{}/images/{}'.format(self.ROOT_PATH, image_name)

            new_path_of_image = '{}/images/{}'.format(self.BROADLEAF, image_name)
            shutil.move(image_path, new_path_of_image)

    def move_not_use_label(self):
        images_list = os.listdir('{}/images'.format(self.BROADLEAF))

        for file_name in images_list:
            label_name = file_name.replace(".jpg", ".txt")
            label_path = '{}/labels/{}'.format(self.BROADLEAF, label_name)

            new_path_of_label = '{}/labels2/{}'.format(self.BROADLEAF, label_name)
            shutil.move(label_path, new_path_of_label)




    # Assistant method to get all lines from file with classifications
    #
    # label_path is the path of the label
    def __get_label_lines(self, label_path):
        file = open(label_path, "r")
        content = file.readlines()

        file.close()

        return content
class MinTrainers:

    def __init__(self):
        self.trainerSubjects = []
        self.lines = []

        self.total_uniq_subjects = []
        self.total_uniq_trainers = []
        self.edges = []
        self.possible_row_combinations = []

    '''
        This Methods reads input file inputPS13.txt and creates a Adjacency matrix
    '''

    def read_input(self, input_file):
        try:
            with open(input_file, 'r') as f:
                self.lines = f.read().splitlines()

            for line in self.lines:
                line_data = line.split('/')
                self.trainerSubjects.append((line_data[0], line_data[1:]))

            self.trainerSubjects = sorted(self.trainerSubjects)

            self.create_uniq_list_of_subjects()
            self.create_uniq_list_of_trainers()
            self.create_graph()

        except Exception as e:
            print(e)

    # This method create a unique list of subjects that the college would have on the whole
    def create_uniq_list_of_subjects(self):
        first_list = []
        self.total_uniq_subjects = list(first_list)
        for t in self.trainerSubjects:
            self.total_uniq_subjects.extend(x for x in t[1] if x not in self.total_uniq_subjects)

        self.total_uniq_subjects = sorted(self.total_uniq_subjects)

    # This method create a unique list of trainers
    def create_uniq_list_of_trainers(self):
        for t in self.trainerSubjects:
            self.total_uniq_trainers.append(t[0])
        self.total_uniq_trainers = sorted(list(set(self.total_uniq_trainers)))

    # this method would create a graph using adjacency matrix
    def create_graph(self):
        self.edges = [[0 for j in range(len(self.total_uniq_subjects))] for i in range(len(self.total_uniq_trainers))]

        for i in range(len(self.total_uniq_trainers)):
            for j in range(len(self.total_uniq_subjects)):
                if self.trainerSubjects[i][0] == self.total_uniq_trainers[i] and self.total_uniq_subjects[j] in \
                        self.trainerSubjects[i][1]:
                    self.edges[i][j] = 1

    # this method would display the trainers who can deal given subjects from promptsPS13.txt file
    def display_trainers(self):
        prompt_subject = []
        trainers = []
        try:
            with open('promptsPS13.txt') as f:
                for prompt in f.read().splitlines():
                    prompt_subject.append(prompt.split(':')[1].strip())

            for subject in range(len(prompt_subject)):
                for i in range(len(self.trainerSubjects)):
                    if prompt_subject[subject] in self.trainerSubjects[i][1]:
                        trainers.append(self.trainerSubjects[i][0])

            trainers = list(set(trainers))
            with open('outputPS13.txt', 'a') as f:
                f.write('\n----------Function display_trainers--------------\n')
                f.write('\nList of Trainers who can teach ' + ','.join(prompt_subject) + '\n')
                for trainer in trainers:
                    f.write(trainer + '\n')
                f.write('\n------------------------\n')
        except Exception as e:
            print(e)

    # this method would display the trainers & subjects on the whole read from inputPS13.txt file
    def show_all(self):
        with open('outputPS13.txt', 'a') as f:
            f.write('\n----------Function showAll--------------\n')
            f.write('Total no. of trainers: ' + str(len(self.total_uniq_trainers)) + '\n')
            f.write('Total no. of subjects: ' + str(len(self.total_uniq_subjects)) + '\n')

            f.write('\nList of trainers:\n')
            for trainer in self.total_uniq_trainers:
                f.write(trainer + '\n')

            f.write('\nList of subjects:\n')
            for subject in self.total_uniq_subjects:
                f.write(subject + '\n')

            f.write('\n------------------------\n')

        for i in self.edges:
            print(i)

    def printSubArrays(self, arr, start, end):
        # Stop if we have reached the end of the array
        if end == len(arr):
            return

        # Increment the end point and start from 0
        elif start > end:
            return self.printSubArrays(arr, 0, end + 1)

        # Print the subarray and increment the starting
        # point
        else:
            if len(arr[start:end + 1]) > 1:
                self.possible_row_combinations.append(arr[start:end + 1])
            return self.printSubArrays(arr, start + 1, end)

    def displayRecruitList_bkp(self):
        self.printSubArrays([i for i in range(len(self.edges))], 0, 0)
        self.possible_row_combinations.sort(key=lambda t: len(t), reverse=False)
        print(self.possible_row_combinations)

    def displayRecruitList(self):
        string1 = "showMinList"
        with open("promptsPS13.txt") as f:
            readfile = f.read()
        if string1 in readfile:
            col_sum = []
            row_sum = []
            pos_list = []
            temp_list = self.edges.copy()
            for j in range(0, len(self.total_uniq_subjects)):
                x = 0
                for i in range(0, len(self.total_uniq_trainers)):
                    x = x + self.edges[i][j]
                col_sum.append(x)
                for i in range(0, len(self.total_uniq_trainers)):
                    temp_list[i][j] = self.edges[i][j] / col_sum[j]
            for i in temp_list:
                row_sum.append(sum(i))
            for j in range(0, len(self.total_uniq_subjects)):
                sub_list = []
                for i in range(0, len(self.total_uniq_trainers)):
                    sub_list.append(temp_list[i][j])
            unique_val = list(set(sub_list))
            unique_val_2 = [x for x in unique_val if x != 0][0]
            indices = [i for i, x in enumerate(sub_list) if x == unique_val_2]
            row_vals = [row_sum[n] for n in indices]
            pos_list.append(row_sum.index(max(row_vals)))
            train_req = list(set(pos_list))
            self.lines.sort()
            recruit_list = [self.lines[n] for n in train_req]

        with open('outputPS13.txt', 'a') as f:
            f.write('\n----------Function RecruitList--------------\n')
            f.write('No of trainers required to cover all subjects: '
                    + str(len(train_req)) + '\n')
            for x in recruit_list:
                f.write(str(x) + '\n')



def main():
    min_trainers = MinTrainers()
    min_trainers.read_input('inputPS13.txt')
    min_trainers.show_all()
    min_trainers.display_trainers()
    min_trainers.displayRecruitList_bkp()
    min_trainers.displayRecruitList()


if __name__ == '__main__':
    main()

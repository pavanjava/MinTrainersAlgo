class MinTrainers:

    def __init__(self):
        self.trainerSubjects = []
        self.lines = []

        self.total_uniq_subjects = []
        self.total_uniq_trainers = []
        self.edges = []

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

    def create_uniq_list_of_subjects(self):
        first_list = []
        self.total_uniq_subjects = list(first_list)
        for t in self.trainerSubjects:
            self.total_uniq_subjects.extend(x for x in t[1] if x not in self.total_uniq_subjects)

        self.total_uniq_subjects = sorted(self.total_uniq_subjects)

    def create_uniq_list_of_trainers(self):
        for t in self.trainerSubjects:
            self.total_uniq_trainers.append(t[0])
        self.total_uniq_trainers = sorted(list(set(self.total_uniq_trainers)))

    def create_graph(self):
        self.edges = [[0 for i in range(len(self.total_uniq_trainers))] for j in range(len(self.total_uniq_subjects))]

        for i in range(len(self.total_uniq_trainers)):
            for j in range(len(self.total_uniq_subjects)):
                if self.trainerSubjects[i][0] == self.total_uniq_trainers[i] and self.total_uniq_subjects[j] in \
                        self.trainerSubjects[i][1]:
                    self.edges[i][j] = 1

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

            for i in self.edges:
                print(i)


def main():
    min_trainers = MinTrainers()
    min_trainers.read_input('inputPS13.txt')
    min_trainers.show_all()


if __name__ == '__main__':
    main()

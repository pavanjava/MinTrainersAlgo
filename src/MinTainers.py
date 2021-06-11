class MinTrainers:

    def __init__(self):
        self.trainerSubjects = []
        self.lines = []

    def read_input(self, input_file):
        try:
            with open(input_file, 'r') as f:
                self.lines = f.readlines()
            for line in self.lines:
                line_data = line.split('/')
                self.trainerSubjects.append((line_data[0], line_data[1:]))
        except Exception as e:
            print(e)

    def show_all(self):
        print(self.lines)
        print(self.trainerSubjects)


def main():
    min_trainers = MinTrainers()
    min_trainers.read_input('inputPS13.txt')
    min_trainers.show_all()


if __name__ == '__main__':
    main()

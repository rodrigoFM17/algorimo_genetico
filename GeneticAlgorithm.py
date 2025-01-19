import math
from Subject import Subject
from StringUtils import binary_string_to_bin, binary_string_to_int
from random import random, randint
from copy import deepcopy

class GeneticAlgorithm:
    
    def __init__(self, a, b, dx, p_breeding, p_mutation, p_mutation_gen, operation, average_tolerancy):
        self.a = int(a)
        self.b = int(b)
        self.dx = float(dx)
        self.p_breeding = float(p_breeding)
        self.p_mutation = float(p_mutation)
        self.p_mutation_gen = float(p_mutation_gen)
        self.n = self.calculate_n()
        self.n_bits = self.calculate_n_bits()
        self.dx = self.calculate_dx()
        self.operation = operation
        self.subjects = []
        self.descendants = []
        self.pairs = []
        self.generations = []
        self.sorted_subjects = []
        self.best_subjects = []
        self.worst_subjects = []
        self.average_subjects = []
        self.average_tolerancy = float(average_tolerancy)

    def start(self):
        print("algoritmo genetico iniciado")
        self.eval_subjects()
        self.make_pairs()
        self.breeding()
        self.mutation()
        self.cute()
        self.get_best_subjects()
        self.get_worst_subjects()
        self.get_average_subjects()
        self.summarize()
        

    def calculate_n(self):
        return int((self.b - self.a) / self.dx + 1)
    
    def calculate_n_bits(self):
        return math.ceil(math.log2(self.n))
    
    def calculate_dx(self):
        return (self.b - self.a)/ (2 ** self.n_bits - 1)
    
    def eval_subjects(self):
        if len(self.subjects) == 0:
            for i in range(self.n):
                self.subjects.append(Subject(bin(i), i, self.operation, self.a, self.dx))
        else:
            for subject in self.subjects:
                subject.eval_phenotype()

    def make_pairs(self):
        self.sorted_subjects = sorted(self.subjects, key=lambda subject: subject.phenotype, reverse=True)
        for i in range(len(self.sorted_subjects)):
            p = random()
            if p <= self.p_breeding:
                j = randint(0,i)
                
                self.pairs.append({
                    "i":i,
                    "j":j
                })

    def breeding(self):
        for pair in self.pairs:
            l = randint(1, self.n_bits - 1)
            genomes = {
                "1": self.sorted_subjects[pair["i"]].get_string_genome(self.n_bits),
                "2": self.sorted_subjects[pair["j"]].get_string_genome(self.n_bits)
            }
            genomes_splitted = {
                "a1": genomes["1"][:l],
                "a2": genomes["1"][l:],
                "b1": genomes["2"][:l],
                "b2": genomes["2"][l:],
            }
            new_genomes = {
                "1": genomes_splitted["a1"] + genomes_splitted["b2"],
                "2": genomes_splitted["b1"] + genomes_splitted["a2"]
            }
            new_descendants = {
                "1": Subject(binary_string_to_bin(new_genomes["1"]), binary_string_to_int(new_genomes["1"]), self.operation, self.a, self.dx ),
                "2": Subject(binary_string_to_bin(new_genomes["2"]), binary_string_to_int(new_genomes["2"]), self.operation, self.a, self.dx )
            }
            self.descendants.append(new_descendants["1"])
            self.descendants.append(new_descendants["2"])

    def mutation(self):
        for descendant in self.descendants:
            p = random()
            if p <= self.p_mutation:
                genome_string = descendant.get_string_genome(self.n_bits)
                for i in range(len(genome_string)):
                    if random() <= self.p_mutation_gen:
                        char = str(randint(0,1))
                        genome_string = genome_string[:i] + char + genome_string[i + 1:]
                descendant.set_genome(binary_string_to_bin(genome_string))
        
        self.generations.append(deepcopy(self.descendants))

    def cute(self):                                            
        subjects_combined = self.subjects + self.descendants
        subjects_combined_no_repeated = list(set(subjects_combined))
        self.subjects = subjects_combined_no_repeated
        self.descendants = []

    def get_best_subjects(self): 
        for generation in self.generations:
            best = max(generation, key=lambda subject: subject.phenotype)
            self.best_subjects.append(best)
    
    def get_worst_subjects(self):
        for generation in self.generations:
            worst = min(generation, key=lambda subject: subject.phenotype)
            self.worst_subjects.append(worst)

    def get_average_subjects(self):
        regular_point = (self.best_subjects[0].phenotype - self.worst_subjects[0].phenotype) / 2
        for generation in self.generations:
            for subject in generation:
                if subject.phenotype >= regular_point - self.average_tolerancy and subject.phenotype <= regular_point + self.average_tolerancy:
                    self.average_subjects.append(subject)

    def summarize(self):
        print("------------resumen------------")
        print(f'''generaciones: {len(self.generations)}, {len(self.generations[len(self.generations) - 1])}
            mejores: {len(self.best_subjects)}, {self.best_subjects[len(self.best_subjects) - 1]}
            peores: {len(self.worst_subjects)}, {self.worst_subjects[len(self.worst_subjects) - 1]}
            regulares: {len(self.average_subjects)}, {self.average_subjects[int(len(self.average_subjects) / 2)]}
        ''')

    def get_last_generation_points(self):
        points = {
            "general": {
               "x": [],
               "y": []
            },
            "best": {
                "x": self.best_subjects[len(self.best_subjects) - 1].get_x(),
                "y": self.best_subjects[len(self.best_subjects) - 1].get_y()
            },
            "worst": {
                "x": self.worst_subjects[len(self.worst_subjects) - 1].get_x(),
                "y": self.worst_subjects[len(self.worst_subjects) - 1].get_y()
            },
            "average_point":{
                "y": ( 
                    self.best_subjects[len(self.best_subjects) - 1].get_y() - self.worst_subjects[len(self.worst_subjects) - 1].get_y()
                    ) / 2 + self.worst_subjects[len(self.worst_subjects) - 1].get_y()
            }
        }

        for subject in self.generations[len(self.generations) - 1]:
            points["general"]["x"].append(subject.get_x())
            points["general"]["y"].append(subject.get_y())
        
        return points
        
    def get_best_subject(self):
        return max(self.best_subjects, key=lambda subject:subject.phenotype)
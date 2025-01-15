import math
from random import random, uniform, randint
from Subject import Subject

# libreria matplot

def calculate_n(a, b, dx):
    return int((b - a) / dx + 1)

def calculate_n_bits(n):
    return math.ceil(math.log2(n))

def evaluation(x):
    return 0.1 * x * math.log(1 + abs(x)) * math.cos(x) * math.cos(x)

def calculate_dx(a, b, n_bits):
    return (b - a)/ (2 ** n_bits - 1)

def binary_string_to_int(str):
    return int(str, 2)

def binary_string_to_bin(str):
    return bin(binary_string_to_int(str))

a = -20
b = 50 
dx = 0.05

p_breeding = 0.7
p_mutation = 0.5
p_mutation_gen = 0.5

subjects = []
descendants = []
pairs = []
generations = []

sorted_subjects = []

n = calculate_n(a, b, dx)
n_bits = calculate_n_bits(n)
dx = calculate_dx(a, b, n_bits)
n = calculate_n(a, b, dx)

def eval_subjects(a, dx):
    for i in range(n):
        subjects.append(Subject(bin(i), i, evaluation, a, dx))

    print(subjects)

def make_pairs():
    sorted_subjects = sorted(subjects, key=lambda subject: subject.phenotype, reverse=True)
    for i in range(len(sorted_subjects)):
        p = random()
        if p <= p_breeding:
            j = randint(0,i)
            
            pairs.append({
                "i":i,
                "j":j
            })
    return sorted_subjects

def breeding(n_bits, sorted_subjects, operation, a, dx):
    for pair in pairs:
        l = randint(1, n_bits - 1)
        genomes = {
            "1":  sorted_subjects[pair["i"]].get_string_genome(n_bits),
            "2": sorted_subjects[pair["j"]].get_string_genome(n_bits)
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
            "1": Subject(binary_string_to_bin(new_genomes["1"]), binary_string_to_int(new_genomes["1"]), operation, a, dx ),
            "2": Subject(binary_string_to_bin(new_genomes["2"]), binary_string_to_int(new_genomes["2"]), operation, a, dx )
        }
        descendants.append(new_descendants["1"])
        descendants.append(new_descendants["2"])

def mutation(n_bits):
    for descendant in descendants:
        p = random()
        if p <= p_mutation:
            genome_string = descendant.get_string_genome(n_bits)
            print(genome_string)
            for i in range(len(genome_string)):
                if random() <= p_mutation_gen:
                    char = str(randint(0,1))
                    genome_string = genome_string[:i] + char + genome_string[i + 1:]
                else: 
                    break
            descendant.set_genome(binary_string_to_bin(genome_string))
            print(descendant, genome_string)

def cute(subjects, descendants):
    subjects_combined = subjects + descendants
    subjects_combined_no_repeated = list(set(subjects_combined))
    print(len(subjects_combined), len(subjects_combined_no_repeated))




eval_subjects(a, dx)
sorted_subjects = make_pairs()
breeding(n_bits, sorted_subjects, evaluation, a, dx)
mutation(n_bits)
cute(subjects, descendants)

 

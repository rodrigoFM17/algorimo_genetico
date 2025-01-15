class Subject:

    def __init__(self, genome, int_genome, operation, a, dx):
        self.phenotype = operation(a + dx * int_genome)
        self.genome = genome
        self.int_genome = int_genome
        self.operation = operation
        self.a = a
        self.dx = dx

    def eval_phenotype(self):
        self.phenotype = self.operation(self.a + self.dx * int(self.genome, 2))

    def get_string_genome(self, n_bits):
        return self.genome[2:].zfill(n_bits)
    
    def set_genome(self, new_genome):
        self.genome = new_genome
        self.int_genome = int(new_genome, 2)
    
    def __eq__(self, other):
        return self.genome == other.genome
    
    def __hash__(self):
        return hash(self.genome)

    def __str__(self):
        return f"(genome: {self.genome}, int_genome: {self.int_genome}, phenotype: {self.phenotype})\n"
    
    def __repr__(self):
        return f"(genome: {self.genome}, int_genome: {self.int_genome}, phenotype: {self.phenotype})\n"
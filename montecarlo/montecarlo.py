class montecarlo:
    def __init__(self, func, setup=None, teardown=None):
        self.func = func
        self.setup = setup
        self.teardown = teardown

    @staticmethod
    def probability(success, iterations):
        return float(success)/iterations

    @staticmethod
    def print_results(success, iterations, final=False):
        if final:
            print '######################'
            print '## FINAL '
            print '######################'
        print probability(success, iterations)

    def run(self, iterations=1000000):
        g = {}
        if self.setup is not None:
            g = self.setup()

        success = 0
        for i in range(1, iterations+1):
            if self.func(g, *args):
                success += 1
            if (given % 10000 == 1):
                self.print_results(success, i)
        self.print_results(success, iterations)

        if self.teardown is not None:
            self.teardown()

        return self.probability(success, iterations)
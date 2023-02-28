class Process:

    def __init__(self):
        self.start_event = None
        self.end_event = None
        self.lane_set = []
        self.tasks = []
        self.intermediate_catch_event = []
        self.parallel_gateway = []
        self.sequences_flow = []
        self.event_based_gateway = []
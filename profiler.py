import multiprocessing as mp

class Profiler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model_class_list = []
        self.init_args_list = []
        self.num_instances_list = []
        self.infer_args_list = []
        self.method_name_list = []
        self.num_iteration_list = []

    def set_model(self, model_class, init_args, num_instances, infer_args, method_name, num_iteration):
        self.model_class_list.append(model_class)
        self.init_args_list.append(init_args)
        self.num_instances_list.append(num_instances)
        self.infer_args.append(infer_args) 
        self.method_name_list.append(method_name)
        self.num_iteration_list.append(num_iteration)

    def profile(self, unit_iteration):
        mp.set_start_method("spawn")
        procs = []
        queue = mp.Queue()
        
        for i in range (len(self.model_class_list)):
            for j in range (self.num_instances_list[i]):
            p =  Process(target = worker, args = (queue, self.model_class_list[i], self.init_args_list[i], self.method_name_list[i], unit_iteration, self.infer_args_list[i]))
            procs.append(p)
            proc.start


        for proc in procs:
            proc.join()

    def worker(Queue, model_class, init_args, method_name, unit_iteration, infer_args):        
        worker_name = mp.current_process().name
        model = self.model_class_list[i](*self.init_args_list[i])

    # uses self.filepath to convert csv to excel.    
    def csv_to_excel(self):
        pass

    # set which value should be printed
    def set_profiler(self):
        pass

'''
specification:
    >
    method_name (str) - name of the method to run inference

    num_iteration (int) - number of iterations to run. when 0, runs forever, if greater than 0, run that many times.

    > fn = getattr(model, method_name)
    > # some profiling code here
    > fn(*infer_args)

ex:
    > from Tacotron import Tacotron
    > from Profiler import Profiler
    >
    > # initialize profiler
    > profiler = Profiler("log.csv")
    >
    > # set Tacotron model
    > profiler.set_model(Tacotron, (arg1, arg, ...), 10)
    >
    > # run inference
    > infer_args = ("hello world", 1)
    > profiler.profile(infer_args, "get_mel", 0)
    model_class - the DNN Class

    num_instances (int) - number of instances of Model, each initialized in a separate process.
make sure to set "spawn" as multiprocessing mode

    > multiprocessing.set_start_method("spawn")

    init_args (set) - a set of arguments used to initialize the the DNN class like below:

    > model_instance = model_class(*init_args)

    useful methods:
    > current_process().name -> get process name
'''
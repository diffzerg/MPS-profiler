import multiprocessing as mp
import cupy as cp
import time
import numpy as np

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
        self.infer_args_list.append(infer_args) 
        self.method_name_list.append(method_name)
        self.num_iteration_list.append(num_iteration)

    def profile(self, unit_iteration):
        mp.set_start_method("spawn")
        procs = []
        queue = mp.Queue()
        
        for i in range (len(self.model_class_list)):
            for j in range (self.num_instances_list[i]):
                p =  mp.Process(target = self.worker, args = (queue, self.model_class_list[i], self.init_args_list[i], self.method_name_list[i], unit_iteration, self.infer_args_list[i]), self.num_iteration_list[i])
                procs.append(p)
                p.start()

        for proc in procs:
            proc.join()
        
        file = open(self.file_path, 'w')
        while queue.empty() = False:
            file.write(queue.pop())
            file.write("\n")


    def worker(self, Queue, model_class, init_args, method_name, unit_iteration, infer_args, num_iteration):        
        worker_name = mp.current_process().name
        model = model_class(*init_args)
        
        function = getattr(model, method_name)
        time_list = []

        for i in range (num_iteration):
            if ((i + 1) % unit_iteration == 0):
                sum_string = str(model_class) + " " + str(worker_name) + " " + str(i + 1) + " " + str(np.mean(time_list))  + " " + str(np.var(time_list))  
                Queue.put(sum_string)
                time_list.clear()
            start_time = time.time()   
            #run inference code
            function_result = function(*infer_args)
            #synchronize Device
            cupy.cuda.Device(device=0).synchronize()
            end_time = time.time() - start_time
            time_list.append(end_time)
            

    

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
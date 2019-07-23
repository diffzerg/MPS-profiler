class Profiler.__init__(file_path)

"""
model_class - the DNN Class

num_instances (int) - number of instances of Model, each initialized in a separate process.
make sure to set "spawn" as multiprocessing mode

    > multiprocessing.set_start_method("spawn")

init_args (set) - a set of arguments used to initialize the the DNN class like below:

    > model_instance = model_class(*init_args)

"""
Profiler.set_model(model_class, init_args, num_instances)


"""
method_name (str) - name of the method to run inference

num_iteration (int) - number of iterations to run. when 0, runs forever, if greater than 0, run that many times.

    > fn = getattr(model, method_name)
    > # some profiling code here
    > fn(*infer_args)
"""
Profiler.profile(infer_args, method_name, num_iteration, num_transactions)

"""
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

"""

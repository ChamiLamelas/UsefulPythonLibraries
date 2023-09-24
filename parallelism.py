from multiprocessing import Pool, cpu_count


def run_parallel(cpus, targets, argslist):
    assert len(targets) == len(
        argslist), f"len(targets) = {len(targets)} != len(argslist) = {len(argslist)}"
    print(
        f"Running {len(targets)} tasks on {cpus} CPUs. Your system has {cpu_count()} CPUs.")
    pool = Pool(processes=cpus)
    for target, args in zip(targets, argslist):
        pool.apply_async(target, args)
    pool.close()
    pool.join()

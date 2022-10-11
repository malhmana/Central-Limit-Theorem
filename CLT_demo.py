def CLT_demo(population, num_of_samples, sample_size, visualize= False):
    """
    population: Iterable(list,tuple) of the entire population
    num_of_samples: number of samples who's means are to be stored(This is not sample size, i.e the size of the sample taken.)
    sample_size: Size of a single sample taken at a time.
    visualize: Pass this value as True if you want to visualize directly through the function, default is False.
    """
    
    import random
    import seaborn as sns
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
    population = list(population)
    sample_means= []
    count = 0
    for i in range(num_of_samples + 1):
        sample = random.sample(population, sample_size)
        sample_mean= np.mean(sample)
        sample_means.append(sample_mean)
    if visualize:
        sns.distplot(sample_means)
    else:
        return sample_means
        
        

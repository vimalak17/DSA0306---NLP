 

states = ["DT", "NN", "VBZ", "NNS", "VBP", "RB"]

transition = {
    ("DT", "NN"): 1.000,
    ("NN", "VBZ"): 0.625,
    ("VBZ", "NN"): 0.800,
    ("VBZ", "NNS"): 0.200,
    ("NNS", "VBP"): 0.500,
    ("VBP", "NN"): 0.333,
    ("VBP", "RB"): 0.333,
    ("VBP", "NNS"): 0.333
}

emission = {
    ("DT", "The"): 0.600,
    ("DT", "A"): 0.400,
    ("NN", "cat"): 0.250,
    ("NN", "milk"): 0.250,
    ("VBZ", "drinks"): 0.400,
    ("NN", "boy"): 0.125,
    ("NN", "girl"): 0.125
}

print("States")
print(states)

print("\nTransition Dictionary")
for key in transition:
    print(key, "=", transition[key])

print("\nEmission Dictionary")
for key in emission:
    print(key, "=", emission[key])

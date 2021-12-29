def compute_patterns(pattern, inputs=None):
    if inputs is None:
        inputs = []
    inputs.append(pattern)
    patterns = "a list based on " + pattern
    return patterns

print(compute_patterns(pattern='new pattern'))
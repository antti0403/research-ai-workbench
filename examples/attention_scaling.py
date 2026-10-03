"""A synthetic numerical check, not a reproduction of Transformer training."""
import json
import math
import random
import statistics


def check():
    generator = random.Random(42)
    rows = []
    for dimension in (1, 16, 64):
        dots = [sum(generator.gauss(0, 1) * generator.gauss(0, 1)
                    for _ in range(dimension)) for _ in range(6000)]
        scaled = [dot / math.sqrt(dimension) for dot in dots]
        variance = statistics.variance(scaled)
        assert 0.85 < variance < 1.15, 'Illustrative scaled variance is outside the expected range'
        rows.append({'dimension': dimension, 'raw_variance': round(statistics.variance(dots), 4),
                     'scaled_variance': round(variance, 4)})
    # Independent known-case check: two equal scores must average their values.
    scores = [0.0, 0.0]
    weights = [math.exp(score - max(scores)) for score in scores]
    weights = [weight / sum(weights) for weight in weights]
    assert sum(weight * value for weight, value in zip(weights, [10, 20])) == 15
    return {'kind': 'synthetic illustration, not training results', 'seed': 42,
            'samples_per_dimension': 6000, 'rows': rows, 'equal_score_output': 15}


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))

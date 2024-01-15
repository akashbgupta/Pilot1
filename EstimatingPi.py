import random
import time

def estimate_pi_within_time_limit(time_limit):
    start_time = time.time()
    inside_circle = 0
    total_samples = 0

    while time.time() - start_time < time_limit:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

        total_samples += 1

    pi_estimate = (inside_circle / total_samples) * 4
    return pi_estimate, total_samples

if __name__ == "__main__":
    time_limit_seconds = 1

    pi_approximation, num_samples = estimate_pi_within_time_limit(time_limit_seconds)

    print(f"Approximation of pi using {num_samples} samples in {time_limit_seconds} seconds: {pi_approximation}")

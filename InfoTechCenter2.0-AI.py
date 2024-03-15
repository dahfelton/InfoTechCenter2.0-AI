import time
import sys

def boot_up_system():
    """Simulate system boot-up process."""
    total_load_time = 2.5  # Total time for boot-up
    ellipsis_cycles = 4    # Number of ellipsis cycles
    ellipsis_duration = 0.5  # Duration for each ellipsis cycle

    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(1)  # Delay for a better user experience

    print("Booting up InfoTech Center System:")
    start_time = time.time()  # Record the start time

    for cycle in range(1, ellipsis_cycles + 1):
        progress = cycle / ellipsis_cycles  # Calculate progress
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        remaining_time = total_load_time - elapsed_time  # Calculate remaining time

        # Print progress percentage
        print(f"{cycle * 25}% complete")

        # Display ellipsis with calculated progress
        ellipsis = "." * cycle
        sys.stdout.write(f"\r{'InfoTech Center System Booting':<40}{ellipsis:<4}")
        sys.stdout.flush()
        time.sleep(ellipsis_duration)

    # Final message after boot-up
    print("\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_system()

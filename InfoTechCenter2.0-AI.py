import time
import sys

def boot_up_system():
    """Simulate system boot-up process."""
    # Constants for boot-up process
    total_load_time = 2.5  # Total time for boot-up
    ellipsis_cycles = 4    # Number of ellipsis cycles
    ellipsis_duration = 0.5  # Duration for each ellipsis cycle

    # Display welcome message
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(1)  # Delay for a better user experience

    print("Booting up InfoTech Center System:")
    start_time = time.time()  # Record the start time

    # Loop through ellipsis cycles
    for cycle in range(1, ellipsis_cycles + 1):
        # Calculate progress
        progress = cycle / ellipsis_cycles * 100

        # Calculate elapsed time and remaining time
        elapsed_time = time.time() - start_time
        remaining_time = total_load_time - elapsed_time

        # Print progress percentage
        print(f"{progress}% complete")

        # Display ellipsis with calculated progress
        ellipsis = "." * cycle
        sys.stdout.write(f"\r{'InfoTech Center System Booting':<40}{ellipsis:<4}")  # Update line without newline
        sys.stdout.flush()  # Flush output buffer to show the updated line
        time.sleep(ellipsis_duration)  # Wait for the specified duration

    # Final message after boot-up
    print("\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_system()

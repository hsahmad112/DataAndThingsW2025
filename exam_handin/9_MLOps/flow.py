import subprocess, time
import IPython.display as display


def start_mlflow_ui(port=5000):
    print("\nStarting MLFlow UI...")
    process = subprocess.Popen(["mlflow", "ui", "--port", str(port)])  # Starts MLFlow UI on the specified port

    # Wait a moment to ensure the server starts
    time.sleep(3)

    # Print the link to the MLFlow UI
    print(f"MLFlow UI is running at http://localhost:{port}. Press Ctrl+C in the terminal to stop it.")

    try:
        # Keep the script running to keep the port open
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping MLFlow UI...")
        process.terminate()
        process.wait()
        print("MLFlow UI has been stopped.")

if __name__ == "__main__":
    start_mlflow_ui()
import multiprocessing
import os


def process_message(pipe_end):
    current_pid = os.getpid()
    print(f"Child process running with PID: {current_pid}")

    incoming_text = pipe_end.recv()
    print(f"Child received: {incoming_text}")

    result = incoming_text[::-1].upper()

    pipe_end.send(result)
    print("Child sent the modified message back.")


if __name__ == "__main__":
    main_pid = os.getpid()
    print(f"Main process started with PID: {main_pid}")

    main_side, child_side = multiprocessing.Pipe()

    text_to_send = "Operating Systems 2026"

    worker = multiprocessing.Process(
        target=process_message,
        args=(child_side,)
    )

    print("Creating child process...")
    worker.start()

    print(f"Parent sends: {text_to_send}")
    main_side.send(text_to_send)

    print("Parent is waiting for the processed message...")
    final_text = main_side.recv()

    print(f"Message returned by child: {final_text}")

    worker.join()
    print("Child process finished. Program ended correctly.")
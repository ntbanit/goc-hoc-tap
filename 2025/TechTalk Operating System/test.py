import pandas as pd
import io

# Data based on the merged and refined 20 questions (4 options, 1 correct answer)
# The options are simplified and formatted to be concise.
quiz_data = [
    {
        "Question": "What is the primary benefit of Non-blocking I/O (e.g., in Node.js) for high-concurrency, I/O-bound tasks?",
        "Option 1": "It increases the available CPU cores.",
        "Option 2": "It reduces the overhead of frequent Context Switching.",
        "Option 3": "It enables true Parallelism for CPU-bound tasks.",
        "Option 4": "It completely eliminates the need for connection pooling.",
        "Correct Option": 2
    },
    {
        "Question": "Which OS component is responsible for handling the low-level TCP/IP packet transmission for a database request?",
        "Option 1": "The application's connection pool.",
        "Option 2": "The OS Kernel's networking stack.",
        "Option 3": "The Database Management System (DBMS).",
        "Option 4": "The garbage collector (GC).",
        "Correct Option": 2
    },
    {
        "Question": "To achieve true Parallelism for CPU-bound tasks in CPython, what should a developer use?",
        "Option 1": "The single-threaded `asyncio` Event Loop.",
        "Option 2": "The standard `threading` module, relying on the GIL.",
        "Option 3": "The `multiprocessing` module or background workers.",
        "Option 4": "Java Virtual Threads (Project Loom).",
        "Correct Option": 3
    },
    {
        "Question": "How does a Java Virtual Thread (VT) prevent its underlying OS Kernel Thread from blocking during I/O?",
        "Option 1": "The VT uses the Python GIL to yield control.",
        "Option 2": "The VT is unmounted and the kernel thread is returned to a pool.",
        "Option 3": "The VT bypasses the OS and uses direct memory access.",
        "Option 4": "The VT executes the I/O synchronously on the main thread.",
        "Correct Option": 2
    },
    {
        "Question": "In Node.js, the `libuv` library primarily implements what function?",
        "Option 1": "Executing JavaScript bytecode (V8).",
        "Option 2": "Managing the Event Loop and thread pool for blocking I/O.",
        "Option 3": "Serving HTTP requests directly without a web server.",
        "Option 4": "Generating virtual threads for every incoming request.",
        "Correct Option": 2
    },
    {
        "Question": "When reading large files, utilizing application-level buffering helps reduce the number of slow calls to which OS boundary?",
        "Option 1": "The Java Virtual Machine (JVM).",
        "Option 2": "The User Mode / Kernel Mode boundary (System Calls).",
        "Option 3": "The application's heap memory.",
        "Option 4": "The Python Global Interpreter Lock (GIL).",
        "Correct Option": 2
    },
    {
        "Question": "What is the consequence of an application failing to close too many File Descriptors (FDs) or sockets?",
        "Option 1": "An Out-of-Memory (OOM) error due to heap exhaustion.",
        "Option 2": "Hitting the process's hard FD limit, preventing new connections.",
        "Option 3": "Triggering excessive garbage collection cycles.",
        "Option 4": "Disabling the use of the File System Cache.",
        "Correct Option": 2
    },
    {
        "Question": "What is the primary characteristic that distinguishes a Process from a Thread?",
        "Option 1": "A Thread can only perform I/O-bound tasks.",
        "Option 2": "A Process shares its memory space with other processes.",
        "Option 3": "A Process has its own isolated Virtual Memory Space.",
        "Option 4": "Threads have a higher overhead for context switching.",
        "Correct Option": 3
    },
    {
        "Question": "Which resource is explicitly shared by all Threads within a single Process?",
        "Option 1": "The thread's dedicated stack memory.",
        "Option 2": "The entire process's heap memory (for dynamic data).",
        "Option 3": "The current state of the CPU registers.",
        "Option 4": "The unique Thread ID (TID).",
        "Correct Option": 2
    },
    {
        "Question": "Why are frequent System Calls considered a performance bottleneck?",
        "Option 1": "They are always asynchronous and must wait for an Event Loop.",
        "Option 2": "They require the CPU to switch from User Mode to Kernel Mode.",
        "Option 3": "They force the process to release the GIL.",
        "Option 4": "They bypass the OS Kernel entirely.",
        "Correct Option": 2
    },
    {
        "Question": "According to the CAP Theorem, which two properties are often prioritized by globally distributed NoSQL databases (e.g., Cassandra)?",
        "Option 1": "Consistency and Availability (CA).",
        "Option 2": "Consistency and Partition Tolerance (CP).",
        "Option 3": "Atomicity and Isolation (AI).",
        "Option 4": "Availability and Partition Tolerance (AP).",
        "Correct Option": 4
    },
    {
        "Question": "Environment variables enhance security primarily by preventing sensitive data from entering what system?",
        "Option 1": "The OS Kernel.",
        "Option 2": "The Application's heap memory.",
        "Option 3": "The Version Control System (e.g., Git).",
        "Option 4": "The TCP/IP stack.",
        "Correct Option": 3
    },
    {
        "Question": "What is the best practice when a critical environment variable (like a database password) is missing at application startup?",
        "Option 1": "Assume a default value and log a warning.",
        "Option 2": "Crash the application immediately during its startup phase (Fail Fast).",
        "Option 3": "Attempt to fetch the password from a public, remote API.",
        "Option 4": "Wait indefinitely until the variable is externally provided.",
        "Correct Option": 2
    },
    {
        "Question": "What is the primary role of the Operating System (OS), as defined in the slides?",
        "Option 1": "Defining the application's business logic.",
        "Option 2": "Acting as a Resource Manager for CPU, Memory, and I/O Devices.",
        "Option 3": "Managing the application's dependency graph.",
        "Option 4": "Providing a high-level API for object-oriented programming.",
        "Correct Option": 2
    },
    {
        "Question": "What is the main benefit of Process Isolation for application safety?",
        "Option 1": "It allows the OS to run the process in User Mode only.",
        "Option 2": "It enables the OS to contain crashes within a single process.",
        "Option 3": "It simplifies Inter-Process Communication (IPC).",
        "Option 4": "It ensures the CPU burst is longer than the I/O burst.",
        "Correct Option": 2
    },
    {
        "Question": "Process execution alternates between which two fundamental cycles?",
        "Option 1": "Read Burst and Write Burst.",
        "Option 2": "User Burst and Kernel Burst.",
        "Option 3": "Creation Burst and Termination Burst.",
        "Option 4": "CPU Burst and I/O Burst.",
        "Correct Option": 4
    },
    {
        "Question": "Threads within the same Process share the same memory space, which allows for what?",
        "Option 1": "Enforcing memory protection between threads.",
        "Option 2": "Faster data exchange (but requires synchronization).",
        "Option 3": "Avoiding all forms of context switching.",
        "Option 4": "Using a unique stack memory for local variables.",
        "Correct Option": 2
    },
    {
        "Question": "What is the direct consequence when multiple threads access a shared variable concurrently without synchronization (Race Condition)?",
        "Option 1": "Deadlock of the entire operating system.",
        "Option 2": "Immediate process termination.",
        "Option 3": "Data Inconsistency and unpredictable results.",
        "Option 4": "The OS automatically grants Mutual Exclusion.",
        "Correct Option": 3
    },
    {
        "Question": "What is the file system configuration practice recommended in the slides for deployed applications?",
        "Option 1": "Hardcode absolute paths to all files.",
        "Option 2": "Avoid hardcode absolute paths for portability.",
        "Option 3": "Set all file permissions to `777`.",
        "Option 4": "Use only Direct/Random Access.",
        "Correct Option": 2
    },
    {
        "Question": "What is the key best practice for handling File Descriptors (FDs) and socket connections in application code?",
        "Option 1": "Use the 'Ignorance' Deadlock strategy.",
        "Option 2": "Always close file descriptors/socket connections.",
        "Option 3": "Never use connection pooling.",
        "Option 4": "Set the thread pool size to 1.",
        "Correct Option": 2
    }
]

# Create a DataFrame
df = pd.DataFrame(quiz_data)

# Add Option 5 column as empty string as requested (4 or 5 options)
df['Option 5'] = ''

# Rename and reorder columns to match the requested format
df = df.rename(columns={
    "Option 1": "Option 1",
    "Option 2": "Option 2",
    "Option 3": "Option 3",
    "Option 4": "Option 4",
    "Option 5": "Option 5",
    "Correct Option": "Correct Option"
})
df = df[["Question", "Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Correct Option"]]

# Convert the DataFrame to a CSV string
csv_output = df.to_csv("backend_os_quiz.csv", index=False)
print(csv_output)
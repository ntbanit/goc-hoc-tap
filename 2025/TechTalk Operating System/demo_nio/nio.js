const fs = require('fs');
const http = require('http');

// This function DELEGATES the task and allows the main thread to continue.
function nonBlockingRead(callback) {
    // fs.readFile() is the asynchronous, NON-BLOCKING version.
    console.log('2. Starting NON-BLOCKING I/O delegation...');
    
    // The main thread delegates the slow I/O to the OS, provides a callback function,
    // and returns immediately, without waiting.
    fs.readFile('large_file.txt', 'utf8', (err, data) => {
        // This callback runs LATER, when the OS signals the I/O is complete.
        if (err) return callback('Error reading file.');
        console.log('5. I/O operation signaled completion (callback executed).');
        callback(`File read complete (size: ${data.length} bytes)`);
    });
    
    console.log('3. Main thread finished delegation and is READY for next task.');
}

http.createServer((req, res) => {
    if (req.url === '/fast') {
        // This is a fast, non-I/O task.
        console.log('1. Processing /fast request.');
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Fast response completed.');
        console.log('4. /fast request finished.');
    } else if (req.url === '/slow') {
        console.log('1. Processing /slow request.');
        nonBlockingRead((result) => {
            // This is the callback that executes LATER.
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(result);
            console.log('6. /slow response sent.');
        });
    }
}).listen(8081, () => { // Note: using port 8081 to avoid conflict
    console.log('Non-Blocking Server running at http://localhost:8081/');
    // Create a large file for testing
    fs.writeFileSync('large_file.txt', 'X'.repeat(500 * 1024 * 1024)); // 500MB file
});

// To observe the non-block:
// 1. Open your browser to http://localhost:8081/slow
// 2. WHILE IT IS LOADING, open a new tab to http://localhost:8081/fast
// Result: The /fast request will process and complete immediately, even while the /slow request is still waiting for the file read to finish.
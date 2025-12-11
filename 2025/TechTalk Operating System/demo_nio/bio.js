const fs = require('fs');
const http = require('http');

// This function BLOCKS the entire server until the file read is complete.
function blockingRead() {
    // fs.readFileSync() is the synchronous, BLOCKING version.
    console.log('2. Starting BLOCKING I/O...');
    const data = fs.readFileSync('large_file.txt', 'utf8'); 
    console.log('3. Finished BLOCKING I/O.');
    return `File read complete (size: ${data.length} bytes)`;
}

http.createServer((req, res) => {
    if (req.url === '/fast') {
        // This is a fast, non-I/O task.
        console.log('1. Processing /fast request.');
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Fast response completed.');
        console.log('4. /fast request finished.');
    } else if (req.url === '/slow') {
        // This will block the server for several seconds.
        const result = blockingRead();
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(result);
        console.log('4. /slow request finished.');
    }
}).listen(8080, () => {
    console.log('Blocking Server running at http://localhost:8080/');
    // Create a large file for testing
    fs.writeFileSync('large_file.txt', 'X'.repeat(500 * 1024 * 1024)); // 500MB file
});

// To observe the block:
// 1. Open your browser to http://localhost:8080/slow
// 2. WHILE IT IS LOADING, open a new tab to http://localhost:8080/fast
// Result: The /fast request will wait until the /slow request has completely finished.
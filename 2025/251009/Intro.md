# LEET CODE LINK 
https://lgcns-my.sharepoint.com/:x:/p/an_ntb/EV1V1kgnD2JIivolULD-xBIBRE0D0cFU9gMytMFtFZwAEA?e=i7cFuK

#BREAK THE ICE 
chào mn, có ai thấy mặt mình quen k ạ, có thể mình đã pv các bạn lúc đầu vào 
để mình bắt đầu cho nó suôn sẻ thì c 
 C cũng xin tự giới thiệu 1 tý là c tên An, cũng già rồi, sn 94, trước c học PTIT. thì c mong là các bạn sẽ nhớ tên / mặt của nhau và hợp tác tốt với nhau nhé, vì mn sẽ là 1 team dự án để kết thúc cái CTĐT Fresher. và như cá nhân c thì dù lv lâu rồi nhưng mà nc đùa giỡn trao đổi với các bạn lúc trc vào cùng đợt với mình vẫn thấy dễ dàng thân thiết nhất ấy. nên là mong các bạn sẽ cùng nhau có 1 khoảng th.gian bổ ích trong 2 tháng này để trau dồi kiến thức, knlv, kĩ năng giao tiếp, teamwork.. nữa 
.... 
Overview về nội dung training thì chắc các bạn cũng đã được biết 
học ... làm project ... 


Có 1 phần bị lược vì mn nghĩ là ai cũng biết rồi, nhưng mình vẫn sẽ overview qua tý nhé 
Computer Science overview : hardware / software / middleware 
Hardware → The physical parts of a computer system (e.g., CPU, memory, hard drive, keyboard, monitor). It’s what you can touch.
Software → The programs or instructions that tell the hardware what to do (e.g., Windows, Chrome, Python app). It’s what you run.
Operating System (OS) → The main software that manages computer hardware and other software. It controls memory, files, devices, and runs programs (e.g., Windows, Linux, macOS).
Process → A running program. It has its own memory and resources managed by the OS.
Thread → A smaller unit inside a process that shares the same memory but runs tasks in parallel.
Multithreading → Running multiple threads inside one process to do tasks seemingly at the same time.
Concurrent Execution → Tasks start, run, and complete overlapping in time (not necessarily at the same instant). It’s about managing multiple tasks. (cpu switch giữa các task) 
Parallel Execution → Tasks run literally at the same time on multiple CPUs or cores. It’s about speed through true simultaneity.
Cấu trúc dữ liệu và giải thuật 
Understand key points, able to research more about process / thread / stack / heap


TCP (Transmission Control Protocol) → Reliable, connection-based communication.

Ensures data arrives in order, without loss or duplication.

Used for: web pages (HTTP/HTTPS), emails, file transfers.
🧱 Think: guaranteed delivery, slower but safe.

UDP (User Datagram Protocol) → Unreliable, connectionless communication.

Sends data fast, doesn’t check if it arrives.

Used for: video calls, games, live streaming.
⚡ Think: best effort delivery, faster but no guarantee.

🧠 In short:
TCP = reliability, UDP = speed.


Sure — short and simple 👇

HTTP (HyperText Transfer Protocol) → The basic protocol for web communication (e.g., loading websites).

HTTPS → Same as HTTP but secure — data is encrypted using SSL/TLS.

Header → Extra metadata sent with requests/responses (e.g., Content-Type, Authorization, User-Agent).
📨 Tells the server how to handle the data.

Cookie → Small piece of data stored in the browser, sent with each request to the same site.
🍪 Used for login sessions, preferences, and tracking.

🧠 In short:
HTTP = talk, HTTPS = secure talk,
Header = info about the talk, Cookie = memory of past talks.

| Feature    | REST             | GraphQL                | WebSocket          |
| ---------- | ---------------- | ---------------------- | ------------------ |
| Connection | Request–Response | Request–Response       | Persistent         |
| Data       | Fixed endpoints  | Custom queries         | Real-time messages |
| Use case   | Simple APIs      | Flexible data fetching | Live updates/chat  |

CORS (Cross-Origin Resource Sharing)
| Concept                | Meaning                                                |
| ---------------------- | ------------------------------------------------------ |
| **Same-Origin Policy** | Browser blocks cross-site requests by default          |
| **CORS**               | Mechanism to safely allow specific cross-site requests |
| **Fix**                | Server adds `Access-Control-Allow-Origin` header       |

| Feature     | Session Login        | JWT                  | OAuth                             |
| ----------- | -------------------- | -------------------- | --------------------------------- |
| Storage     | Server-side          | Client-side          | External provider                 |
| Type        | Authentication       | Authentication       | Authorization                     |
| Scalability | Limited              | High                 | High                              |
| Use case    | Traditional web apps | APIs / microservices | “Login with Google” or API access |

Certificates

A digital ID card for the website, issued by a trusted authority (CA — Certificate Authority).

Proves the website is real (not fake) and enables encryption.

When you visit https://example.com:

Browser requests the site’s SSL certificate.

It checks if the certificate is valid and signed by a trusted CA.

If valid → browser and server create an encrypted channel using public/private keys.

| Category                     | Examples                                                                                                                   | Why                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 🔑 **Secrets & Credentials** | - Database username/password <br> - API keys (e.g. AWS, OpenAI, Google Cloud) <br> - Access tokens <br> - SSH private keys | Anyone with repo access could misuse or leak them |
| ⚙️ **Environment Configs**   | - `.env` files <br> - `config.json` with sensitive values                                                                  | Should be managed securely, not stored in code    |
| 🧠 **Encryption Info**       | - Secret keys for JWT <br> - TLS private keys <br> - OAuth client secrets                                                  | Exposing these breaks authentication & security   |
| 🧍 **User Data**             | - Personal info <br> - Password hashes <br> - Session data                                                                 | May violate privacy or compliance (GDPR, etc.)    |
| 💻 **System Access**         | - Server IPs or admin URLs <br> - VPN credentials                                                                          | Can help attackers find or enter your systems     |
| 🧩 **Third-party Config**    | - Firebase config (if contains API key) <br> - Payment provider secrets                                                    | Often used to impersonate your app                |



OK hơi giông dài 1 chút, giờ thì để cho tỉnh ngủ thì hqua mn đã học về Overview CS rồi đúng k, phần hqua cũng khá lq đến buổi hnay, và c nghĩ là làm j cũng cần output, nên c mời mn join quiz này để nhắc lại 1 chút kt hqua nhé 

.... 
Cảm ơn mn đã join quiz, giờ mình sẽ start nội dung chính của buổi hôm nay nhé 

### 
thi thoảng thì c sẽ hỏi mn 1 số nội dung, c hi vọng câu trả lời sẽ kp là "e kb" mà sẽ là "e đoán nó là ABC" hay j đó nhé -> dù câu trả lời là XYZ .. thì cũng đừng sợ sai, việc sai sẽ giúp chúng ta nhớ lâu hơn, hiểu hơn vấn đề 

#OVERVIEW 
1. vì sao SA quan trọng : 
- cái gì build nên cũng cần 1 kiến trúc, và khi chúng ta phát triển 1 cái hệ thống ngày càng lớn, thì sẽ ngày càng khó để thay đổi cái kiến trúc đó  resources: $$$$ , time, human .. 
- kiến trúc hệ thống thể hiện 
    + Mục đích của sản phẩm
    + Chất lượng của sản phẩm 
- ví dụ kiến trúc của 1 rạp hát vs của 1 ngôi nhà 
    + 1 cái để xem, trình diễn buổi biểu diễn 
    + 1 cái để ở 
    nếu swap ? vẫn có thể dùng được, nhưng sẽ cực kì bất tiện 
- tương tự với 1 phần mềm, có vô số cách để cấu trúc code, mỗi cách lại dùng cho một mục tiêu khác nhau 
- kiến trúc hệ thống phần mềm sẽ ảnh hưởng đến 
    + Operational 
    + Security
    + Reliability
    + Performance 
    + Cost 
	...
** Vì SAO DEV CẦN BIẾT VỀ KIẾN TRÚC HỆ THỐNG 
-> có cái nhìn tổng quan về công việc mình đang làm : kiểu xây nhà .. 
có thể nắm được các kiến thức căn bản, hợp tác tốt hơn với các thành viên khác trong team, đọc hiểu tài liệu... -> WORK BETTER 

2. Định nghĩa SA
- Kiến trúc phần mềm của 1 hệ thống là 1 bản mô tả nâng cao của các thành phần cấu tạo nên nó, cách chúng giao tiếp với nhau để hoàn thiện các yêu cầu / ràng buộc của hệ thống 

+ 1 bản mô tả nâng cao -> mô tả trừu tượng các thành phần, không đi vào chi tiết cách cài đặt 
    [..] các công nghệ / ngôn ngữ lập trình là 1 phần trong chi tiết cách cài đặt 
+ các thành phần giao tiếp với nhau: các thành phần cũng là 1 black box, và chi tiết bên trong chúng cũng rất phức tạp
+ hoàn thiện các yêu cầu / ràng buộc của hệ thống : PHẢI LÀM GÌ / ĐỂ LÀM GÌ / KHÔNG NÊN / KHÔNG ĐƯỢC LÀM GÌ 
SYSTEM REQUIREMENTS 
- functional 
- non-functional 
- limit boundaries : resources : cost, time, pics ...
	technical : programing language, cloud / os /device .. ..  
	/ business : cost, time, pics
	/ legal : global / regional .. -> user data sharing 
** negotiation OR loosely couple architecture ?
FEATURE REQUIREMENTS 
1. METHODS:
- ask the client (not always a good method)
- use cases & user flows 
	+ use cases : situation / scenario 
	+ user flows : step by step of each use case 
2. STEPS: 
- define all actors / users of systems 
- define all possible use cases -> expand with user flows 
	+ UML 
NON-FUNCTIONAL REQUIREMENTS
Consider : 
- testable 
- measureable 
Tradeoff
- 

 SA là output của design, input của implement trong SDLC
tổng quan về SDLC 

# PILLARS 

# COMMON COMPONENTS 
1. API 
##2. API Gateway -> cổng chào : 
có thể giăng băng rôn, biển hiệu chào đón, cũng có thể có bác bảo vệ bắt xuống xe xuất trình giấy tờ/ hoặc là block lại k cho đi 

### 8. Protocol Conversion
**Example**: A client sends a request using the SOAP protocol (common in legacy systems), but the backend service only supports REST over HTTP. The API Gateway converts the SOAP request into a RESTful HTTP request by transforming the XML payload into JSON and adjusting the communication protocol, then forwards it to the backend service. For instance, a SOAP request to `GetUserDetails` might be converted to a REST `GET /users/{id}` endpoint.

### 9. Error Handling
**Example**: A client sends a request to an API, but the backend service is down, resulting in a 503 Service Unavailable error. The API Gateway intercepts this error, logs it for debugging, and returns a user-friendly response to the client, like `{"error": "Service temporarily unavailable, please try again later"}`, instead of exposing the raw server error. It might also trigger a notification to the ops team to address the issue.

### 10. Circuit Breaking
**Example**: A backend service starts failing repeatedly due to overload. The API Gateway implements a circuit breaker pattern: after 5 consecutive failures within 30 seconds, it "opens" the circuit, temporarily halting requests to that service for 1 minute. During this time, the Gateway returns a fallback response, like `{"message": "Service is currently down, using fallback data"}`, and might serve cached data or route to a backup service if available.

### 11. Logging/Monitoring
**Example**: For every incoming request, the API Gateway logs key details like the client’s IP address, timestamp, endpoint called, response status, and latency. For instance, a log entry might look like: `[2025-06-05 20:18:00 KST] Client: 192.168.1.1, Endpoint: /api/v1/users, Status: 200, Latency: 120ms`. This data is sent to a monitoring tool like Prometheus, which can trigger alerts if the error rate exceeds 5% in a 10-minute window.

### 12. Caching
**Example**: A client requests a product catalog via `GET /api/v1/products`. The API Gateway checks its cache (e.g., Redis) and finds a recent response for this endpoint, cached with a TTL of 5 minutes. Instead of forwarding the request to the backend, the Gateway returns the cached response, reducing load on the backend and improving response time. If the cache is stale or empty, it fetches a fresh response and caches it for future requests.

These examples show how an API Gateway enhances functionality beyond basic request routing, improving reliability, performance, and security.


## 3. ELB 
Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs).

The image illustrates two realistic use cases of a Load Balancer (LB) in a system architecture, labeled by ByteByteGo.

Failure Handling: On the left, clients send requests to the Load Balancer (LB), which distributes them to multiple application (APP) instances. One instance fails (marked "Failed"), and the LB detects this failure. It stops routing traffic to the failed instance (shown with a dashed line) and redirects all traffic (100%) to the healthy instances, which respond with a 200 (OK) status code, ensuring uninterrupted service.
Instance Health Checks: On the right, the LB performs health checks on the application instances by periodically sending requests to a /health endpoint (indicated by a heartbeat icon). If an instance responds with "Not OK," the LB marks it as unhealthy (dashed line) and stops sending traffic to it. Traffic is then routed only to the healthy instances, which respond with 200 (OK), maintaining system reliability.
In summary, the image shows how a Load Balancer ensures system stability by handling instance failures and conducting health checks to route traffic only to healthy application instances.

Why This Order?
The API Gateway provides a unified entry point for API management, security, and routing logic, which should happen before load distribution.
The Load Balancer focuses on distributing traffic to backend instances, which is a lower-level concern that comes after the API Gateway’s request processing.


# 4. Message Broker 
A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures. Messages are stored on the queue until they are processed and deleted. Each message is processed only once, by a single consumer. Message queues can be used to decouple heavyweight processing, to buffer or batch work, and to smooth spiky workloads.


The image compares two communication approaches between a Sender and Receiver: a Blocking API Call versus an Asynchronous Communication model using a message broker.

Left Side: Blocking API Call
The Sender makes a direct, synchronous API call to the Receiver.
The communication is represented by a single arrow with an envelope icon, indicating a request.
A red "X" labeled "Blocking API call" highlights that the Sender must wait for the Receiver to process the request and respond, which can lead to delays or failures if the Receiver is slow or unavailable.
Right Side: Asynchronous Communication
The Sender sends a message to a message broker (depicted as a cylinder with envelopes), which acts as an intermediary.
Key benefits are listed:
Asynchronous Communication + ACK: The Sender receives an acknowledgment (ACK) immediately after sending the message, allowing it to continue processing without waiting for the Receiver.
Decoupling: The Sender and Receiver operate independently, as the message broker handles message delivery.
Fault Tolerant: The system can handle failures (e.g., if a Receiver is down) since messages are queued in the broker.
Scalability: Multiple Receiver instances can process messages from the broker, improving system capacity.
The broker distributes messages to one or more Receivers, ensuring reliable delivery.
Summary
The image contrasts the limitations of blocking API calls (delays, dependency) with the advantages of asynchronous communication (speed, fault tolerance, scalability) using a message broker.

#  5. CDN 
A content delivery network (CDN) is a network of interconnected servers that speeds up webpage loading for data-heavy applications. CDN can stand for content delivery network or content distribution network. When a user visits a website, data from that website's server has to travel across the internet to reach the user's computer. If the user is located far from that server, it will take a long time to load a large file, such as a video or website image. Instead, the website content is stored on CDN servers geographically closer to the users and reaches their computers much faster.


# 6. Database 
SQL vs NoSQL 
ACID 
Sure! Let’s compare the ACID properties of SQL to something familiar, like baking a cake:

ACID Properties
Atomicity: Think of this as the “all or nothing” rule. When baking a cake, you can’t just bake half a cake and call it done. Either you bake the whole cake, or you don’t bake it at all. Similarly, in a database, a transaction must be fully completed or not done at all.
Consistency: This ensures that the cake follows the recipe correctly. If the recipe says to add 2 cups of flour, you must add exactly 2 cups. In a database, consistency means that any transaction will bring the database from one valid state to another, maintaining all rules and constraints.
Isolation: Imagine you’re baking a cake in a busy kitchen. Even if others are cooking around you, your cake ingredients and process shouldn’t be affected by what others are doing. In databases, isolation ensures that transactions are processed independently without interference from other transactions.
Durability: Once your cake is baked and cooled, it should stay intact even if the power goes out or the kitchen gets messy. In a database, durability means that once a transaction is committed, it will remain so, even in the event of a system failure.
By ensuring these properties, databases maintain accuracy, reliability, and integrity, much like how following a recipe ensures a delicious cake every time! 🍰

Does this analogy help clarify the ACID properties for you?

# PATTERNS AND STYLES 


# QUIZ TIME 

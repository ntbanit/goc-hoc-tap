[1]
Xin chào mọi người, mình là An, lời đầu tiên xin cảm ơn mọi người đã join buổi Tech Talk ngày hôm nay 
Chia sẻ một chút tại sao lại có buổi Tech Talk hôm nay, là vì lúc trước thì mình và Tú Anh cũng có viết một vài bài trong nhóm, nhưng sếp Thành cũng thấy việc viết bài chưa hiệu quả trong việc thúc đẩy tinh thần học tập trong Team lắm nên cần chuyển thành những buổi Tech Talk ntn. 
Bản chất của việc tổ chức Tech Talk này thì nó cũng hơi giống buổi seminar hôm trước Tĩnh là speaker, nhưng mà quy mô nhỏ hơn trong Team chứ kp trong cty, và thời lượng cũng ngắn hơn tầm 1-2h, và tổ chức thường xuyên hơn tầm 2 tuần 1 lần 
Về buổi ngày hôm nay thì mình muốn bắt đầu bằng chủ đề Database, vì Team mình là "DnA - Data and AI" và đây là chủ đề liên quan đến công việc hàng ngày trong project của mình. 
Tham gia buổi hôm nay thì cũng có những bạn không chuyên về kỹ thuật hoặc chưa làm việc nhiều đến data, mình hy vọng là những chia sẻ ngày hôm nay sẽ đều dễ hiểu và có thể giúp ích cho việc học tập hay là công việc sau này của mọi người. 
Slide thì cũng xấu do toàn đi cóp chỗ này nhặt chỗ kia ạ : Youtube 1 tý, Udemy, Book, Blog ... mn thông cảm 
Cũng có nhiều kiến thức mình mới tìm hiểu, hoặc trong quá trình mình chia sẻ thì nếu cso gì sai sót mong mọi người góp ý giúp ạ 

[2]
Nội dung buổi Tech Talk hôm nay của mình thì gồm 3 phần chính
Trước hết sẽ là Sơ lược về Database, sau đó là đi sau vào 1 vài loại database cụ thể và một vài ví dụ trong các dự án thực tế, sau cùng là đi vào chi tiết các khái niệm quan trọng trong SQL (Relational Database) 

[3]
Phần đầu là sơ lược về database ạ

[4]
Đầu tiên là đi vào định nghĩa
Về data thì là dữ liệu, bất cứ thông tin gì mà máy tính có thể xử lý đều được xem là data đúng không ạ, còn base thì là cái kho chứa. Sơ lược về Database thì đây là một định nghĩa tổng quan: Database là nơi tập hợp data để lưu trữ, quản lý, tìm kiếm, biến đổi một cách thuận tiện
Database là thành phần sau cuối của một ứng dụng, đóng vai trò quan trọng vì nó là nơi lưu trữ, quản lý data, đảm bảo an toàn và dễ dàng truy cập đến data khi cần. 
Database cũng thường được xây dựng để có thể scale ngang hoặc dọc. Dọc là mình tăng kích thước lưu trữ, ngang là thêm nhiều instance chẳng hạn ..   để tối ưu performance,
Security thì đảm bảo chỉ những user được qua author, athen mới có thể truy cập data, hoặc là cấp quyền thêm sửa xóa data, thay đổi cấu hình các table cho từng user, mã hóa data nhạy cảm như password.. để đảm bảo tính bảo mật
Backup thì là hệ thống được xây dựng để database có thể tự động có một bản sao khác và có thể phục hồi ngăn ngừa khả năng mất mát dữ liệu. Ví dụ như data chỉ được lưu ở 1 server (1 cái máy chủ nào đó) thì nếu máy đó chết có thể sập cả hệ thống, nhưng nếu lưu trên nhiều server A B C thì nếu máy A chết mình có thể trỏ sang máy B C (cái này thì thường là ở các database trên cloud) 

[5]
Tiếp theo là phân loại data
Các loại data phổ biến thì là structured: thường được tổ chức quy củ, có cấu trúc cố định, đồng nhất với nhau, dữ liệu đã được xử lý từ trước khi lưu vào database, thường liên hệ đến SQL, hay là file CSV, Excel - có các cột và hàng cố định, dễ dàng query. Ví dụ với một bảng data ntn thì mình có thể nhìn ra ngay là sản phẩm nào bán được số lượng nhiều nhất đúng không ạ 
Un-structured, ngược lại là các data không có cấu trúc cố định gì cả, thường chưa được xử lý trước khi lưu vào database, có thể có rất nhiều format, thường liên hệ đến các file như text, videos, audio, images, emails... , rất khó để query. Ví dụ mình muốn biết video đó nói về nội dung gì, ai là người đăng, bài hát này thì lyrics là gì, ca sĩ nào, nằm trong album nào ... 
Semi-structured thì là nằm giữa 2 loại trên, nó không có cấu trúc cố định như structured, nhưng cũng không hỗn loạn như Un-structured, ví dụ như các file XML, JSON, email headers, log files.. 

[6]
Đây là một cái hình minh họa mình thấy khá phù hợp với 3 loại data này
Structured thì như 1 cái hình mảnh ghép hoàn chỉnh
Un-structured thì rời rạc gần như hoàn toàn, rất khó mà ghép lại được
còn semi-structured thì không hẳn là rời rạc, nhưng cũng không hẳn là ghép lại được 

[7]
Tiếp theo là các tính chất của data: gồm có 3 chữ V này. Nó quyết định đến cách mình lưu trữ, xử lý data, lựa chọn database cần dùng cho ứng dụng 
Volume: Khối lượng data mà mình cần lưu trữ, xử lý, phân tích trong một khoảng thời gian nào đó. 
Ví dụ ở các nền tảng mạng xã hội SNS như FB, X, Tiktok, Youtube, Thread.. thì hàng ngày có thể lên đến hàng TB (terabyte) bài post, ảnh, videos.. 
Hoặc các hệ thống bán hàng như Shoppee, Lazada, Tiki... thì có thể lên đến hàng PB (petabytes) dữ liệu giao dịch thanh toán hàng tháng 
Velocity : tốc độ mà data mới được sinh ra, thu tập, xử lý. liệu mình có thể xử lý bằng batch hàng ngày, hàng giờ, hay là cần xử lý realtime ? Ví dụ , trên các ứng dụng như Google Maps, cần cập nhật location trên từng giây chẳng hạn.. 
 hoặc là như các ứng dụng liên quan đến IoT như xe tự lái, hoặc là health care như Apple Watch thì sensor data cần đọc lên đến mili giây
Variety: là sự đa dạng của data formats, cấu trúc dữ liệu, hoặc được thu thập từ những nguồn khác nhau 
Ví dụ như một doanh nghiệp bán hàng cần thu thập data từ cả các giao dịch lưu trong SQL, JSON logs, lượt xem sản phẩm trên web, apps.. 
hay là hệ thống sức khỏe cần thu thập data từ các thiết dị điện tử, hoặc thiết bị đeo tay, email feedback của khách hàng ... 

[8]
 3 chữ V này. Nó quyết định đến cách mình lưu trữ, xử lý data, lựa chọn database cần dùng cho ứng dụng
 Tùy vào bài toán đặt ra mà chúng ta sẽ lựa chọn loại database phù hợp. Tiếp theo mình sẽ đi vào một số loại database phổ biến hiện nay 

[9] 
Các loại database thông dụng hiện nay thì Relational hay là SQL vẫn đang rất phổ biến 
*insert here* vì nó gồm các data đã được chuẩn hóa, có tính chính xác, toàn vẹn dữ liệu, có quan hệ liên kết với nhau, dễ dàng query, có ACID, hỗ trợ index, optimize hiệu năng, security ... SQL đã tồn tại hơn 50 năm, cộng đồng sử dụng rất nhiều, nhiều tool support, phổ biến. Dù nó không phải lựa chọn tốt nhất nhưng có thể sử dụng SQL trong hầu hết các trường hợp của ứng dụng. Nhược điểm của nó thì là khó scale ngang, khó xử lý với data unstructured, semi-structured, performance giảm nếu data set lớn, query quá phức tạp , khó thay đổi schema khi change requirement chẳng hạn 

Hiện nay theo mình thấy thì các project trong công ty cũng đang chủ yếu sử dụng SQL, và chủ yếu cá nhân mình cũng làm việc nhiều đến SQL nhất, nên mình sẽ có riêng 1 phần đề nói về nó, còn NoSQL mình sẽ sơ lược ở đây thôi, vì mình cũng mới tìm hiểu để làm slide, nói nhiều lại sai ạ 
Những database khác thì có thể được gọi chung là NoSQL (Not Only SQL vì không thể thay thế hoàn toàn SQL truyền thống được), nó được sinh ra để khắc phục những nhược điểm của SQL, một số loại phổ biến gồm có 
*Key-Value* Redis : lưu trữ dữ liệu nhỏ, cấu  trúc phức tạp, lưu dạng key-value, tốc độ truy cập đọc -ghi cao,  dễ dàng scale ngang , thường dùng trong các ứng dụng real time, caching, cần độ trễ rất thấp
Ứng dụng như là cache, quản lý session, ranking trong game .. 
*Time-series* InfluxDB dữ liệu dạng time-stamped , tự động sort theo time, High write and query performance, có thể nén dữ liệu, dễ dàng set up policy để xóa những dữ liệu cũ (giúp DB nhẹ hơn), scale ngang 
Thích hợp cho những data realtime thay đổi rất nhanh như thị trường chứng khóa, cổ phiếu, đấu giá online, monitoring system 
*Graph* Neo4J thích hợp cho những dữ liệu unstructured có quan hệ phức tạp, lưu dưới dạng đồ thị các đỉnh và cạnh , có thể duyệt dựa trên các thuật toán đồ thị 
Ví dụ ứng dụng mạng xã hội gợi ý kết bạn, ản phẩm, video yêu thích, phân tích lỗi hệ thống, 
*Document* MongoDB. Thích hợp với data lớn. Không có scema cố định, JSON or BSON, nhưng cũng ít thay đổi, sharding là scale ngan, có replication để High availability 
Ví dụ ứng dụng Content Management Systems (lưu thông tin về các bài báo, định dạng HTML, có cái cây dynamic, hierarchical or nested data structures, gì đó, hay quản lý catalog sản phẩm bán hàng) data những cái này thì thường không giống nhau, thêm mới thường xuyên nhưng update thì ít đúng không ạ, thường sẽ update theo ngày theo tháng gì đó 
*Wide column* với Columnar thì theo mình cùng loại nhé, cái wide thì nó có thể những thằng trống này k lưu gì thay gì lưu null 
HBase, Cassandra Thường dùng cho big data, analytics, reporting, etc., những data không được chuẩn hóa
Mỗi row thì sẽ có thể có column khác nhau. vì các cột sẽ luôn có cùng kiểu dữ liệu nên có thể nén data lại và có performance lớn hơn lúc đọc dữ liệu . dùng trong các ứng dụng về gợi ý sản phẩm, video yêu thích , big data and analytics applications,
IoT device data, time-series data

*Text Search* ElasticSearch : full text search, analytics trong log hay event data 
Ứng dụng: Auto completer, spell checker
Full-text search on Wikipedia
Full-text search on StackOverflow
*Object Store* này thì mình có biết đến S3 của AWS, thường lưu file dạng blob (binary large object, ncl có thể hiểu rất khó thay đổi 1 nội dung nhỏ trong file, mà phải thay đổi cả file) nên hay lưu audio, video, ảnh... thay vì text file, giá cả rất rẻ, thực ra theo mình cái này nên được list là storage hơn là database 
NoSQL thì cũng có nhược điểm là data không được chuẩn hóa như SQL, thường có kiểu query khác nên cũng có khó khăn tích hợp với SQL, vì là scale ngang nên là độ consitency (nhất quán) cũng thấp hơn SQL, nhiều DB không được thiết kế để support query phức tạp hay là transaction
Gần đây thì có NewSQL là mô hình DB hiện đại cố tìm cách kết hợp ưu điểm của SQL và NoSQL nữa, nhưng mà mình cũng chưa biết gì và thời lượng buổi TechTalk hạn chế nên không cho vào slide, bạn nào hứng thú thì tìm đọc thêm giúp mình ạ 

[10]
Dưới đây là 1 vài RDBMS phổ biến nhất hiện tại, mỗi loại đều có ưu nhược điểm riêng, dưới đây là bảng so sánh tương đối * Scale này lát ở phần sau mình sẽ có nói thêm 

[11]
đây là bảng so sánh tương đối một vài NoSQL DB 
Tunable là có thể điều chỉnh được 
Như mình đã nói lúc nãy thì hầu hết các DB này đều có QL riêng 
Có phần ACID với Consistency Model thì là đặc trưng của SQL thì có 1 số DB hỗ trợ ntn
Mn có thể tham khảo thêm 

[12] 
Đây là file cheatsheet database trên các nền tảng cloud phổ biến hiện nay, mình thì chỉ biết mỗi AWS nên chỉ nói riêng về phần này thôi nhé 
Khi mình chọn 1 cái service trên cloud thì thường cso lợi thế là rẻ, nhanh hơn mình tự build ở local, và nó có nhiểu service nên support lẫn nhau 
 
*RDS, Aurora*: 2 cái này thì cũng na ná nhau, chỉ khác là RDS support nhiều loại SQL hơn như có cả MySQL, PostgreSQL, MariaDB, Oracle, and Microsoft SQL Server. Aurora thì chỉ có MySQL, PostgreSQL. Aurora thì đắt tiền hơn, support Serverless, hiệu năng cao hơn.  
OLTP (Online Transaction Processing) cái này thường dùng cho những bài toán cần transactional data như e-commerce, banking, and order processing.
Focuses on write-heavy operations, such as inserting, updating, and deleting records.
-> ROW-BASED

*Redshift*:
OLAP (Online Analytical Processing): Designed for complex queries and data analysis, often used in data warehousing and business intelligence. 
Data Operations: Focuses on read-heavy operations, such as aggregating, summarizing, and analyzing large volumes of data.
Reporting, data mining, and decision support systems.
Data Operations: OLAP is read-heavy, focusing on complex queries, whereas OLTP is write-heavy, focusing on transaction processing.
Data Structure: OLAP uses multidimensional models, while OLTP uses normalized relational databases.
-> COLUMN-BASED : phân tích dữ liệu bán hàng, giao dịch chứng khoán, lượt click quảng cáo, trend toàn cầu 

*DynamoDB*: HA cao, thích hợp với hệ thống phân tán, support hàng triệu requesst/ giây. Mỗi bảng thì có thể có vô hạn rows (items), nhưng mỗi rows thì bị giới hạn về size, và PK thì cần đặt lúc tạo bảng, có thể tạo thêm partionkey , sort key, support caching, stream cho real time data, support query bằng SQL 

*ElastiCache* implement Redis, Memcache 

*Keyspaces* implement Cassandra  And so, with keyspaces you get Cassandra directly managed. And it will automatically scale tables up and down
based on the application's traffic.
Thường dùng cho big data, analytics, reporting, 

*Timestream*: các ứng dụng lần xuất báo cáo theo năm, ví dụ doanh số bán hàng của 1 sản phẩm theo ngày của 1 mặt hàng -> nhanh và rẻ hơn rất nhiều lần dùng RDS . data thì tự động sort theo time nên dễ dàng set up policy lưu trữ data, data lâu quá 1 năm sẽ bị xóa đi chẳng hạn 
-> IoT app, phân tích báo cáo real time 

*Neptune*: with highly connected datasets, so like a social network. 1 người bạn của mình đọc, like cái gì đó, chơi game gì check in ở đâu thì nó hay hiện lên new feed của mình luôn đúng k ạ. đấy là cách graph DB hoạt động nhờ các thuật toán duyệt đồ thị 
hoặc khi tìm đường trên map chẳng hạn, đi đường ngắn nhất đến đâu, đường A tắt thì rẽ đường B chẳng hạn , phát hiện lỗi (như trong trò xếp hình có 1 miếng k khớp) 

*DocumentDB* : implement MongoDB (JSON, BSON data) 

*Opensearch*: (formally để tên là ElasticSearch) thì mn cũng hiểu là nó implement rồi đó, cái chuyện đổi tên này thì nó liên quan đến drama bản quyền gì gì đó , license, tích hợp cả Kibana nữa, ( tool để visual dữ liệu) 
 full text search, analytics trong log hay event data 
Ứng dụng: Auto completer, spell checker
Full-text search on Wikipedia
Full-text search on StackOverflow
Ngoài ra dùng cho big data, analytics, reporting, 

*S3*: rẻ và lâu đời, nên được dùng rất nhiều, ngày ngày càng có nhiều tool support ... nói qua về blob 

[13]
Đó như mn thấy thì có thể cùng 1 bài toán, nhưng mình có thể dùng 1 trong nhiều công cụ để giải quyết, và các loại db cũng có điểm giống nhau, khác nhau, hay là bị lai tạp dần.. 
Trong những hệ thống lớn, phức tạp thì thường là sẽ kết hợp rất nhiều database với nhau, mỗi loại đều có ưu điểm nhược điểm khác nhau, không có cái gì hoàn hảo trong mọi trường hợp, nên là có thể tính năng này dùng DB A, tính năng module kia dùng DB B là chuyện bình thường, mình cần chọn đúng DB cho trường hợp cụ thể
*Sau đây là ví dụ về một hệ thống tương tự như Netflix *
- RDS: Dùng MySql để lưu những thông tin người dùng, các giao dịch thanh toán.. 
- Columnar: Dùng Apache Spark, Redshift, Tableau để phân tích dữ liệu, tạo báo cáo biểu đồ.. 
- Key-value: Caching bằng Memcache, theo mình thì cái này cũng tương tự Redis, dùng để hiện homepage, show recommendation
- Wide-column: Cassandra , db default lưu thông tin về video (meta data), diễn viên, phim, user data như device, history watching.. 
- Text Search thì dùng Elastic Seach
- S3 is the default choice and stores almost everything related to Image/Video/Metrics/Log files.

[14]
Hiện nay theo mình thấy thì các project trong công ty cũng đang chủ yếu sử dụng SQL, và chủ yếu cá nhân mình cũng làm việc nhiều đến SQL nhất,
SQL đã tồn tại hơn 50 năm, cộng đồng sử dụng rất nhiều, nhiều tool support, phổ biến. Dù nó không phải lựa chọn tốt nhất nhưng có thể sử dụng SQL trong hầu hết các trường hợp của ứng dụng.
Sau đây thì mình sẽ đi vào chi tiết 1 số concept mình nghĩ là quan trọng trong SQL 

[15] 
Trước tiên là mình sẽ nói về các kiến thức cơ bản về SQL, cái này mình sẽ nói hơi nhanh, vì mình nghĩ phần này cũng dễ hiểu ạ 
chỗ màu tím này là định nghĩa, mình nghĩ k cần thiết lắm nên cắt bớt đi, viết tắt của Structured Query Language (tổ chức dữ liệu thành hàng và cột ntn), dễ mô hình hóa data vì phản ánh các data trong thực tế đều có quan hệ gì đó với nhau
Chỗ màu cam này là có PK, FK, unique Key, Composite Key là kết hợp nhiều cột làm key 
Example: Combination of order_id and product_id in an order_details table.
Join Types: thiều full join là lấy cả 2 bên 

[16] 
Tiếp theo là các kiến thức cơ bản liên quan đến coding và theo mình Thường để build 1 ứng dụng thì mn chỉ cần dừng lại ở nắm được slide này là đủ
 1. DDL (Data Definition Language)
Purpose: Defines the structure of the database, including tables, indexes, and constraints.
Commands:
CREATE: Creates a new table, view, or other database object.
ALTER: Modifies an existing database object.
DROP: Deletes a database object.
TRUNCATE: Removes all records from a table, but not the table itself.
2. DQL (Data Query Language)
Purpose: Retrieves data from the database.
Commands:
SELECT: Fetches data from one or more tables.
3. DML (Data Manipulation Language)
Purpose: Manipulates data within the database.
Commands:
INSERT: Adds new records to a table.
UPDATE: Modifies existing records in a table.
DELETE: Removes records from a table.
4. DCL (Data Control Language)
Purpose: Controls access to data within the database.
Commands:
GRANT: Gives a user access privileges to the database.
REVOKE: Removes access privileges from a user.
5. TCL (Transaction Control Language)
Purpose: Manages transactions within the database to ensure data integrity.
Commands:
COMMIT: Saves all changes made in the current transaction.
ROLLBACK: Undoes all changes made in the current transaction.
SAVEPOINT: Sets a point within a transaction to which you can later roll back.
These SQL command types help in managing and manipulating the database effectively, ensuring data integrity, security, and efficient data retrieval.

Do you have any specific questions about these commands or how to use them?

[17] 
Sau đây là các phần hơi nâng cao 1 chút, mình sẽ cố gắng nói 1 cách dễ hiểu nhất nên có thể sẽ không thể đi vào chi tiết được quá nhiều
Cảnh báo trước với mn là từ phần này về sau nghe sẽ khá là đau đầu và khó hiểu ạ.
Nhưng theo mình đã là dev mà làm việc lâu năm với SQL thì những cái này cần phải nắm đc, và nó cũng chưa phải level expert 
Phần này mình nghĩ là cần thiết khi bạn là người có nhiệm vụ build bảng ở trong DB mà data đã chuẩn chỉ sẵn rồi thì nên nắm được
Chuẩn hóa DB: mức càng cao thì DB sẽ càng chuẩn, vì mình đang làm việc với SQL nên việc data có model chuẩn cần thiết, mình thấy có thể mn sẽ quên do vì bây giờ NoSQL đang ngày càng phổ biến, nên mình nhắc lại (mà NoSQL thì data lưu k cần chuẩn j cả) 

[18]
Chuẩn 1NF: chuẩn này thì khá đơn giản nên thực ra thì hầu hết mn đều đang làm rồi
1- 1 column k được mix datatype
2- k có 2 column trùng tên 
3- không để thông tin nào được quyết định bởi thứ tự các dòng
4- có khóa chính PK (k trùng nhau, k null) 
mấy cái này thì thực ra trong RDBMS hiện đại nó đều tự động hết rồi
chỉ có cái này mình nghĩ là có thể mn sẽ dễ quên 
5- không lưu thông tin kiểu group trùng lặp

[20]
2NF là 1 NF, với thêm 1 điều kiện, những cột k phải key phải phụ thuộc hoàn toàn vào key (nếu key có 2 cột thì phụ thuộc vào key 2 cột, key 1 cột thì ...) 

[22]
3NF là 2NF, những cột k phải key phải phụ thuộc hoàn toàn vào key (2NF) 
 với thêm 1 điều kiện, và những cột k phải không phụ thuộc vào bất kì cột nào khác ngoài key 

[24]
Fourth Normal Form (4NF)
4NF deals with multi-valued dependencies. A table is in 4NF if it is in Boyce-Codd Normal Form (BCNF) and has no multi-valued dependencies.

[26]
5NF, or Project-Join Normal Form (PJNF), deals with join dependencies. A table is in 5NF if it is in 4NF and cannot be decomposed into smaller tables without losing information.

[27]
Which One is Better?
The choice between 3NF and 5NF depends on your specific needs:

3NF: This is often sufficient for most practical applications. It reduces redundancy and avoids update anomalies, making it easier to maintain data integrity1.

5NF: This is more advanced and is used in cases where the database needs to be free of all join dependencies. It is typically used in complex databases where data integrity and minimal redundancy are critical2.

In general, 3NF is more commonly used because it strikes a good balance between normalization and performance. 5NF is used in more specialized scenarios where the highest level of normalization is required.

có thể hiểu đơn giản là k lưu data kiểu là kết quả của phép join ấy, vì sẽ bị trùng lặp dữ liệu 
Mình để link video minh họa dễ hiểu ở đây ạ. Mn có thể xem qua 
https://www.youtube.com/watch?v=GFQaEYEc8_8 

[28]
**Transaction**
A transaction really is nothing but a collection of SQL queries that are treated as one unit of work.
And the reason we are treating this as one unit of work, because the the nature of SQL or the structured  query language is my data is, is is structured, it has many tables. So it's very hard to do everything you want in one query. Sometimes it's impossible, right?
So that you really need to do one or more queries to achieve what you logically want at the application.
Usually transactions are used to change and modify data. That's that's what we always think about transaction.
But actually it's perfectly normal.To have a read only transaction.
**WHEN**Read-only transactions are useful in scenarios where you need to ensure data consistency and integrity while performing read operations without making any changes to the data. Here are some common situations where read-only transactions are beneficial:
- Reporting and Analytics: When generating reports or performing data analysis, you want to ensure that the data remains consistent throughout the transaction. A read-only transaction ensures that the data you read is not modified by other transactions during the process.
- Data Integrity Checks: When performing data integrity checks or validations, you want to ensure that the data remains unchanged during the validation process. A read-only transaction helps maintain data consistency.
- Snapshot Isolation: In scenarios where you need to take a consistent snapshot of the data at a specific point in time, a read-only transaction ensures that the data remains unchanged during the snapshot process.
- Long-Running Queries: For long-running queries, a read-only transaction ensures that the data remains consistent throughout the duration of the query, preventing any changes that could affect the query results.
BEGIN COMMIT ROLLBACK 

[32]
**Atomicity**
It's like an atom. And until now, an atom cannot be split. atomic bombs. DARK JOKE nuclear fission 
*QnA* - nếu trong 1 transaction có 100 query, 98 cái chạy OK, cái 99 failed (do lỗi syntax hoặc runtime error gì đó) thì cái 98 cái trc đó và cái 100 sẽ ntn ? 
>>> 
(1) như ai cũng đã biết -> rollback 
(2) commit thành công 
(3) sẽ ntn nếu cái 99 kia đang chạy, nhẽ ra nó k lỗi j, nhưng RDBMS bị sấp, ví dụ server mất điện =>>> cũng auto rollback 
cái này là tùy cách từng loại RDBMS Thì sẽ khác nhau vd Postgres, vd 1 số cái khác ... UNDO .. REDO lúc restart 

[32]
**Isolation**
PROBLEMS (Read phenomena) 
SOLUTION (Isolation Levels) 

[38] 
Dirty Read: A transaction reads data written by another uncommitted transaction.
Dirty Read : Đọc data mà bị rollback later 
>> tệ hại nhất, hầu hết defaul Isolation Level của RDBMS đã chặn cái này rồi, nhưng có cái vẫn cho enable lại 

[41]
Non-repeatable Read: A transaction reads the same row twice and finds different data each time because another transaction has modified the row.
Non-repeatable Read : Đọc data mà bị commit giữa chừng 
defaul Isolation Level của hầu hết RDBMS 

[44]
Phantom Read: A transaction re-executes a query and finds that the set of rows satisfying the query condition has changed due to another transaction inserting or deleting rows.

[49]
Lost Update
A lost update occurs when two or more transactions simultaneously update the same data, and one of the updates is overwritten by another, resulting in the loss of the first update.

[50]
SOLUTION (Isolation Levels) 
● Read uncommitted - No Isolation, any change from the outside is visible to the transaction, committed or not.
● Read committed - Each query in a transaction only sees committed changes by other transactions
● Repeatable Read - The transaction will make sure that when a query reads a row, that row will remain unchanged while its running.
● Snapshot - Each query in a transaction only sees changes that have been committed up to the start of the transaction. It's like a snapshot version of the database at that moment. 
(chụp ảnh cả cái db tại time đó) 
● Serializable - Transactions are run as if they serialized one after the other. >> Reduce Concurrency 

**● Each DBMS implements Isolation level differently**
Locking Mechanism:
Pessimistic: Locks data until transaction completes
Optimistic: Checks for conflicts at commit time
● Pessimistic - Row level locks, table locks, page locks to avoid lost updates
● Optimistic - No locks, just track if things changed and fail the transaction if so
● Repeatable read “locks” the rows it reads but it could be expensive if you read a lot of rows, postgres implements RR as snapshot. That is why you don’t get phantom reads with postgres in repeatable read
● Serializable are usually implemented with optimistic concurrency control, you can implement it pessimistically with SELECT FOR UPDATE

[52]
**Consistency**
Consistency in DATA : Model, constraints :PK, FK, unique, not null, default, check ... 
Consistency in READ
cái mình data đang có có phải là cái thực sự đang lưu trong bộ nhớ k ? 
đương nhiên là phải lấy ra từ DB, nhưng khi DB có nhiều instans, nhiều sharding ... -> dữ liệu có thể khác . vì 1 db để ghi (master) nhiều replica chẳ hạn ... 

[53]
Consistency in DATA : Model, constraints :PK, FK, unique, not null, default, check ... -> define by user (người dùng DB)
ví dụ : picture 1 có 2 like, picture_likes check ra đúng là có Jon với Edmond like thật ...
-> data nhất quán với nhau 
ví dụ nữa là ng đăng ảnh 2 xóa ảnh đi thì data ai like ảnh 2 (ở đây là jon cũng tự động xóa đi) DELETE ON CASADE 
VD trong transacion chuyển tiền, ông A muốn chuyển tiền cho ông B 100k mà còn có 99k -> fail, rollback (vi phạm 1 cái constrain đc setup trc) 
[54]
Consistency in READ : Ông đỏ update X xong, commit rồi liệu ông xanh đọc X có thấy được ngay lập tức không 
cái mình data đang có có phải là cái thực sự đang lưu trong bộ nhớ k ? 
đương nhiên là phải lấy ra từ DB, nhưng khi DB có nhiều instans, nhiều sharding ... -> dữ liệu có thể khác . vì 1 db để ghi (master) nhiều replica chẳ hạn ... 
Trade of for performance in NoSQL : Eventualy -> no right or wrong answer. 
● Strong consistency ● guarantees that every read operation returns the most recent write operation's result, regardless of which node the read operation is executed on. This ensures that all clients always see the same data at the same time. 
Cons:
Higher latency due to the need to synchronize data across all nodes.
Reduced availability and scalability, as the system may need to wait for all nodes to be updated before responding to a read request.

●Eventual Consistency ●  given enough time, all nodes will converge to the same value for a given data item. However, there may be temporary inconsistencies between nodes. NCL đọc rất nhanh nhưng có thế k đúng, vì phải tầm 5p, 10p giữa cách node mới synch data với nhau 1 lần chả hạn 
Pros:
High availability and low latency, as nodes can respond to read and write requests independently.
Better scalability, as the system does not need to synchronize data across all nodes immediately.
Cons:
Temporary inconsistencies may occur, which can be problematic for applications requiring real-time data accuracy.
Requires conflict resolution mechanisms to handle data discrepancies.

[55]
**Durability** : Changes made by committed transactions must be persisted in a durable non-volatile storage. NCL commit rồi thì server có bị sập thì lúc bật RDBMS lên lại thì vẫn có cái data mình đã commit 
cái này chủ yếu là DB nó implement hết rồi nên mình cũng kc hiểu nhiều mình chỉ nói qua thôi, b nào đam mê tìm hiểu sâu thì tự tìm hiểu thêm nhé ạ , mình đọc nhiều thấy đau đầu quá nên skip
● Durability techniques : 
	○ WAL - Write ahead log
		Writing a lot of data to disk is expensive (indexes, data files, columns, rows, etc..) That is why DBMSs persist a compressed version of the  changes known as WAL (write-ahead-log segments
		-> viết hết lên disk thì rất chậm -> viết lên mem, ghi log trc, lúc restart RDBMS thì check log có thể sửa lại data trong disk 
		Description: Before any changes are made to the database, they are first written to a log. This log is used to redo the changes in case of a system crash.
		How it works: The log records the details of each transaction before it is applied to the database. If a failure occurs, the log can be used to replay the transactions and restore the database to a consistent state1.
	○ Asynchronous/Synchronous snapshot: chụp lại cả DB 
	○ AOF
	(Append Only File) is a persistence mechanism used in databases like Redis to ensure durability. 
	Logging Operations: AOF logs every write operation received by the server. These operations are appended to the AOF file.
	Replaying Logs: Upon server startup, the AOF file is replayed to reconstruct the original dataset. This ensures that all write operations are reapplied, maintaining data consistency
**● Each DBMS implements differently**

chốt lại cái hình 4 màu này sau đống slide dài quá dài thì thì mình cần nhớ gì lúc code, lv với SQL nc 
A: transaction BEGIN COMMIT ROLLBACK, VÀ đang trong transaction mà DB sập thì cũng rollback hết   
I: 4 cái Isolation level để set lúc dùng transaction  
● Read uncommitted 
● Read committed 
● Repeatable Read 
● Snapshot
● Serializable
C: DATA build data model : mấy cái chuẩn NF kia, mấy cái từ khóa PK, FK, unique, not null, default, check mấy cái ràng buộc >0 on insert / delete update thì CASCADE hay là set null hay là default hay là k làm j ... trigger function procedure ... j j đó 
READ RDBMS nếu k sharding mặc định là STRONG consistency
D: chỉ cần biết là nó như vậy thôi là đc

[58]
SQL Execution Order giups 
Sure! Here are some tips to help you write faster SQL queries:

Use Indexes: Indexes can significantly speed up data retrieval. Make sure to index columns that are frequently used in WHERE, JOIN, and ORDER BY clauses.

Avoid "SELECT star": Instead of selecting all columns, specify only the columns you need. This reduces the amount of data transferred and processed.

Use Joins Wisely: Be mindful of the type of joins you use. Inner joins are generally faster than outer joins. Also, ensure that the join conditions are properly indexed.

Limit the Number of Subqueries: Subqueries can be slow. Try to use joins or temporary tables instead.

Optimize WHERE Clauses: Use indexed columns in your WHERE clauses and avoid functions on columns in the WHERE clause, as this can prevent the use of indexes.

Use Proper Data Types: Ensure that you are using the most efficient data types for your columns. For example, use INT instead of VARCHAR for numeric data.

Avoid Unnecessary Columns in GROUP BY and ORDER BY: Only include columns that are necessary for your query.

Use Query Execution Plans: Analyze the execution plan of your query to identify bottlenecks and optimize accordingly.

Batch Updates and Inserts: Instead of updating or inserting rows one at a time, batch them together to reduce the number of transactions.

Regularly Update Statistics: Ensure that your database statistics are up-to-date to help the query optimizer make better decisions.

Do you have a specific query you're working on that you'd like help with?
 
[59]
Both B-tree and bitmap indexes are used to improve the performance of database queries, but they have different use cases and characteristics:

B-tree Indexes -> ID, date time ...  / default 
Structure: B-tree indexes are balanced tree structures that maintain sorted data and allow searches, sequential access, insertions, and deletions in logarithmic time.
Use Case: Ideal for columns with high cardinality (many unique values), such as primary keys or columns with unique constraints.
Performance: Efficient for transactional systems (OLTP) where data is frequently updated. They perform well with range queries and equality searches.
Storage: Typically require more storage space compared to bitmap indexes.
Bitmap Indexes -> Category low cardinality
Structure: Bitmap indexes use bitmaps (arrays of bits) to represent the presence of a value in a column. Each bit in the bitmap corresponds to a row in the table.
Use Case: Best suited for columns with low cardinality (few unique values), such as gender or status columns. They are commonly used in data warehousing and decision support systems (DSS).
Performance: Highly efficient for read-heavy operations and complex queries involving multiple conditions. They are not ideal for environments with frequent updates, as updating a bitmap index can be costly.
Storage: Generally require less storage space, especially for columns with low cardinality, due to the compression of bitmaps.
When to Use Each
B-tree Index: Use when you have high-cardinality columns, need to support frequent updates, and require efficient range queries.
Bitmap Index: Use when you have low-cardinality columns, the environment is read-heavy with infrequent updates, and you need to perform complex queries with multiple conditions.
Would you like more details on how to implement these indexes in a specific database system?

[62] 
cái execution plan này thì mỗi một rdbms nó lại khác nhau nên mình nói 1 cái đại diện thôi nhé 
chém gió chém gió oracle 
chạy từ dưới lên theo tứ tự sql order đã nói ở trên 

#TODO ##
Execution Plan -> nói DETAIL về những phần mình hiểu của Oracle, check lại cái git repo cũ ... 

## Sơ lược thôi# về Partitioning vs Sharding

## Sơ lược thôi Concurrency Control

## Lướt lướt về Replication và Security 

# Discusion >>> QnA của mn + QUIZZ
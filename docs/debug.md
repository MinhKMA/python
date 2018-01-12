## Python Debug

### I.What is debugging

Debugging hay còn được gọi là debug. Debugging là quá trình để tìm và gỡ lỗi chương trình máy tính, được xử lý một cách có phương pháp bởi các phần mềm lập trình thông qua các công cụ gỡ lỗi. Gỡ lỗi kiểm tra, phát hiện và sửa lỗi hoặc lỗi để cho phép chương trình hoạt động theo quy định.

### II. How many way to debug in Python

#### 6 Quick python debugging tips :

##### 1. The humble print statement

Nền tảng của hầu hết các câu lệnh gỡ lỗi là câu lệnh print, để câu lệnh này kết thúc chỉ cần thêm một vài chữ để hiển thị trên màn hình . Đây là một cách tuyệt vời để kiểm tra tại chỗ rằng mọi thứ đang được thực hiện.

Ví dụ nếu bạn không thấy bất kỳ văn bản mong muốn nào của mình :

- Đoạn code chưa được gọi tới.
- The stdout đang được chuyển hướng tới đâu đó.

Trường hợp print () thực sự hữu dụng là khi bạn muốn xác nhận thực hiện mã nhanh chóng, hoặc trên một máy chủ từ xa.

##### 2. import logging

Từ nền việc sử dụng print() nhưng tiến cao hơn một chút là sử dụng thư viện logging trong python. Kỹ thuật này phức tạp hơn nhưng có một số ưu điểm: 

- Các level khác nhau của logging được dùng để kiểm soát mức độ chi tiết (error vs warning vs debug)
- Gửi một output đến nơi khác.

Bạn có thể cấu hình logging đến các file log (giống như là syslog dành cho máy tính của bạn) hoặc thậm chí đến những nơi lưu log khác như log.io. 

Logging services thật tuyệt vời bởi vì chúng cho phép bạn thu thập tất cả nhật ký của mình tại một nơi mà bạn có thể tìm kiếm hoặc chia sẻ chúng.

##### 3. An IDE debugger

Có nhiều nhiều tiện ích khi sử dụng một Integrated Development Evironment (IDE) và tiện ích lớn nhất là việc tích hợp vào đó một trình gỡ lỗi. 

Một intergrated debugger cho phép developer thực hiện code của họ và sau đó kiểm tra nó khi code đó được thực hiện. 

##### 4. pdb: The command line debugger

Đôi khi bạn không thể sử dụng một IDE để gỡ lỗi cho code của bạn. Trong những trường hợp này việc sử dụng module pdb được tích hợp vào thư viện python là rất hữu ích.

Khá nhiều thứ bạn có thể làm với một IDE debugger mà bạn có thể làm với pdb. Sự khác biệt lớn nhất là pdb thường sẽ sử dụng trong terminal và các command cũng khó tiếp cận hơn. 

Sử dụng pdb cực kì hữu ích trên các máy từ xa. Mặc dù có thể kết nối với một IDE nhưng nó khá phức tạp thay vì bạn ssh vào và sử dụng pdb để tìm và giải quyết vấn đề trong code của bạn.

##### 5. pdb++

Một số tip của pdb nổi bật:

- `args or locals()` : Hai lệnh này sẽ cho bạn thấy các đối số đã được thông qua trong phạm vi hiện tại, hoặc các biến hiển thị trong phạm vi hiện tại.
- `cpaste` : Nếu bạn có một đoạn code mà bạn muốn paste vào thì bạn sử dụng cpaste thay vì phải từng dòng một.

##### 6. Debugging from the REPL

***Note: this tip only works in ipython, not in the standard Python 2.7 REPL***

### III. How to setup debug in Pycharm?

Sau đây mình xin hướng dẫn các bạn cách debug một chương trình đơn giản

- Ví dụ đây là một chương trình bạn muốn debug: 

<img src = "https://i.imgur.com/8Ynjodf.png">

- Bước 1: click chuột trái vào lề trái của dòng code mình muốn bắt đầu debug với nó :

<img src = "https://i.imgur.com/VimhgyG.png">

- Bước 2: Sử dụng tổ hợp phím `shift + F9` hoặc click chuột phải chọn `Debug'tên file'`

<img src ="https://i.imgur.com/0avd9pq.png">

- Bước 4: sử dụng F8 để debug từng dòng một theo từng bước một 

Mỗi bước nó sẽ hiển thị giá trị và kiểu của các biến mà từng dòng nó đã gọi tới

<img src ="https://i.imgur.com/NCH59oE.png"> 

Thông qua đó người lập trình viên có thể tìm ra những lỗi trong code của mình. 

- Bước 5: Sử dụng tổ hợp phím `ctrl + F2` để stop debug Hoặc `ctrl F5` để rerun debug

  
Có thể còn nhiều cách debug sâu hơn nhưng ở bài viết này mình chỉ đề cập đến vài bước đơn giản :) 



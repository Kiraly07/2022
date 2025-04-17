# WRITE-UP 

```text
switch ($req->username) {
        case 'godmode':
            /* No password is required in god mode */
            $_SESSION['login'] = true;
            $_SESSION['admin'] = true;
            break;

        case 'admin':
            /* Secret password is required in admin mode */
            if (sha1($req->password) === ADMIN_PASSWORD) {
                $_SESSION['login'] = true;
                $_SESSION['admin'] = true;
            }
            break;

        case 'guest':
            /* Guest mode (low privilege) */
            if ($req->password === 'guest') {
                $_SESSION['login'] = true;
                $_SESSION['admin'] = false;
            }
            break;
    }
```
Khi theo dấu code, ta thấy có một đoạn switch, và từ khóa này trở thành manh mối.
Ta thử tìm trên Google với từ khóa php switch danger (https://stackoverflow.com/questions/31819412/unexpected-php-switch-behavior), và phát hiện rằng trong PHP, so sánh trong switch sử dụng so sánh lỏng (loose comparison) – 
tức là không cần cùng kiểu dữ liệu, chỉ cần có thể "ép kiểu" tương đương là được. Trong so sánh lỏng, biểu thức như true == "any_string" sẽ trả về TRUE,
vì PHP ngầm chuyển "any_string" thành boolean, và bất kỳ chuỗi không rỗng nào cũng được coi là true

Sau đó ta có thể thử intercept (chặn) request như sau:
```text
{
  "username": true,
  "password": "iamgod"
}
```
Do true == "admin" là false, nhưng true == true là true, nên nếu có case xử lý với true, nó sẽ bị khớp — điều này dẫn đến bypass logic xác thực và ta có thể truy cập , từ đó nhận được flag.

Flag: CakeCTF{y0u_mu5t_c4st_2_STRING_b3f0r3_us1ng_sw1tch_1n_PHP}

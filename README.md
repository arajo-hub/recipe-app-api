# Recipe App API 명세서
## 회원
### 가입
```json
POST /api/user/create
```
* Request
	- email : @와 .을 포함한 문자열
	- password : 5글자 이상(문자, 숫자, 특수문자 포함 가능)
	- name : 최대길이 255바이트의 문자열

* Response
	- SUCCESS : 200, OK
	* FAIL
| 종류       | 코드   |  메세지  |
| --------   | -----:  | :----:  |
|  email에 @ 혹은 .이 포함되어 있지 않음  |  400  |  "Enter a valid email address."  |
|  password가 5글자 미만으로 입력됨  |  400  |  "Ensure this field has at least 5 characters."  |

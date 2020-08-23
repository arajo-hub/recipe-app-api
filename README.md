# Recipe App API 명세서
## 회원
### 가입
```json
POST /api/user/create
```
* Request
	- email : @와 .을 포함한 문자열
	- password : 5글자 이상(문자, 숫자, 특수문자 포함 가능)
	- name : 최대길이 255자의 문자열

* Response
	- SUCCESS : 200, OK
	* FAIL

|종류|코드|메세지|
|:--:|:--:|:---:|
|email에 @ 혹은 '.'이 포함되어 있지 않음|400|"Enter a valid email address."|
|password가 5글자 미만으로 입력됨|400|"Ensure this field has at least 5 characters."|
### 토큰 생성
```json
POST /api/user/token
```
* Request
	- 가입한 로그인 정보로 로그인

* Response
	- SUCCESS : 200, OK
	* FAIL : "Unable to authenticate with provided credentials"
### 회원정보 변경
```json
POST /api/user/me
```
* Request
	- email : 변경할 문자열(@와 .을 포함)
	- password : 변경할 5글자 이상(문자, 숫자, 특수문자 포함 가능) 비밀번호
	- name : 변경할 문자열(최대길이 255자)

* Response
	- SUCCESS : 200, OK
	* FAIL

|종류|코드|메세지|
|:--:|:--:|:---:|
|email에 @ 혹은 '.'이 포함되어 있지 않음|400|"Enter a valid email address."|
|password가 5글자 미만으로 입력됨|400|"Ensure this field has at least 5 characters."|

## 재료
### 등록
```json
POST /api/recipe/ingredients
```
* Request
	- Name : 최대길이 255자의 문자열

* Response
	- SUCCESS : 200, OK

## 태그
### 등록
```json
POST /api/recipe/tags
```
* Request
	- Name : 최대길이 255자의 문자열

* Response
	- SUCCESS : 200, OK

## 레시피
### 등록
```json
POST /api/recipe/recipes
```
* Request
	- Title : 최대길이 255자의 문자열
	- Ingredients : 콤보박스에서 재료 1개 선택
	- Tags: 콤보박스에서 태그 1개 선택
	- Time minutes : 정수
	- Price : 실수(소수점 두번째자리까지 가능)
	- Link : URL(선택)

* Response
	- SUCCESS : 200, OK

### 이미지 업로드
```json
POST /api/recipe/recipes/<int:pk>/upload-image
```
* Request
	- Image : 이미지파일 선택하여 업로드

* Response
	- SUCCESS : 200, OK
	* FAIL

|종류|코드|메세지|
|:--:|:--:|:---:|
|이미지 확장자가 아닌 파일 업로드|400|"Upload a valid image. The file you uploaded was either not an image or a corrupted image."|

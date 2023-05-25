# \* 재빙

SSAFY 관통프로젝트로 만든 영화 웹 서비스 입니다.

&nbsp;

## 1. 실행 방법

백 서버 경로에 진입합니다.

```bash
> cd final-pjt-back
```

pip로 프로젝트에 필요한 패키지를 설치합니다.

```bash
> pip install -r requirements.txt
```

migrate를 한 뒤 fixture을 통해 영화 데이터를 로드 합니다.

```bash
> python manage.py makemigrations
> python manage.py migrate
> python manage.py loaddata movies1.json
```

Django 프로젝트를 실행합니다

```bash
> python manage.py runserver
```

&nbsp;

## 2. 업무 분담

정재욱 : DB / 장고 REST API 설계, 장고 로직 구현, Vue 로직 구현, CSS

안솔비 : 화면 설계 및 CSS, Vue 로직 구현, REST API 활용

&nbsp;

## 3. 사용 기술 및 개발 계획

#### Frontend

- Vue : 2.7.14
- vuex : 2.0.
- Axios : 1.4.0
- bootstrap-vue : 2.23.1
- eslint : 7.32.0
- vue-js-modal : 2.0.1
- vue-carousel : 0.18.0
- vue-moment : 4.1.0
- Node.js : 18.16.0

#### Backend

- Django : 3.1.3
- Django REST framework : 3.12.2
- Python : 3.9.13

&nbsp;

#### 개발 계획

- 진행 기간 : 2023.05.17 - 2023.05.25
- 목표 : 영화 포털 사이트의 기본 기능과 시인성 좋은 서비스를 구현.

#### 노션 계획 내역

- 간단 정리
  ![D25EC51D-9705-493A-A62C-AD34366E3F12.jpg](../\final-pjt\final-pjt-front\src\assets\images\D25EC51D-9705-493A-A62C-AD34366E3F12.jpg)
- 메인
  - <위>
    - https://getbootstrap.com/docs/4.0/components/carousel/ 최신영화 or 추천 등등
      https://github.com/eunjineee/PICKME_AVG27.5-ver2
    - 네브바( 홈버튼, 회원가입, 로그인 → 영화 추천 게시판으로 바로)
    - 홈페이지 소개
  - <아래>
    - 투자 정보(각자 계좌)
    - 사업자 등록 정보 : 무면허 불법
    - 전화문의
- 네브바 (홈, 게시판, 회원가입, 로그인, 내프로필(햄버거))
- \*영화 게시판(영화 데이터는 최소 50개 이상)
  - <필수>
  - 나라별, 장르별, 평점별, 랜덤(리스트 별로), 등급별(성인/아동), 년도별
  - 영화 상세 페이지 - 리뷰 댓글있음(+ 영화 좋아요)
    - 포스터, 개봉일, 등급, 러닝타임, 줄거리, 감독/출연진, 예고편 영상 + (구분선) 리뷰(평점) 댓글
      - 예고편 동영상 넣는법
      - https://www.codingfactory.net/11880 - 배경 영상
  - <API별 정보>
    - online json https://jsonviewer.stack.hu/
    - tmdb my api https://www.themoviedb.org/settings/api?language=ko
    - tmdb api https://developers.themoviedb.org/3/getting-started/introduction
    - nowplaying: 등급, 언어, 제목, 줄거리, 평점, 개봉일
    - popular: 등급, 언어, 제목, 줄거리, 평점, 개봉일
    - top_rated: 등급, 언어, 제목, 줄거리, 평점, 개봉일
    - credits: cast(출연진) crew(감독: directing)
      출연진 + {0~9} 이름
      감독 + 이름
    - videos
      key 값을 youtube의 v= 뒤에 넣으면 됨.
  - <번외>
  - 영화 명대사 맞추기 (맞추면 영화 명대사 장면 재생)
  - 영화배우 mbti 검색 게시판
- *로그인 / *로그아웃

  - 회원가입

    - 아이디 닉네임(되면 하고) 이메일 비밀번호 비밀번호확인 개인정보사용동의
    -

    ```
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = ''
            self.fields['username'].help_text = ''
            self.fields['username'].widget.attrs['placeholder'] = "Username"
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = ''
            self.fields['password1'].widget.attrs['placeholder'] = "Password"
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = ''
            self.fields['password2'].widget.attrs['placeholder'] = "Confirm Password"

    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('first_name', 'last_name',)
            labels = {
                'first_name': '',
                'last_name': '',
            }
    ```

  - 로그인
    - 아이디 비밀번호
  - 로그아웃
  - 아이디 비밀번호 찾기
  - 회원탈퇴

- *커뮤니티(해쉬태그) - *팔로우, \*댓글
  - - 개인 프로필 ( 쓴 글 & 댓글, 좋아요 한 글, 팔로우 / 팔로잉, 내가 주인이라면 - 수정 가능)
      - 프로필 사진 구현: [https://okayoon.tistory.com/entry/vuejs-기초-세미나-후기-3회차-코딩애플](https://okayoon.tistory.com/entry/vuejs-%EA%B8%B0%EC%B4%88-%EC%84%B8%EB%AF%B8%EB%82%98-%ED%9B%84%EA%B8%B0-3%ED%9A%8C%EC%B0%A8-%EC%BD%94%EB%94%A9%EC%95%A0%ED%94%8C)
  - 영화 리뷰 게시판
  - 영화 찾아주세요 ㅠㅠ 게시판
  - 영화 잡담
  - 영화 짤방
  - 영화 이스터에그
  - 댓글 달 수 있음
- \* 좋아요
  - 내가 보고 싶은 영화 좋아요 누르기(좋아요 눌러있는 영화를 기반으로 모아놓은 페이지)
- 해당 기능 중 기능 설명에 있는 기능 들만 구현(브레인스토밍의 30%)

&nbsp;

## 4. ERD

![장고 DB](../final-pjt/final-pjt-front/src/assets/images/erd.png)

&nbsp;

## 5. 핵심 기능

### 1) 영화 추천

![영화 추천](..\final-pjt\final-pjt-front\src\assets\images\moviereviewtrue.PNG)

- 영화 상세 페이지에서 특정 영화에 리뷰를 남기게 되면 해당 영화 장르에 카운트 1회 증가.

![영화 추천](..\final-pjt\final-pjt-front\src\assets\images\recommended.PNG)

- 영화 페이지에서 가장 횟수가 많은 장르의 영화를 골라 4개 추천.

### 2) 회원 가입 및 로그인

![회원 가입](..\final-pjt\final-pjt-front\src\assets\images\signup.PNG)

- 요구 정보를 입력하고 개인정보 이용 약관에 동의 하게 되면
- 미동의 시 가입 불가 경고창 alert
- 입력 정보 오류 시 경고창 alert

![개인정보동의](..\final-pjt\final-pjt-front\src\assets\images\이용약관.PNG)

![로그인](..\final-pjt\final-pjt-front\src\assets\images\login.PNG)

- 회원가입 후 로그인 가능
- 입력 정보 오류 시 로그인 불가 경고창 alert
- jwt 활용 보안
- 로그인 시 사용자 정보를 local storage에 저장하여 새로 고침 시 로그인 상태 유지
- 로그아웃 시 삭제

### 3) 영화 페이지

![영화 HIT MOVIE](..\final-pjt\final-pjt-front\src\assets\images\movie_hit.PNG)

![추천 및 영화 리스트](..\final-pjt\final-pjt-front\src\assets\images\recommend_movielist.PNG)

- 우측 상단 캐러셀에 히트작들을 보여줌
- 하단 순서대로 추천 영화 리스트
- 히트작 밑 버튼으로 장르 선택 시 해당 장르의 영화 리스트를 캐러셀로 출력(Default로 액션)

![영화 디테일](..\final-pjt\final-pjt-front\src\assets\images\moviereviewtrue.PNG)

- 디테일 페이지에서는 영화의 포스터, 제목, 내용, 예고편을 볼 수 있음
- 하단에서는 평점과 추천 여부 리뷰를 작성하고 리뷰 리스트를 표현(admin의 경우 작성 불가)
- 리뷰 작성자와 로그인 유저가 같을 경우 수정 및 삭제 버튼 표시

### 4) 커뮤니티 게시판

![게시글 목록](..\final-pjt\final-pjt-front\src\assets\images\post.PNG)

- 작성한 게시글 리스트과 각각의 번호, 제목, 작성자, 작성 시간을 표시

![게시글 디테일](..\final-pjt\final-pjt-front\src\assets\images\postdetail.PNG)

- 게시글 작성자, 제목, 내용, 작성일시, 수정일시, 댓글, 댓글 리스트, 좋아요 버튼 표시
- 역시 로그인 한 유저와 작성자가 일치 할 경우 수정, 삭제 버튼 표시
- admin은 모든 게시글을 삭제 할 수 있음
- 작성자명 클릭 시 해당 작성자의 프로필로 이동
- Go To List 클릭 시 게시글 목록으로 이동

![게시글 생성](..\final-pjt\final-pjt-front\src\assets\images\createpost.png)

- 우측 상단 create post 버튼 클릭시 게시글 작성 가능

### 5) 영화 검색

![영화 검색](..\final-pjt\final-pjt-front\src\assets\images\search.PNG)

- 검색 폼에 찾고 싶은 영화 제목의 일부를 입력

![영화 검색 결과](..\final-pjt\final-pjt-front\src\assets\images\search_result.PNG)

- 검색 string을 포함하는 모든 영화 카드로 출력

&nbsp;

### 6) 프로필

![프로필](..\final-pjt\final-pjt-front\src\assets\images\profile.PNG)

- 로그인 한 유저 또는 선택한 유저의 이름, 생년월일, 이메일, 팔로워 수, 회원등급을 표기

![프로필](..\final-pjt\final-pjt-front\src\assets\images\postlist.PNG)
![프로필](..\final-pjt\final-pjt-front\src\assets\images\reviewlist.PNG)
![프로필](..\final-pjt\final-pjt-front\src\assets\images\commentlist.PNG)

- 하단에는 해당 유저가 작성한 게시글, 영화리뷰, 댓글을 모아서 표기

### 7) Admin

![어드민 영화 페이지](..\final-pjt\final-pjt-front\src\assets\images\adminmain.PNG)

- 어드민으로 로그인 시 영화관리, 회원관리 버튼 활성화

![영화 관리](..\final-pjt\final-pjt-front\src\assets\images\managemovie.PNG)

- fixture에서 가져온 모든 영화의 번호, 코드, 제목, 개봉일, 추천 수, 평점을 표로 표시

![유저 관리](..\final-pjt\final-pjt-front\src\assets\images\userlist.PNG)

- 이용 중인 유저의 정보를 목록으로 표시하고, 삭제 가능

&nbsp;

## 6. 느낀 점

### \- 정재욱

- 프로젝트 시작 당시에만 해도 프론트와 백이 무엇인지에 대한 이론적인 개념은 있었으나 피부에는 와닿지 않는 느낌이였는데 짧은 기간 프로젝트를 진행 하는동안 많은 시행 착오를 거치고, 공부하며 무엇이 프론트이고 백인지, 어느 쪽이 나의 성향에 맞는 지를 느낀 게 가장 큰 수확이였고, 막막했던 처음과 다르게 점점 구도가 잡혀가고 형상이 잡혀가는 결과물을 보며 뿌듯함과 서로의 장점을 모아 1+1 이 3, 4가 될 수 있는 경험을 할 수 있었다.

### \- 안솔비

- 솔비

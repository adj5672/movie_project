# Final_Project - 2021. 05. 20 ~ 2021. 05. 28

> 영화 정보 기반 추천 서비스 구성 
>
> 커뮤니티 서비스 구성 
>
> HTML, CSS, JavaScript, Vue.js, Django, REST API, DataBase 등을 활용한 실제 서비 스 설계 
>
> 서비스 관리 및 유지보수

<br>

---

<br>

### 팀원 정보 및 업무 분담 내역

<br>

- #### 팀원

  SSAFY 5기 서울 3반 __`안건우`__,__`안동준`__ 

  <br>

- #### 업무 분담 내역

  Django Server & Vue component는 전부 같이 구성 및 코드 작성

  Vue Styling은 구역별로 나누어서 작업

<br>

---

<br>

### __MongCha__ 

`안건우` 님 께서 기르시는 강아지 이름은 __`"몽"`__ + 영화 스트리밍 사이트 __`"왓차"`__ 

![mongcha](README.assets/mongcha.png)

<br>

=> 완성된 영화 추천 사이트의 이름은 __`"몽차"`__ 

![logo](README.assets/logo.png)

<br>

---

<br>

### 목표 서비스 구현 및 실제 구현 정도

<br>

- #### 목표 서비스

  인기순 상위 10개의 영화 및 장르별 영화를 3D Carousel을 사용하여 사용자들에게 추천해주고 

  Instagram 처럼 리뷰에 태그를 다는 방식을 적용하고 이 정보를 바탕으로 사용자가 선택한 기분에 따라

  영화를 추천해주는 모델 및 알고리즘을 구성하려고 계획을 하였습니다. 

  그리고 Carousel Slide에 마우스를 올리면 애니메이션 효과와 함께 해당 영화에 대한 

  간단한 정보들을 사용자가 볼 수 있는 것을 목표로 하였습니다.

  <br>

  마이-페이지 및 로그인 페이지를 따로 만들지 않고 Sidebar Component를 사용하여 접근할 수 있도록

  계획을 세웠습니다. 그리고 마이-페이지에서 내가 "좋아요"를 누른 영화들을 모으거나 사용자가 

  작성한 리뷰, 댓글을 손쉽게 조회, 수정, 삭제 할 수 있도록 서비스를 제공하려고 하였습니다.

<br>

- #### 서비스 구현 정도

  모든 영화 추천 Carousel에 3D Carousel을 사용하여 사용자가 페이지를 보는 동안 

  지루함을 덜 느끼도록 구현하였으며 인기순 상위 10개의 영화 및 장르별 영화를 

  추천해 주는 기능을 잘 구현하였습니다. 🤩

  Carousel Slide에 마우스를 올렸을 때 애니메이션 효과는 없지만 해당 영화의 제목, 장르, 개봉일을

  볼 수 있도록 서비스를 구현하였습니다.

  <br>

  태그 기능의 경우, 처음에는 리뷰를 작성하는 사용자가 원하는 갯수 만큼, 원하는 내용으로 태그로 

  덧붙일 수 있는 기능을 제공하려고 계획했으나 그 기능은 전부 구현하지 못하였고

  대신 `#기쁨`, `#슬픔`, `#짜증`, `#심심`, `#사랑`, 이 5가지 태그 중 한개를 선택하여 

  리뷰를 작성하도록 만들었습니다. 그리고 이  5가지 태그를 기준으로 사용자가 선택한 태그와

  영화에 가장 많이 달린 태그가 일치하는 영화들을 추천해주는 기능을 구현하였습니다.

  <br>

  Sidebar에 로그인 및 마이-페이지를 구현하였고, 사용자가 등록한 프로필 사진을 Sidebar 상단에 

  보여주는 기능을 계획했으나 그 부분은 구현하지 못하였습니다. 

  마이-페이지에서 사용자가 "좋아요"를 누른 영화 목록들을 Card 형태로 볼 수 있도록 만들었고,

  사용자가 작성한 리뷰 및 댓글을 모아 볼 수 있어 쉽게 조회, 수정, 삭제가 가능합니다.

  다만 이 3개의 페이지 모두 Pagination이 적용되지 않았고 갯수가 많아지게 되면 스크롤이 계속 밑으로

  늘어나는 불편함이 발생할 것으로 예상됩니다.

<br>

---

<br>

### ERD

![](README.assets/ERD.png)

<br>

---

<br>

### 필수 기능에 대한 설명

<br>

- #### 영화 정보

  50개 이상의 영화 데이터 베이스 구현(900여 개)

  ![AllMovies](README.assets/AllMovies.png)

<br>

- #### 관리자 뷰 구현 ❌

<br>

- #### 전체 영화 페이지 구현

  - ##### 리스트

    인기순 top 10, 5개의 장르별(`로맨스`, `액션`, `판타지`, `공포`, `코메디`) 10개의 랜덤 영화의 포스터를 3D Carousel을 사용하여 출력

    시간이 지나면 자동으로 스크롤되는 3D Carousel 구현

    ![MovieList](README.assets/MovieList.png)

  <br>

  - ##### 포스터

    인기순 top 10 에서는 포스터의 왼쪽 하단에 순위 출력

    모든 포스터에 마우스 이동 시 영화의 간단한 상세정보(제목, 장르, 개봉날짜) 출력

    ![top10](README.assets/top10.gif)

    <br>

    모든 포스터의 오른쪽 상단에 "좋아요" 여부에 따라 하트 아이콘 출력

    

    ![like](README.assets/like.png)

<br>

- #### 상세 영화 페이지 구현

  해당 포스터를 클릭 시 Dialog의 형태로 영화의 상세정보 출력

  리뷰 데이터를 바탕으로 리뷰를 남긴 사용자들의 tag와 평점 평균 출력

  ![movie_detail](README.assets/movie_detail.gif)

  <br>

  리뷰 리스트 출력 및 리뷰 작성을 버튼으로 구현, 리뷰 리스트 5개씩 Pagination

  ![ReviewList](README.assets/ReviewList.png)

<br>

- #### 추천 영화 페이지 구현

  - ##### Tag

    리뷰 데이터를 바탕으로 리뷰를 작성한 사용자가 가장 많이 선택한 기분(tag)을 해당 영화의 기분(tag)으로 지정

    반응형 이모지를 활용하여 이모지 클릭 시, 해당 기분(tag)의 영화들을 3D Carousel을 사용하여 출력

    기분(tag)클릭 시 화면에 출력되는 "기분" Text의 색이 tag에 따라 변하도록 구현

    ![recommand](README.assets/recommand.gif)

<br>

- #### 커뮤니티

  - ##### 리뷰

    로그인한 사용자만 리뷰 조회 / 생성 및 작성자 본인만 글을 수정 / 삭제 기능 구현

    ![authorization](README.assets/authorization.png)

    <br>

    리뷰 작성 시 별점의 형태로 평점 기능 구현 (5점 만점)

    ![review_create](README.assets/review_create.png)

    <br>

    리뷰 정보에 해당 리뷰의 댓글 개수 출력

    ![review](README.assets/review.png)

  <br>

  - ##### 댓글

    게시글에 댓글 작성 및 수정 삭제 기능 구현

    ![review_comment2](README.assets/review_comment2.png)

    <br>

    모든 게시글 및 댓글에 생성 및 수정 시각 정보 포함

    Pagination을 활용, 페이지당 10개씩 댓글 출력

    ![review_comment](README.assets/review_comment.png)

<br>

- #### 기타

  - __회원가입__

    간단한 Form으로 회원가입 구현

    ![signup](README.assets/signup.png)

    <br>

  - ##### SideBar

    Hamburger Button(☰) 클릭 시 오른쪽에서 SideBar 생성

    로그인 form 출력

    SideBar 하단에 현재 시간 정보를 보여주는 시계 출력

    ![sidebar1](README.assets/sidebar1.png)

    <br>

  - ##### 사용자 페이지

    로그인시 Sidebar에 마이-페이지 구현

    ![login](README.assets/login.png)

    <br>

    로그인한 사용자의 "좋아요"한 영화들을 Card 형태로 출력해주는 페이지 구현

    ![mymovies](README.assets/mymovies.png)

    <br>

    로그인한 사용자의 리뷰들을  Card 형태로 보여주는 페이지 구현

    ![myreviews](README.assets/myreviews.png)

    <br>

    로그인한 사용자의 댓글들을  Card 형태로 보여주는 페이지 구현

    ![mycomment](README.assets/mycomment.png)

    <br>

- 보안

  dotenv를 사용하여 API_KEY, Django SECRET_KEY 숨김

  ![dotenv](README.assets/dotenv.png)

<br>

---

<br>

### 배포 서버 URL

배포 하지 못했습니다......😥

<br>

---

<br>

### 마치며....

<br>

#### __`안건우`__ 

교수님이 작년에 했던 프로젝트와 영상들을 보여줬을 땐 내가 할 수 있을까..? 겁이 많이 났었다.

때문에 처음에 어디서부터 시작해서 어떻게 코드를 짜야할지 갈피를 못잡았는데, 팀원(동준)이 순서대로 진행해야 할 코드를 잘 알려주고 이끌어줘서 이렇게 완성할 수 있었던 것 같다.

또 시간 남으면 추가 기능들을 구현해보자는 가벼운 마음으로 임했는데, 주말과 평일 저녁시간까지 프로젝트에 몰두하는 팀원(동준)을 보면서 나도 열심히 하자는 마음을 먹었다. 그래서 팀원(동준)에게 고마운 마음이 크다.

이렇게 완성된 프로젝트와 영상까지 제작하며 짧지만 길었던 일주일간의 기간이 뿌듯하고 자랑스럽다. 하지만 6개월간의 1학기가 끝나는 마지막 프로젝트로서는 아쉬운 마음도 든다. 

2학기도 열심히 임했던 1학기처럼 끝까지 열심히 임하자는 다짐으로 느낀점 끝:blush:

<br>

#### __`안동준`__

...




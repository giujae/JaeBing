<template>
  <!-- 전체 디브 -->
  <div id="main">
    <!-- 네브바 있는 헤더 -->
    <header>
      <nav class="nav fixed-top">
        <a href="/" class="home font-weight-bold">Home</a>
        <div>
        <router-link :to="{ name: 'Signup' }" class="nav-margin">
          <button class="font-weight-bold">SignUp</button>
        </router-link>
        <router-link :to="{ name: 'Login' }" class="nav-margin">
          <button class="font-weight-bold">Login</button>
        </router-link>
      </div>
      </nav>
      <router-view @login="login = true" />
    </header>
    <div v-if="this.$route.path == '/'">
      <!-- 텍스트 박스 먹은 비디오 박스 -->
      <div class="video-box">
        <!-- 비디오 박스 -->
        <div class="jb-box">
          <video muted autoplay loop>
            <source src="@/Legend.mp4" type="video/mp4" >
            <strong>Your browser does not support the video tag.</strong>
          </video>
        </div>

        <!-- 비디오 내에 보이는 텍스트 박스 -->
        <div class="message-title jb-text">
          <p class="fw-bold">내가 찾던 재미</p>
          <p>보고 싶은 콘텐츠를 발견하세요!</p>
          <p>최신, 인기 TV프로그램, 영화</p>
          <p>해외시리즈, 파라마운트+ 오리지널 및 독점</p>
        </div>
      </div>
      <!-- 비디오 박스 끝 -->

      <!-- 이미지 슬라이드 디브 -->
      <div class="flow-scene-wrap">
        <div class="flow-scene-first">
          <!-- ul박스 -->
          <ul class="first-ul-1">
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P000643144.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P000643144.jpg/dims/resize/1024"
                  alt="유 퀴즈 온 더 블럭 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001706762.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001706762.jpg/dims/resize/1024"
                  alt="장사천재 백사장 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001693843.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001693843.jpg/dims/resize/1024"
                  alt="방과 후 전쟁활동 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001691763.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001691763.jpg/dims/resize/1024"
                  alt="래빗홀 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001710496.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001710496.jpg/dims/resize/1024"
                  alt="닥터 차정숙 포스터"
                />
              </picture>
            </li>
          </ul>
        </div>
        <!-- flow-scene-first div -->
      </div>
    </div>
    <!-- flow-scene-wrap div -->

    <!-- 사이트 정보? -->
    <footer>
      <p>제비 스튜디오</p>
      <button>
        전화문의
        <a
          href="data:image/jpeg;base64,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"
        >
        </a>
      </button>
    </footer>
  </div>
  <!-- main div -->
</template>

<script>
export default {
  mounted() {
    var originalID, cloneID; //인터벌 포인터
    //롤링 배너 복제본 생성
    let roller = document.querySelector('.flow-scene-first');
    roller.id = 'roller1';

    let clone = roller.cloneNode(true);
    clone.id = 'roller2';
    document.querySelector('.flow-scene-wrap').appendChild(clone); //부착

    //원본, 복제본 배너 위치 지정
    document.querySelector('#roller1').style.left = '0px';
    document.querySelector('#roller2').style.left = document.querySelector('.flow-scene-first ul').offsetWidth + 'px';

    //클래스 할당
    roller.classList.add('original');
    clone.classList.add('clone');

    //인터벌 메서드로 애니메이션 생성
    let rollerWidth = document.querySelector('.flow-scene-first ul').offsetWidth; //회전 배너 너비값
    let betweenDistance = 1; //이동 크기 - 정수여야 함

    //롤링 시작
    function startRoller() {
      originalID = window.setInterval(
        betweenRollCallback,
        parseInt(1000 / 100),
        betweenDistance,
        document.querySelector('#roller1')
      );
      cloneID = window.setInterval(
        betweenRollCallback,
        parseInt(1000 / 100),
        betweenDistance,
        document.querySelector('#roller2')
      );
    }

    // 정지 안쓰려면 아래 주석하심 됩니다? 안호구씨 그리고 위에 변수 지워주고 originalID, cloneID 이거 두개
    //롤링 정지
    function stopRoller() {
      clearInterval(originalID);
      clearInterval(cloneID);
    }

    //마우스 호버시 롤링이 멈추었다 벗어나면 다시 롤링이 되도록 처리
    document.getElementById('roller1').addEventListener('mouseover', () => {
      stopRoller();
    });
    document.getElementById('roller2').addEventListener('mouseover', () => {
      stopRoller();
    });
    document.getElementById('roller1').addEventListener('mouseout', () => {
      startRoller();
    });
    document.getElementById('roller2').addEventListener('mouseout', () => {
      startRoller();
    });

    //인터벌 애니메이션 함수(공용)
    function betweenRollCallback(d, roller) {
      let left = parseInt(roller.style.left);
      roller.style.left = left - d + 'px'; //이동
      //조건부 위치 리셋
      if (rollerWidth + (left - d) <= 0) {
        roller.style.left = rollerWidth + 'px';
      }
    }

    startRoller(); //롤링 초기화
  },
};
</script>

<style>
@font-face {
    font-family: 'EF_watermelonSalad';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-EF@1.0/EF_watermelonSalad.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

/* 도화지 배경 */
html {
  /* background-color: #0F2648; */
  background: linear-gradient(45deg, #e8d1d9, #3c537f, #101130);
}

/* 바디 배경 */
body {
  padding: 0px;
  margin: 0px;
}

/* 비디오 박스 */
.jb-box {
  width: 100%;
  height: 800px;
  overflow: hidden;
  margin: 0px auto;
  position: absolute;
}

/* 비디오 */
video {
  width: 100%;
  opacity: 0.45;
}

/* 텍스트 박스 */
.jb-text {
  position: absolute;
  top: 20%;
  width: 100%;
}

/* 텍스트 박스 내 텍스트 속성 */
.jb-text p {
  margin-top: -24px;
  text-align: center;
  font-size: 48px;
  color: #e8d1d9;
}

/* 전체 페이지 속성 */
#main {
  font-family: 'EF_watermelonSalad';
  background-color: #101130;
  /* background: linear-gradient(45deg, #E8D1D9, #3C537F, #0f2648); */
  color: #e8d1d9;
  text-align: center;
}

/* 버튼들있는 네브바 */
.nav {
  color: #e8d1d9;
  display: flex;
  justify-content: space-between;
}

/* 홈 버튼 속성 */
.home {
  text-decoration-line: none;
  padding: 8px;
  color: #e8d1d9;
  background-color: #10113000;
  width: 70px;
  height: 40px;
}

/* 로그인 버튼 속성 */
button {
  margin: 10px;
  background-color: #10113000;
  /* border-color: #E8D1D9;; */
  color: #e8d1d9;
  width: 70px;
  height: 40px;
}

/* 버튼 클릭시 색변경 */
button:hover,
a:hover {
  color: #d5b0c1;
}

/* 각 태그들 점 없애기 */
dl,
li,
ol,
ul {
  list-style: none;
}

/* 슬라이드 이미지 속성 */
img {
  border-radius: 5px;
  width: 350px;
  height: 200px;
  margin: 10px;
}

.flow-scene-wrap {
  overflow: hidden;
  height: 800px;
}

.flow-scene-first {
  position: absolute;
  top: 50%;
}

.flow-scene-first > ul {
  margin: 0;
  list-style: none;
  padding: 9px 0;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.first-ul-1 {
  height: 200px;
  bottom: 100%;
  position: relative;
}

.flow-scene-second ul {
  display: flex;
  /* width: 300%; */
  animation: slidein 6s infinite linear;
  animation-timing-function: linear;
}

@keyframes slidein1 {
  0% {
    transform: translateX(30%);
  }
  50% {
    transform: translateX(-70%);
  }
  50.01% {
    transform: translateX(70%);
  }
  100% {
    transform: translateX(30%);
  }
}

@keyframes slidein2 {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-200%);
  }
}

/* 애니메이션 */
.roller.original {
  animation: 33s linear 0s infinite normal forwards running rollingleft1;
}
.roller.clone {
  animation: 33s linear 0s infinite normal none running rollingleft2;
}
@keyframes rollingleft1 {
  /* 원본용 */
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-100%);
  }
  50.01% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}

  /* 클론용 */
/* @keyframes rollingleft2 {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-200%);
  }
} */

footer {
  width: 100%;
  height: 150px;
}
</style>

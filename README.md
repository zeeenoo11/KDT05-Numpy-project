# _KDT05-Numpy_Project_

경북대학교 KDT(Korea Digital Training) 빅데이터 전문가 양성과정 5기 : Numpy 1팀입니다

이화은 : [깃허브 링크](https://github.com/Skylee0310)  
전진우 : [깃허브 링크](https://github.com/zeeenoo11)  
옥영신 : [깃허브 링크](https://github.com/YeongshinOk)  
명노아 : [깃허브 링크](https://github.com/noah2397)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)

<hr/>

#### 개발환경

| 패키지 이름 | 버전   | 사용 커맨드(Version command) |
| ----------- | ------ | ---------------------------- |
| Python      | 3.8.18 | python --version             |
| jupyter     | 1.0.0  | pip show jupyter             |
| ipython     | 8.12.2 | pip show ipython             |
| notebook    | 7.0.6  | pip show notebook            |
| numpy       | 1.24.3 | pip show numpy               |
| pandas      | 2.0.3  | pip show pandas              |
| matplotlib  | 3.7.2  | pip show matplotlib          |
| statsmodels | 0.14.0 | pip show statsmodels         |

<hr/>

### KDT(Korea Digital Training)-Numpy Project(통계분석)

<hr/>

#### 사용한 데이터 사이트

1. [KBO 홈페이지](https://www.koreabaseball.com/Default.aspx)
2. [Daum 스포츠-야구](https://sports.daum.net/record/kbo/team?season=2023)
3. [구글공유 PPT](https://docs.google.com/presentation/d/1iw8iwN1F_FjeJlKNg46WBwOhtqjZGTJt9zUaESa8WAY/edit)

<hr/>

###### 주제 : 야구 통계 분석

- 목차

* 1. 배경
* 2. OPS와 승률 상관관계 분석(옥영신)
* 3. 구단별 승리와 인기의 관계(이화은)
* 4. 구단별 승리 요인 분석(명노아)
* 5. 삼성 김성윤 키우기(전진우)

###### 역할 분담

|          역할 | 참여인원                       |
| ------------: | ------------------------------ |
|      주제선정 | 이화은, 명노아, 전진우, 옥영신 |
|          코딩 | 이화은, 명노아, 전진우, 옥영신 |
|          발표 | 이화은, 명노아, 전진우, 옥영신 |
|       git관리 | 이화은, 명노아, 전진우, 옥영신 |
|   Readme 작성 | 명노아, 이화은                 |
|      PPT 제작 | 이화은, 명노아, 전진우, 옥영신 |
| PPT 관리,병합 | 전진우                         |

### 소주제 개요(개인 항목)

<details>
  <summary>
    각 구단별 승률과 인기 사이의 상관 관계(이화은)
  </summary>
  
  ◎ 개인 주제 : 각 구단별 승률과 인기 사이 상관 관계

1. 배경 :  
   ▶ 야구를 잘 모르는 입장에서 사람들이 특정 야구 팀을 선호하는 이유에 대한 의문.  
   ▶ '사람들은 승률이 높은 팀을 선호하는가?'

2. 분석 방법 :  
   ▶ 인기를 객관적인 자료로 나타내는 것은 불가능  
   => 홈 경기 기준 관중 수를 바탕으로 각 구단의 인기를 추론.

3. 본론 :

1) 한국 프로 야구 인기 추이

- 자료 : 연도별 관중 현황(2015년 ~ 2023년)  
  ▶ 현재 존재하는 모든 구단이 창설된 이후인 2015년 이후부터 가장 최근 시즌인 2023년까지로 자료 한정.  
  ▶ 2018년 아시안게임 출전 선수 선정 관련 논란에 이어 2019년 프로야구 오심 및 수준 저하 논란 발생으로 소폭 감소.  
  ▶ 2020년 코로나 이슈 발생으로 뒤늦은 개막과 더불어 전반기 시즌 종료.  
  ▶ 2021년 ~ 2022년 꾸준한 회복세가 이어져 2023년에는 코로나 이전과 비슷한 수를 보임.

2. 최근 3년 사이 인기 구단

- 자료 : 일자별 관중 현황(2021년~2023년)  
  ▶ 코로나 확산으로 인해 경기 취소된 경우로 인해 각 구장 별 경기 수가 일치하지 않아 일평균 관중 수를 도출하여 사용.  
  ▶ 삼성 라이온즈를 제외하고는 LG, 두산, SSG 등 수도권에 인기 구단이 집중되어 있음.

3. 인기와 승률의 관계

- 자료 : 일자별 관중 현황(2021년~2023년) + 팀 순위(2021년 ~2023년)  
  => 각 구단의 승률과 홈구장에서 경기를 할 때 관중 수의 관계를 산점도로 도출.  
  ※ 승률 순위와 실제 시즌 순위가 일치 하지는 않음.(-> 정규시즌 1위로 포스트시즌에 진출했으나 플레이오프에서 좋은 결과를 얻지 못한 경우 존재.)  
  ▶ 승률이 높다고 해서 관중수가 많지는 않음. = > 상관 관계 불명확.

4. 인기와 지역 사이 관계

- 자료 : 구장별 관중 현황(2021년 ~2023년) + 행정구역*시군구*별\_주민등록세대수(구장이 있는 지역만 추출)  
  ▶ 서울의 경우 다른 지역보다 인구 수가 많고 관중수도 평균보다 높은 편.  
  ▶ 전체적으로 그밖 지역에서는 비례관계를 이루고 있음.

4. 결론 :  
▶ 어떤 야구 팀을 선호하는 이유에는 승률보다 주거 지역이 더 큰 영향을 끼치고 있음.
</details>

<details>
  <summary>
    구단별 승리 요인 분석(명노아)
  </summary>
  
  ◎ 개인 주제 : 구단별 승리 요인 분석

1. 배경 :  
   ▶ 어떤 자질을 가진 팀들이 더 우승할 확률이 높은가?  
   ▶ 최종적으로 어떤 근본적인 요인이 우승의 당락을 결정할까?

2. 분석 방법 :  
   ▶ Daum 스포츠 사이트에 있는 각 연도별 구단별 승률 데이터를 수집.  
   ▶ 종합순위, 공격순위, 수비순위 3개의 데이터 프레임을 합침  
   ▶ 각 년도별(2007~2023년)의 자료를 행 방향으로 통합  
   ▶ DBeaver를 통해 데이터베이스를 연결하고 ipynb파일에서 데이터베이스와 연결하여 사용

3. 본론 :  
   ▶ 상관관계 분석을 했을 때, 수비관련 지표(평균자책, WHIP, 세이브)에서 의외의 연관성을 찾을 수 있다  
   ▶ 각 구단의 상위 30%의 값을 가지는 구단들은 연도를 통틀어 상위권의 순위를 기록했음을 확인할 수 있다  
   ▶ 수비 지표 관련 상위 30%을 가지는 역대 구단들과, 전체 구단의 범위값을 비교하여 승률이 높은 지표를 마련함  
   ▶ SQL를 사용하여 평균적으로 성적이 좋은 팀들을 2007~2023까지 뽑아내었고, 결과는 다음과 같다  
   ▶ 2007~2010 : SK의 전성기  
   ▶ 2011~2014 : 삼성의 전성기  
   ▶ 2015~2019 : 두산의 전성기  
   ▶ 2019~2020 : 키움 및 LG의 시스템적 성장  
   ▶ 2021~2023 : LG의 전성기  
   ▶ 뉴스 기사들로 미루어 보았을 때, 결국 선수와 감독이 중요하다

4. 자료 : Readme파일의 출처 참고  
   ▶ LG, 삼성, SK의 성공 요인과 실패 요인  
   ▶ 한화의 류현진 기용으로 인한 기대감 증가

5. 결론 :  
▶ 구단의 승패를 당락짓는 요소는 수비관련 지표에서 많이 찾아볼 수 있다  
▶ 결정적으로 중요한 것은 구단의 시스템과, 선수들이다
</details>
<hr/>

###### 출처/데이터

|                                 관련 자료명                                 | URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                               KBO-규정/자료실                               | [링크](https://www.koreabaseball.com/Kbo/Board/Ebook/EbookPublication.aspx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                KBO-선수 기록                                | [링크](https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx?sort=HRA_RT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                KBO-선수 조회                                | [링크](https://www.koreabaseball.com/Player/Search.aspx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                              KBO-경기일정/결과                              | [링크](https://www.koreabaseball.com/Futures/Schedule/GameList.aspx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                KBO-관중 현황                                | [링크](https://www.koreabaseball.com/Record/Crowd/GraphDaily.aspx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                 KBO-팀 순위                                 | [링크](https://www.koreabaseball.com/Record/TeamRank/TeamRank.aspx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                          Daum 스포츠-야구 KBO리그                           | [링크](https://sports.daum.net/record/kbo/team?season=2023)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                             Google-pptx 템플릿                              | [링크](https://slidesgo.com/?login=uTUFP1GgVWY019c0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                             Canva-공용 PPT URL                              | [링크](https://www.canva.com/design/DAF9eLxeoSE/k4sK7r1k-U1gktwU6cQ_4w/edit?)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                [프로야구] SK 우승 동력, '벌떼 야구'의 승리!                 | [링크](https://news.sbs.co.kr/news/endPage.do?news_id=N1000316844)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                    역대 왕조라 불리운 팀들 3.SK와이번스                     | [링크](https://blog.naver.com/pkijj04/221195058422)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                 구광모 ‘Beyond LG’, 더 독해지고 과감해졌다                  | [링크](https://shindonga.donga.com/economy/article/all/13/4759990/1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                             ‘류현진 한화 복귀’                              | [링크](https://www.sportsseoul.com/news/read/1400883?ref=naver)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 10위-10위-9위 한화, 단숨에 우승후보?…메이저리거 오승환·추신수·김광현 어땠나 | [링크](https://www.seoul.co.kr/news/2024/02/21/20240221500066)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                       두산 송일수 감독, 1년 만에 경질                       | [링크](https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0002045673#:~:text=%ED%95%9C%EA%B5%AD%20%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC%20%EB%91%90%EC%82%B0%20%EB%B2%A0%EC%96%B4%EC%8A%A4%EA%B0%80%201%EB%85%84%20%EB%A7%8C%EC%97%90%20%EA%B0%90%EB%8F%85%EC%9D%84%20%EB%8B%A4%EC%8B%9C,%EB%B0%B0%ED%84%B0%EB%A6%AC%20%EC%BD%94%EC%B9%98%EB%A1%9C%20%EC%9E%88%EB%8D%98%20%EA%B9%80%ED%83%9C%ED%98%95%EC%9D%84%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EA%B0%90%EB%8F%85%EC%9C%BC%EB%A1%9C%20%EC%98%81%EC%9E%85%ED%96%88%EB%8B%A4%EA%B3%A0%20%EB%B0%9D%ED%98%94%EB%8B%A4.) |
|                          삼성라이온즈 암흑기 이유                           | [링크](https://blog.naver.com/dtd00550/223033125717)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|               [OB - 두산베어스]한국시리즈 역대 여섯 번의 우승               | [링크](https://blog.naver.com/bearsball10/222869164378)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|               류현진 내년 예상 성적 "6승 5패 평균자책점 4.38"               | [링크](https://www.yna.co.kr/view/AKR20231123130900007#:~:text=%EC%9E%90%EB%A3%8C%EC%97%90%20%EB%94%B0%EB%A5%B4%EB%A9%B4%20%EB%A5%98%ED%98%84%EC%A7%84%EC%9D%98%202024%EC%8B%9C%EC%A6%8C%20%EC%98%88%EC%83%81%20%EC%84%B1%EC%A0%81%EC%9D%80%2017%EA%B2%BD%EA%B8%B0%20%EC%84%A0%EB%B0%9C%2C,%EC%97%AC%EC%A0%84%ED%95%B4%EB%8F%84%20%EC%82%BC%EC%A7%84%EC%9D%84%20%EC%9E%A1%EB%8A%94%20%EB%8A%A5%EB%A0%A5%EC%9D%80%20%EB%96%A8%EC%96%B4%EC%A7%88%20%EA%B2%83%EC%9D%B4%EB%9D%BC%EB%8A%94%20%EC%A0%84%EB%A7%9D%EC%9D%B4%20%EB%82%98%EC%99%94%EB%8B%A4.)                            |

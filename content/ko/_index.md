---
# Leave the homepage title empty to use the site title
title: 
date: 2022-10-24
type: landing


sections:
  - block: hero
    content:
      title: |

      
        안녕하세요.. 
        연재입니다.
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        🍠🍠🍠🍠🍠🍠🍠🍠🍠

        겨울엔 고구마를 드세요..
        <br>

        <small style="color: #aeaeaeff; font-size: 0.7rem;">
          <a href="/python/sweetpotato.py" style="color: #5c5c5cff;" download>
            Python Turtle로 그린 보라색 고구마 🎨
          </a><br>
        첫 페이지에는 제가 가장 좋아하는 겨울 간식 고구마를 담아보았습니다. 파이썬 터틀 모듈을 이용해 고구마 캐릭터를 만들어보았는데요, 위 텍스트를 누르면 실행 파일이 다운로드 됩니다. 다운하셔서 즐겨보세요!
        </small>      
      
      
  
  - block: features
    id: features
    content:
      title: Information
      items:
        - name: 이름
          icon: user
          icon_pack: fas
          description: 최연재
        - name: 생년월일
          icon: calendar-days
          icon_pack: fas
          description: 2002.12.24
        - name: 연락처
          icon: phone
          icon_pack: fas
          description: 010-2542-2638
        - name: 이메일
          icon: envelope
          icon_pack: fas
          description: cyj0749@naver.com
        - name: 학력
          icon: graduation-cap
          icon_pack: fas
          description: 전북대학교 it지능정보공학과
        - name: 위치
          icon: location-dot
          icon_pack: fas
          description: 전북대학교 공과대학 7호관
    design:
      columns: '3'
        
  
  - block: collection
    content:
      title: Projects
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: slider
    content:
      title: Projects
      slides:
      - title: 쿠키런 프로젝트
        content: 
        align: center
        background:
          image:
            filename: cookie.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
        link:
          text: 프로젝트 보러가기
          url: ../cookierun/
      - title: netflix clone
        content: 
        align: center
        background:
          image:
            filename: netflix.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          text: 프로젝트 보러가기
          url: ../netflix/
      - title: studentmanagement
        content: 
        align: center
        background:
          image:
            filename: studentss.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          text: 프로젝트 보러가기
          url: ../studenmanagement/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000

  # - block: collection
  #   content:
  #     title: Latest Preprints
  #     text: ""
  #     count: 5
  #     filters:
  #       folders:
  #         - publication
  #       publication_type: 'article'
  #   design:
  #     view: citation
  #     columns: '1'

  - block: accomplishments
    id: certificates
    content:
      title: 🎓 자격증
      items:
        - title: IELTS
          organization: IDP
          date_start: '2024-08-31'
          date_end: ''
          description: |
            IDP에서 주관하는 국제 영어 능력 시험인 IELTS를 완료하여 영어 듣기, 읽기, 쓰기, 말하기 영역에서의 능력을 입증받았습니다.
          link:
            text: 자세히 보기
            url: awards/certification
            
        - title: 네트워크 관리사 2급 (필기)
          organization: 한국정보통신자격협회
          date_start: '2024-05-19'
          date_end: ''
          description: |
            TCP/IP, OSI 모델, 네트워크 보안 및 실무적인 네트워크 관리 능력 인증
          link:
            text: 자세히 보기
            url: awards/certification
            
        - title: 리눅스마스터 2급
          organization: 대한검정회
          date_start: '2024-09-13'
          date_end: ''
          description: |
            리눅스 운영체제의 기본 관리, 명령어 활용, 서버 설정 및 네트워크 운용 능력을 인증
          link:
            text: 자세히 보기
            url: awards/certification
            
    design:
      columns: '3'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./contact/" cta_text="contact me →" %}}
    design:
      columns: '1'
---
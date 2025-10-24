---
# Leave the homepage title empty to use the site title
title: 
date: 2022-10-24
type: landing


sections:
  - block: hero
    content:
      title: |

      
        안녕하세요.. 연재입니다.
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        🍠🍠🍠🍠🍠🍠🍠🍠🍠

        겨울엔 고구마를 드세요..
  
  - block: features
    id: features
    content:
      title: Information
      text: 최연재의 정보
      items:
        - name: 이름
          icon: user
          icon_pack: fas
          description: 최연재
        - name: 생년월일
          icon: calendar-days
          icon_pack: fas
          description: 2002.12.24
        - name: 위치
          icon: location-dot
          icon_pack: fas
          description: 전북대학교 공과대학 7호관
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
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./contact/" cta_text="contact me →" %}}
    design:
      columns: '1'
---
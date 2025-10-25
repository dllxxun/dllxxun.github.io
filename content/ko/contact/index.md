---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title: ''
      text: ''
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 0.8
          size: cover
          position: center
        text_color_light: true
      spacing:
        padding: ['200px', '0', '100px', '0']
      css_class: page-banner

  - block: contact
    content:
      title: Contact
      text: |-
        저를 찾아보세요..
      email: cyj0749@naver.com
      phone: 010-2542-2638
      address:
        street: 전북대학교 공대7호관
      coordinates:
        latitude: '35.84614386613747'
        longitude: '127.13450518747047'
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'
---

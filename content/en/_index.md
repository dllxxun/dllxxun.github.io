---
# Leave the homepage title empty to use the site title
title: 
date: 2022-10-24
type: landing


sections:
  - block: hero
    content:
      title: |

      
        Hello, this is Yeonjae
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        🍠🍠🍠🍠🍠🍠🍠🍠🍠

        Eat sweet potatoes in winter..
  
  - block: features
    id: features
    content:
      title: Information
      items:
        - name: name
          icon: user
          icon_pack: fas
          description: Yeonjae Choi
        - name: Date of Birth
          icon: calendar-days
          icon_pack: fas
          description: 2002.12.24
        - name: Contact
          icon: phone
          icon_pack: fas
          description: 010-2542-2638
        - name: Email
          icon: envelope
          icon_pack: fas
          description: cyj0749@naver.com
        - name: Education
          icon: graduation-cap
          icon_pack: fas
          description: Department of IT Intelligent Information Engineering, Jeonbuk National University
        - name: Location
          icon: location-dot
          icon_pack: fas
          description: College of Engineering Building 7, Jeonbuk National University
    design:
      columns: '3'
  
  - block: slider
    content:
      title: Projects
      slides:
      - title: Cookierun Project
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
          text: View Project
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
          text: View Project
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
          text: View Project
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
      title: 🎓 Certificates
      items:
        - title: IELTS
          organization: IDP
          date_start: '2024-08-31'
          date_end: ''
          description: |
            Completed the International English Language Testing System (IELTS) conducted by IDP, demonstrating proficiency in listening, reading, writing, and speaking.
            
            
        - title: Network Manager Level 2 (Written)
          organization: Korea Information and Communication Qualification Association
          date_start: '2024-05-19'
          date_end: ''
          description: |
            Certified in TCP/IP, OSI model, network security, and practical network management skills.
            
        - title: Linux Master Level 2
          organization: Korea Chamber of Informatization
          description: |
            Certified for proficiency in basic Linux administration, command-line usage, server configuration, and network operation.
            
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
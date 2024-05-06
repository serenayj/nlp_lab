---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
       title: |
            Welcome
       image:
          filename: lab_welcome.png  
  - block: hero
    content:
      title: |
        # LARK Lab
        Welcome
      #image:
      #  filename: lab_welcome.png
        
      design:
        banner:
          # Upload a cover image to `assets/media/` folder and reference its filename here (optional)
          filename: lab_welcome.png
   
  
  - block: collection
    content:
      title: Latest News (test) # under post
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
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---

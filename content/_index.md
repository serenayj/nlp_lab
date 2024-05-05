---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        LARK Lab 
      image:
        filename: images/lab_logo.jpg
      text: |
        <br>
    
        The LARK lab at University of Colorado, Anschutz is at the forefront of advancing language technologies to enhance real-world applications, particularly in medicine and health. By developing foundational technologies and conducting cutting-edge research in natural language processing (NLP) with innovative artificial intelligence (AI), the lab is dedicated to creating powerful tools that tackle critical healthcare challenges and integrate seamlessly into healthcare systems. We are seeking passionate individuals who are driven to significantly impact the field through groundbreaking research and inventive solutions. 
  
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

#!/bin/bash

python yaml-resume-to-json.py \
  && resume export web/index.html -t stackoverflow \
  && resume export web/short.html -t short \
  && resume export web/crisp.html -t crisp \
  && scp resume.yaml web/* cs:~/public_html/resume/

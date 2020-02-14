#!/bin/bash

LOGDIR="/home/ubuntu/git/django_project"

DATE=`date -d "yesterday" +"%Y-%m-%d"`

NEWDIR="/home/ubuntu/git/django_project/logs"

mv ${LOGDIR}/uwsgi.log  ${NEWDIR}/uwsgi-${DATE}.log

touch /home/ubuntu/git/django_project/logs/.touchforlogrotat

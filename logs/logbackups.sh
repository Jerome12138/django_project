#!/bin/bash
# 自动备份日志
BASEDIR="/home/ubuntu/git/django_project"

DATE=`date -d "yesterday" +"%Y-%m-%d"`

NEWDIR="/home/ubuntu/git/django_project/logs"

mv ${BASEDIR}/uwsgi.log  ${NEWDIR}/uwsgi-${DATE}.log

touch ${BASEDIR}/uwsgi.log

touch ${BASEDIR}/logs/.touchforlogrotat


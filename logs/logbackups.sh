#!/bin/bash
# 自动备份日志
BASEDIR="/home/ubuntu/git/django_project"

DATE=`date -d "yesterday" +"%Y-%m-%d"`

MONTH=${DATE%-*}

NEWDIR="/home/ubuntu/git/django_project/logs"

mkdir -p ${NEWDIR}/${MONTH}

mv ${BASEDIR}/uwsgi.log  ${NEWDIR}/${MONTH}/uwsgi-${DATE}.log

touch ${BASEDIR}/uwsgi.log

touch ${BASEDIR}/logs/.touchforlogrotat


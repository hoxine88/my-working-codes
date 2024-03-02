#!/bin/bash

#create variables
BACKUP_SRC="/home/hoxine88/Desktop/SRC_FILE"
BACKUP_DST="/home/hoxine88/Desktop/DST_FILE"
BACKUP_DATE=$(date +%Y%m%d%H%M%S)

mkdir -p "$BACKUP_DST/$BACKUP_DATE"
#archive the source directory
cp "$BACKUP_SRC"/* "$BACKUP_DST/$BACKUP_DATE/"
#verify is the backup is created succussfully
if [ $? -eq 0 ];
then
	echo "backup successfully"
else
	echo "backup failed"
fi

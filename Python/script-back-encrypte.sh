#!/bin/bash

#create variables
BACKUP_SRC="/home/hoxine88/Desktop/SRC_FILE"
BACKUP_DST="/home/hoxine88/Desktop/DST_FILE"
BACKUP_DATE=$(date +%Y%m%d%H%M%S)
BACKUP_FILENAME="backup_$BACKUP_DATE.tar.gz"

mkdir -p "$BACKUP_DST/$BACKUP_DATE"
#archive the source directory
tar -czf "$BACKUP_DST/$BACKUP_DATE/$BACKUP_FILENAME" "$BACKUP_SRC"
#verify is the backup is created succussfully
if [ $? -eq 0 ];
then
	echo "backup successfully"
else

echo "backup failed"
#!/bin/bash
set -e
BOOK=../book/docs
if [ -d $BOOK ] ; then
  echo "Updating shared docs from $BOOK ..."
  cp -a $BOOK/shared docs/
  cp -a $BOOK/copyright.rst docs/
fi
